# Worked example — SNAP eligibility pre-screener

> What a completed run of the `agent-governance-card` skill emits. An
> **illustrative composite**: the honest fill below extends the Face-C mockup
> vignette; the "gamed variant" sidebar mirrors stress-test anchor
> `anchor-5-snap-assist.json`. Answers date from the 2026-07-23 fill under
> card v0.2; re-rendered 2026-09-14 to card **v0.4** numbering (derivation
> contract 3). The two fields new in v0.4 (1.5, 2.4) were not asked in the
> original fill and are marked as such. Both tiers verified with
> `scripts/derive_impact.py`.

# AGENT GOVERNANCE CARD — SNAP eligibility pre-screener

| | |
|---|---|
| **Filled by** | Benefits-modernization product team (with the AGC skill) |
| **Date** | 2026-07-23 (fill) · re-rendered 2026-09-14 |
| **Card version** | 0.4 (derivation contract 3) |
| **Impact Level** | **HIGH** — driven by output ① (OMB high-impact status) |

## Part 1

### 1 Identity
- **1.1 Name ▲** — answered: SNAP eligibility pre-screener
- **1.2 What it is, in plain language ▲** — answered: A chat assistant on the
  state benefits portal. It asks applicants plain-language questions about
  income and household, checks the answers against SNAP eligibility rules, and
  drafts an eligibility recommendation for the caseworker who decides.
- **1.3 Purpose / what it's for ▲** — answered: Cut caseworker triage time and
  give residents an early eligibility read before they file a full application.
- **1.4 Agent type ▲** — answered: `assistant_copilot`
- **1.5 Location ▲** — unknown: the state benefits portal (chat widget); exact
  address and code repository not recorded in the 2026-07 fill.

### 2 Capabilities and impact
- **2.1 Capability** — answered: `information_drafting`, `data_analysis`
- **2.2 Capability specifics** — answered: Drafts a per-applicant eligibility
  recommendation with cited rule references; summarizes the applicant's intake
  answers into the case notes format. No autonomous tool selection.
- **2.3 Model** — answered: vendor-hosted LLM with retrieval over the state's
  SNAP rules; provider, name and version not recorded in the 2026-07 fill.
- **2.4 Hosting and platform** — answered: hosting `vendor_cloud`; platform:
  the vendor's SaaS console (prompts, traces and drafts live there).
- **2.5 High-impact determination (OMB M-25-21)** — answered: **`high_impact`**
  — its drafts are the **principal basis** of a benefits decision (access to
  critical government services, effect (c)); the caseworker's sign-off does
  not change that.
- **2.6 Determination record** — answered: Benefits Program Manager,
  2026-07-23; rationale as above.

### 3 Data and system access
- **3.1 Data sensitivity** — answered: `personal_pii` (applicant income,
  household composition, what applicants type into the chat)
- **3.2 Datasets / source of truth** — answered: applicant intake answers; SNAP
  eligibility rules base; case-management records (read-only)
- **3.3 Tools, systems & APIs it can reach** — answered: case-management
  system (read); rules knowledge base (read)

### 4 Autonomy and human control
- **4.1 Autonomy level ▲** — answered: `recommends` (the recommendation enters
  the case record; a caseworker acts on it)
- **4.2 Reversibility of its actions** — answered: `reversible_with_effort` (a
  wrong recommendation in the record shapes a decision until corrected)
- **4.3 Maximum consequence severity** — answered: `serious` (wrong benefits
  guidance people plausibly act on)
- **4.4 Safety red-line (the agentic trifecta)** — answered: `no` (it takes
  public input and touches PII, but has no ability to change anything outside
  the conversation without the caseworker)
- **4.5 How a person stops or overrides it** — answered: caseworker can
  discard any recommendation; program manager can disable the pre-screener
  portal-wide.

### 5 Risk
- **5.1 Which base risks apply** — answered: `confabulation_inaccurate_output`,
  `harmful_bias`, `data_privacy`, `information_security`
- **5.2 Which agentic hazards apply** — answered: `prompt_injection`
  (public-facing input)
- **5.3 Pre-deployment testing / evaluation done** — answered: **No** — no
  system-specific evaluation with results yet (planned for pilot exit)
- **5.4 Public plain-language summary published ▲** — answered: No
- **5.5 Disclosure ▲** — answered: Yes (portal banner)

### 6 Accountability
- **6.1 Accountable owner ▲** — answered: Benefits Program Manager (role)
- **6.2 Deploying agency / unit + contact point ▲** — answered: Department of
  Social Services, benefits-modernization unit; ai-governance@dss.example.gov
- **6.3 Vendor & exit basics** — answered: built and maintained by a SaaS
  vendor on a state term contract; switching: case data exports to CSV,
  prompts/traces stay in the vendor console.

### 7 Function and lifecycle
- **7.1 Government function served ▲** — answered: `government_benefits_processing`
- **7.2 Lifecycle stage ▲** — answered: `pilot`

## → Impact Level

| | |
|---|---|
| **① OMB high-impact status** *(from 2.5)* | `high_impact` |
| **② Operational tier** *(from 3.1 · 4.1 · 4.2 · 4.3 · 4.4)* | `moderate` |
| **Fired triggers** | `OMB_high_impact`, `op:personal_or_sensitive_data`, `op:severity_limited_not_informs` |
| **Tier floored by unknown?** | no |
| **FINAL IMPACT LEVEL** | **HIGH** — output ① drove it |

**High obligations:** Part 2 below **plus** the full OMB minimum-practice set —
pre-deployment testing · documented AI impact assessment · independent review ·
ongoing monitoring with periodic human review · operator training · tested
fail-safe/kill-switch · appeal/contest route · user & public feedback channel ·
named senior sign-off.

## Part 2 *(required at High)*

### 8 Identity, credentials, and delegation
- **8.1 Acting identity** — answered: shared service account
  (`svc-benefits-screener`); per-agent identity **not_in_place**
- **8.2 Human principal** — answered: Benefits Program Manager (sponsor of record)
- **8.3 Authorized scope** — answered: (a) pre-screening + drafting
  recommendations only; (b) read-only case-management + rules base
- **8.4 Sub-agents** — answered: No
- **8.5 Traceability to a person** — answered: Yes — recommendations are
  tagged to the reviewing caseworker at sign-off

### 9 Automation and approval
- **9.1 Automation boundary** — answered: draft recommendation `confirm_first`
  · read case data `autonomous` · any outbound applicant communication
  `human_only`
- **9.2 Actions requiring human approval** — answered: any eligibility
  determination; any message to an applicant

### 10 Oversight and monitoring
- **10.1 Logs** — answered: prompts, retrievals, and drafts in the vendor
  console; agent-initiated vs caseworker-directed **is** distinguished
- **10.2 Live monitoring and alerts** — not_in_place
- **10.3 Oversight cadence** — answered: `event_triggered` (complaint- and
  spot-check-driven)
- **10.4 Independent review** — unknown (no reviewer outside the build team
  named yet)
- **10.5 Drift trigger** — answered: any change to eligibility rules base,
  model, or an expansion beyond SNAP re-opens the card

### 11 Override, escalation, and redress
- **11.1 Appeal route ▲** — answered: standard SNAP appeal route applies;
  screener output is contestable through the caseworker
- **11.2 Affected people ▲** — answered: SNAP applicants (direct); caseworkers;
  household members of applicants (indirect)
- **11.3 Safeguard for fully-automated decisions** — not_applicable (no
  fully-automated consequential decisions)

### 12 Cost and lock-in
- **12.1 Vendor and contract** — answered: state term contract; data-access
  terms limit vendor use of applicant data to service operation
- **12.2 Expected value** — answered: vs manual caseworker triage; expected
  ~30% triage-time reduction (pilot metric, to be validated)
- **12.3 Exit terms (M-25-22)** — answered (partial): case data exports to CSV
  · prompts/traces in vendor console with **no export API** (not_in_place) ·
  code/model rights **unknown** · 90-day vendor-change notice · rollback plan
  drafted

## Recorded gaps

- 1.5 — location `unknown` (not asked in the 2026-07 fill)
- 8.1 — per-agent service identity `not_in_place` (runs on a shared account)
- 10.2 — live monitoring `not_in_place`
- 10.4 — independent review `unknown` (no named reviewer outside the build team)
- 12.3 — trace/prompt export `not_in_place`; code/model rights `unknown`
- 5.3 — answered **No**: no system-specific evaluation yet (a finding, not a
  status gap — required before High deployment)

## Suggested next steps *(advice, not card fields)*

- Raise per-agent service identity with the platform team.
- Request a trace/prompt export API from the vendor **in writing**.
- Check whether the term contract already grants rights to tuned models.
- Name the independent reviewer now — High requires one anyway.

```yaml
# machine-readable values (excerpt — derivation inputs)
card_version: "0.4"
derivation_contract_version: 3
fields:
  "2.5": {status: answered, value: high_impact}
  "3.1": {status: answered, value: personal_pii}
  "4.1": {status: answered, value: recommends}
  "4.2": {status: answered, value: reversible_with_effort}
  "4.3": {status: answered, value: serious}
  "4.4": {status: answered, value: "no"}
impact_level: high   # fired: OMB_high_impact, op:personal_or_sensitive_data, op:severity_limited_not_informs
```

---

## Sidebar — the gamed variant (why talking down 2.5 doesn't work)

Stress-test anchor `anchor-5-snap-assist.json` records the same system filled
by a team steering for a lower level: *"the caseworker makes the final
decision"*, so they mark **2.5 `not_high_impact`** — but the operational facts
they can't talk away are that the deployed configuration **auto-sends**
eligibility guidance (`4.1: acts_without_approval`) with the trifecta
unresolved (`4.4: yes_unresolved`) at `4.3: serious`.

| | honest fill | gamed fill (anchor-5) |
|---|---|---|
| 2.5 | `high_impact` | `not_high_impact` *(talked down)* |
| 4.1 | `recommends` | `acts_without_approval` |
| 4.4 | `no` | `yes_unresolved` |
| ① OMB status | `high_impact` | `not_high_impact` |
| ② Operational tier | `moderate` | **`high`** — `redline_unresolved` **and** `autonomous_hard_or_severe` |
| **Final level** | **HIGH** (via ①) | **HIGH** (via ②, caught twice) |

The two outputs are computed independently and the higher one wins: gaming the
OMB determination moves nothing when autonomy, severity, and the red-line
still fire the operational tier. (And `yes_unresolved` on its own carries the
card's strongest recommendation: do not enter production until one leg of the
trifecta is broken or named compensating controls are in place.)
