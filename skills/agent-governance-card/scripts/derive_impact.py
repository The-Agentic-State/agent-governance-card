#!/usr/bin/env python3
"""Deterministic Impact Level derivation per card v0.3 (two-output model).

Self-contained (stdlib only), bundled with the skill and PINNED to
derivation_contract_version 2. If the schema (or a fill) declares a different
contract version, do NOT run this engine — flag that the skill needs updating
rather than risk miscomputing a tier.

Usage:
    derive_impact.py fill.json           ->  JSON verdict on stdout, exit 0
    derive_impact.py --check anchors_dir ->  verify anchor-*.json against their
                                             _expected blocks; exit 1 on mismatch
Exit codes: 0 ok · 1 anchor mismatch · 2 malformed input · 3 contract mismatch.

The governance level is the HIGHER of two independently-computed outputs:

  (1) OMB high-impact status  — from C7 (R1, faithful M-25-21 test):
        high_impact                        -> HIGH
        presumed_high_but_determined_not   -> not high (determination recorded, C7a)
        not_high_impact                    -> not high
        not_yet_determined / unanswered    -> level is PROVISIONAL (see below)

  (2) Operational tier — from C8, C10, C11, C11a (severity), C12 (R2/R12):
        HIGH if any:
          - C12 == yes_unresolved
          - C10 == acts_without_approval AND (C11 == hard_to_reverse OR severity >= serious)
          - C8 == sensitive AND C10 == acts_without_approval
        MODERATE if any (and not High):
          - C8 in {personal_pii, sensitive}
          - C10 in {acts_with_approval, acts_without_approval}
          - severity >= limited AND C10 != informs
          - C12 == yes_with_compensating_controls
        LOW otherwise.

  Unknown-floor (R3/R6): if ANY operational-tier input is unknown, the tier cannot
  be Low — it is floored at Moderate until the unknown is resolved.

Contract 2 (card v0.3, legal review F2/F7) — THE CARD NEVER BLOCKS:
  - A pending C7 no longer yields the contract-1 blocking value: the final level
    is the operational tier with level_provisional=true, and completing the OMB
    determination lands in to_resolve.
  - to_resolve is a list of {code, recommendation} — strong, welcoming
    recommendations, never prohibitions (binding only where an adopting
    directive says so).
  - part2_groups narrows to automation_detail + oversight when Moderate ONLY
    because of the unknown-floor (honesty costs ~7 questions, not 19).

The verdict keeps the earlier result keys (impact_level, fired_triggers,
boundary, unknown_inputs, level_fragile, inputs) so existing tooling can read
it; impact_level is now always a tier string (low/moderate/high).
"""
import json
import sys
from pathlib import Path

# Contract version this engine understands. Bump ONLY together with a schema
# derivation-contract bump (see schema/README.md); the two are asserted to stay
# in lockstep before any release.
EXPECTED_CONTRACT_VERSION = 2

# Derivation-contract constants, inlined so the script runs anywhere the skill
# is copied, with no dependency on the schema file being present.
DERIVATION_INPUTS = ["C7", "C8", "C10", "C11", "C11a", "C12"]
OPERATIONAL_TIER_INPUTS = ["C8", "C10", "C11", "C11a", "C12"]
SEVERITY_ORDER = {"negligible": 0, "limited": 1, "serious": 2, "severe": 3}

_LEVEL_RANK = {"low": 0, "moderate": 1, "high": 2}
_ALL_EXTENDED_GROUPS = ["identity_delegation", "automation_detail", "oversight",
                        "redress", "cost_lockin"]
_FLOORED_GROUPS = ["automation_detail", "oversight"]  # F7 reduced set (E6-E12)


def _value(fill, fid):
    f = fill.get("fields", {}).get(fid)
    if not isinstance(f, dict) or f.get("status") != "answered":
        return None
    return f.get("value")


def derive(fill):
    v = {fid: _value(fill, fid) for fid in DERIVATION_INPUTS}
    unknown_all = [fid for fid, val in v.items() if val is None]
    unknown_op = [fid for fid in OPERATIONAL_TIER_INPUTS if v[fid] is None]

    # ---- Output 1: OMB high-impact status (R1) ----
    c7 = v["C7"]
    if c7 == "high_impact":
        omb_status, omb_level = "high_impact", "high"
    elif c7 in ("presumed_high_but_determined_not", "not_high_impact"):
        omb_status, omb_level = "not_high_impact", "low"
    else:  # not_yet_determined OR unanswered/unknown -> level is provisional
        omb_status, omb_level = "not_yet_determined", None

    # ---- Output 2: operational tier (R2/R12) ----
    sev = SEVERITY_ORDER.get(v["C11a"])  # None if unknown/unset
    high = []
    if v["C12"] == "yes_unresolved":
        high.append("redline_unresolved")
    if v["C10"] == "acts_without_approval" and (
            v["C11"] == "hard_to_reverse" or (sev is not None and sev >= SEVERITY_ORDER["serious"])):
        high.append("autonomous_hard_or_severe")
    if v["C8"] == "sensitive" and v["C10"] == "acts_without_approval":
        high.append("sensitive_plus_autonomous")

    moderate = []
    if v["C8"] in ("personal_pii", "sensitive"):
        moderate.append("personal_or_sensitive_data")
    if v["C10"] in ("acts_with_approval", "acts_without_approval"):
        moderate.append("acts_changes_state")
    if sev is not None and sev >= SEVERITY_ORDER["limited"] and v["C10"] != "informs":
        moderate.append("severity_limited_not_informs")
    if v["C12"] == "yes_with_compensating_controls":
        moderate.append("redline_mitigated")

    if high:
        op_tier, op_fired = "high", high
    elif moderate:
        op_tier, op_fired = "moderate", moderate
    else:
        op_tier, op_fired = "low", ["residual_low"]

    # Unknown-floor rule (R3/R6): unknown op input -> tier cannot be Low.
    floored = False
    if op_tier == "low" and unknown_op:
        op_tier, op_fired = "moderate", ["unknown_floor(" + ",".join(unknown_op) + ")"]
        floored = True

    # ---- Final level = higher of the two (R3; contract 2: never blocks) ----
    provisional = omb_level is None
    if provisional:
        # F2: the card completes — the operational tier stands, marked provisional
        # (it may rise to High once the OMB determination is made).
        final = op_tier
        fired = ["OMB_high_impact_pending"] + [f"op:{t}" for t in op_fired]
    else:
        final = op_tier if _LEVEL_RANK[op_tier] >= _LEVEL_RANK[omb_level] else omb_level
        fired = []
        if omb_status == "high_impact":
            fired.append("OMB_high_impact")
        fired += [f"op:{t}" for t in op_fired]

    # ---- to_resolve: welcoming recommendations, never prohibitions ----
    to_resolve = []
    if provisional:
        to_resolve.append({
            "code": "omb_determination_pending",
            "recommendation": "Complete the OMB high-impact determination before "
                              "production access — the level is provisional and "
                              "may rise to High once determined (record it in C7a)."})
    if v["C12"] == "yes_unresolved":
        to_resolve.append({
            "code": "redline_unresolved",
            "recommendation": "The card strongly recommends not entering production "
                              "until one leg of the trifecta is broken (e.g. human "
                              "approval on external actions) or named compensating "
                              "controls are in place — then re-answer C12 as "
                              "yes_with_compensating_controls."})
    for fid in unknown_op:
        to_resolve.append({
            "code": f"unknown_input:{fid}",
            "recommendation": f"Resolve {fid} — the tier cannot drop below Moderate "
                              "until it is answered."})

    # ---- Part 2 routing (F7: honesty costs ~7 questions, not 19) ----
    if final in ("moderate", "high"):
        part2_groups = _FLOORED_GROUPS if (floored and final == "moderate") \
            else _ALL_EXTENDED_GROUPS
    else:
        part2_groups = []

    # Diagnostics kept for grader parity with earlier versions.
    boundary = (final == "low")  # a clean Low means every check cleared
    fragile = (bool(unknown_op) or provisional) and final in ("low", "moderate")

    return {
        "case_id": fill.get("case_id"),
        "persona": fill.get("persona"),
        "impact_level": final,                    # always a tier string in contract 2
        "final_level": final,
        "level_provisional": provisional,          # F2: pending C7 -> provisional, not blocked
        "omb_high_impact_status": omb_status,      # high_impact / not_high_impact / not_yet_determined
        "operational_tier": op_tier,
        "fired_triggers": fired,
        "to_resolve": to_resolve,
        "part2_groups": part2_groups,
        "tier_floored_by_unknown": floored,
        "boundary": boundary,
        "unknown_inputs": unknown_all,
        "unknown_operational_inputs": unknown_op,
        "level_fragile": fragile,
        "inputs": v,
    }


def check_anchors(anchors_dir):
    """Re-derive every anchor-*.json and compare against its _expected block."""
    anchors = sorted(Path(anchors_dir).glob("anchor-*.json"))
    if not anchors:
        print(f"no anchor-*.json found in {anchors_dir}", file=sys.stderr)
        return 1
    failures = 0
    for path in anchors:
        fill = json.loads(path.read_text())
        expected = fill.get("_expected", {})
        verdict = derive(fill)
        mismatches = {k: (verdict[k], want) for k, want in expected.items()
                      if k in verdict and verdict[k] != want}
        if mismatches:
            failures += 1
            print(f"FAIL  {path.name}")
            for k, (got, want) in mismatches.items():
                print(f"      {k}: derived {got!r}, expected {want!r}")
        else:
            checked = [k for k in expected if k in verdict]
            print(f"ok    {path.name}  ({verdict['impact_level']}; checked {', '.join(checked)})")
    print(f"\n{len(anchors) - failures}/{len(anchors)} anchors match")
    return 1 if failures else 0


def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "--check":
        return check_anchors(args[1])
    if len(args) != 1:
        print("usage: derive_impact.py fill.json | derive_impact.py --check anchors_dir",
              file=sys.stderr)
        return 2
    fill = json.loads(Path(args[0]).read_text())
    if not isinstance(fill.get("fields"), dict):
        print(json.dumps({"error": "no fields dict in fill"}))
        return 2
    fill_contract = fill.get("derivation_contract_version")
    if fill_contract is not None and fill_contract != EXPECTED_CONTRACT_VERSION:
        # Never compute on a contract this engine doesn't understand.
        print(json.dumps({"error": "derivation_contract_mismatch",
                          "engine_contract": EXPECTED_CONTRACT_VERSION,
                          "fill_contract": fill_contract,
                          "action": "update scripts/derive_impact.py before deriving"}))
        return 3
    print(json.dumps(derive(fill), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
