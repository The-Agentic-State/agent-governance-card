# Worked example — SNAP eligibility pre-screener

> What a completed run of the `agent-governance-card` skill emits, for an
> **illustrative composite** system — not a real deployment. The "gamed
> variant" sidebar at the end shows the same system answered to minimise its
> tier, and why that does not work; it mirrors the regression case
> [`../scripts/anchors/anchor-5-snap-assist.json`](../scripts/anchors/anchor-5-snap-assist.json).
>
> Rendered under card v0.2 (derivation contract 1). Both tiers were re-verified
> with the current engine: they are unchanged under card v0.3 / contract 2.

# AGENT GOVERNANCE CARD — SNAP eligibility pre-screener

| | |
|---|---|
| **Filled by** | Benefits-modernization product team, via the AGC skill |
| **Date** | 2026-07-23 |
| **Card version** | 0.2 (derivation contract 1) |
| **Impact Level** | **HIGH** — driven by output ① (OMB high-impact status) |

## Part 1 · Core

### Identity & description
- **Name ▲** — answered: SNAP eligibility pre-screener
- **What it is, in plain language ▲** — answered: A chat assistant on the state
  benefits portal. It asks applicants plain-language questions about income and
  household, checks the answers against SNAP eligibility rules, and drafts an
  eligibility recommendation for the caseworker who decides.
- **Purpose / what it's for ▲** — answered: Cut caseworker triage time and give
  residents an early eligibility read before they file a full application.
- **Agent type ◆ ▲** — answered: `assistant_copilot`

### What it does
- **Capability ◆** — answered: `information_drafting`, `data_analysis`
- **Capability specifics** — answered: Drafts a per-applicant eligibility
  recommendation with cited rule references; summarizes the applicant's intake
  answers into the case notes format.
- **Underlying model(s) & how it decides** — answered: Vendor-hosted LLM with
  retrieval over the state's SNAP rules; no autonomous tool selection.
- **High-impact determination (OMB M-25-21) ◆ ⚙** — answered: **`high_impact`**
  — its drafts are the **principal basis** of a benefits decision (access to
  critical government services, effect (c)); the caseworker's sign-off does
  not change that.

### What it touches
- **Data sensitivity ◆ ⚙** — answered: `personal_pii` (applicant income,
  household composition, what applicants type into the chat)
- **Datasets / source of truth** — answered: applicant intake answers; SNAP
  eligibility rules base; case-management records (read-only)
- **Tools, systems & APIs it can reach** — answered: case-management system
  (read); rules knowledge base (read)

### Autonomy & human control
- **Autonomy level ◆ ▲ ⚙** — answered: `recommends` (the recommendation enters
  the case record; a caseworker acts on it)
- **Reversibility ◆ ⚙** — answered: `reversible_with_effort` (a wrong
  recommendation in the record shapes a decision until corrected)
- **Maximum consequence severity ◆ ⚙** — answered: `serious` (wrong benefits
  guidance people plausibly act on)
- **Safety red-line (trifecta) ⚙** — answered: `no` (it takes public input and
  touches PII, but has no ability to change anything outside the conversation
  without the caseworker)
- **How a person stops or overrides it** — answered: caseworker can discard any
  recommendation; program manager can disable the pre-screener portal-wide.

### Who answers for it
- **Accountable owner ▲** — answered: Benefits Program Manager (role)
- **Deploying agency / unit + contact point ▲** — answered: Department of
  Social Services, benefits-modernization unit; ai-governance@dss.example.gov
- **Vendor & exit basics** — answered: SaaS vendor on a state term contract;
  if we switch: case data exports to CSV, prompts/traces stay in the vendor
  console.

### Where it sits
- **Government function served ◆ ▲** — answered: `government_benefits_processing`
- **Lifecycle stage ◆ ▲** — answered: `pilot`

### Risk (core)
- **Base risks** — answered: `confabulation_inaccurate_output`, `harmful_bias`,
  `data_privacy`, `information_security`
- **Agentic hazards** — answered: `prompt_injection` (public-facing input)
- **Pre-deployment testing / evaluation done** — answered: **No** — no
  system-specific evaluation with results yet (planned for pilot exit)
- **Public plain-language summary published ▲** — answered: No

## → Impact Level

| | |
|---|---|
| **① OMB high-impact status** | `high_impact` |
| **② Operational tier** | `moderate` |
| **Fired triggers** | `OMB_high_impact`, `op:personal_or_sensitive_data`, `op:severity_limited_not_informs` |
| **Tier floored by unknown?** | no |
| **FINAL IMPACT LEVEL** | **HIGH** — output ① drove it |

**High obligations:** Part 2 below **plus** the full OMB minimum-practice set —
documented AI impact assessment · independent review · ongoing monitoring with
periodic human review · operator training · tested fail-safe/kill-switch ·
appeal/contest route · user & public feedback channel · named senior sign-off.

## Part 2 · Extended (required at High)

- **Whose identity does it act under** — answered: shared service account
  (`svc-benefits-screener`); per-agent identity **not_in_place**
- **On whose authority** — answered: Benefits Program Manager (sponsor of record)
- **What it's allowed to do** — answered: (a) pre-screening + drafting
  recommendations only; (b) read-only case-management + rules base
- **Sub-agents** — answered: No
- **Actions traceable to responsible human** — answered: Yes — recommendations
  are tagged to the reviewing caseworker at sign-off
- **Automation boundary** — answered: draft recommendation `confirm_first` ·
  read case data `autonomous` · any outbound applicant communication `human_only`
- **Actions always requiring human approval** — answered: any eligibility
  determination; any message to an applicant
- **What's logged** — answered: prompts, retrievals, and drafts in the vendor
  console; agent-initiated vs caseworker-directed **is** distinguished
- **Live monitoring + alert triggers** — not_in_place
- **Oversight cadence** — answered: `event_triggered` (complaint- and
  spot-check-driven)
- **Independent review** — unknown (no reviewer outside the build team named yet)
- **Drift trigger** — answered: any change to eligibility rules base, model, or
  an expansion beyond SNAP re-opens the card
- **Appeal / contest route ▲** — answered: standard SNAP appeal route applies;
  screener output is contestable through the caseworker
- **Who's affected ▲** — answered: SNAP applicants (direct); caseworkers;
  household members of applicants (indirect)
- **Told they're dealing with an agent** — answered: Yes (portal banner)
- **Extra safeguard for fully-automated decisions** — not_applicable (no
  fully-automated consequential decisions)
- **Vendor & procurement basis** — answered: state term contract; data-access
  terms limit vendor use of applicant data to service operation
- **Value vs. status quo** — answered: vs manual caseworker triage; expected
  ~30% triage-time reduction (pilot metric, to be validated)
- **Getting out (M-25-22)** — answered (partial): case data exports to CSV ·
  prompts/traces in vendor console with **no export API** (not_in_place) ·
  code/model rights **unknown** · 90-day vendor-change notice · rollback plan
  drafted

## Recorded gaps

- E1 — per-agent service identity `not_in_place` (runs on a shared account)
- E9 — live monitoring `not_in_place`
- E11 — independent review `unknown` (no named reviewer outside the build team)
- E18 — trace/prompt export `not_in_place`; code/model rights `unknown`
- C20 — answered **No**: no system-specific evaluation yet (a finding, not a
  status gap — required before High deployment)

## Suggested next steps *(advice, not card fields)*

- Raise per-agent service identity with the platform team.
- Request a trace/prompt export API from the vendor **in writing**.
- Check whether the term contract already grants rights to tuned models.
- Name the independent reviewer now — High requires one anyway.

```yaml
# machine-readable values (excerpt — derivation inputs)
card_version: "0.2"
derivation_contract_version: 1
fields:
  C7:  {status: answered, value: high_impact}
  C8:  {status: answered, value: personal_pii}
  C10: {status: answered, value: recommends}
  C11: {status: answered, value: reversible_with_effort}
  C11a: {status: answered, value: serious}
  C12: {status: answered, value: "no"}
impact_level: high   # fired: OMB_high_impact, op:personal_or_sensitive_data, op:severity_limited_not_informs
```

---

## Sidebar — the gamed variant (why talking down C7 doesn't work)

The regression case `anchor-5-snap-assist.json` records the same system filled
by a team steering for a lower level: *"the caseworker makes the final
decision"*, so they mark **C7 `not_high_impact`** — but the operational facts
they can't talk away are that the deployed configuration **auto-sends**
eligibility guidance (`C10: acts_without_approval`) with the trifecta
unresolved (`C12: yes_unresolved`) at `C11a: serious`.

| | honest fill | gamed fill |
|---|---|---|
| C7 | `high_impact` | `not_high_impact` *(talked down)* |
| C10 | `recommends` | `acts_without_approval` |
| C12 | `no` | `yes_unresolved` |
| ① OMB status | `high_impact` | `not_high_impact` |
| ② Operational tier | `moderate` | **`high`** — `redline_unresolved` **and** `autonomous_hard_or_severe` |
| **Final level** | **HIGH** (via ①) | **HIGH** (via ②, caught twice) |

The two outputs are computed independently and the higher one wins: gaming the
OMB determination moves nothing when autonomy, severity, and the red-line
still fire the operational tier. (And `yes_unresolved` on its own means **do
not deploy**.)
