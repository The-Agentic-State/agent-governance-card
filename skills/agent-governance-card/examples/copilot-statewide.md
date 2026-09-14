# Worked example — M365 Copilot, statewide (Connecticut)

> A **real** completed fill, rendered in the card format: stress-test fill
> `2_working-notes/260714_stress-test/fills_v0_2/copilot-statewide__P1.json`
> (diligent persona, evidence-based, card v0.2, 2026-07-14). Re-rendered
> 2026-09-14 to card **v0.4** numbering (derivation contract 3); the two fields
> new in v0.4 (1.5, 2.4) are answered from facts already in the fill. Evidence
> quotes are dropped here; the honest tension notes are kept — they model what
> a good fill looks like when the facts are genuinely contested. Tier verified
> with `scripts/derive_impact.py`.

# AGENT GOVERNANCE CARD — M365 Copilot (statewide)

| | |
|---|---|
| **Filled by** | P1 persona, from CT's AI inventory + Policy AI-01 (stress test) |
| **Date** | 2026-07-14 (fill) · rendered 2026-07-23 · re-rendered 2026-09-14 |
| **Card version** | 0.4 (derivation contract 3) |
| **Impact Level** | **MODERATE** — driven by output ② (operational tier) |

## Part 1

### 1 Identity
- **1.1 Name ▲** — answered: M365 Copilot (and the related "Microsoft Copilot
  Chat" register row)
- **1.2 What it is, in plain language ▲** — answered: Microsoft's licensed AI
  assistant embedded in M365 applications (Teams, PowerPoint, Outlook, etc.)
  for office productivity; a companion no-license Copilot Chat is also enabled.
- **1.3 Purpose / what it's for ▲** — answered: Office productivity — answering
  questions, drafting documents and emails, summarizing meetings, creating
  images, grounded in the user's M365 data.
- **1.4 Agent type ▲** — answered: `assistant_copilot`
  *(note: Graph connectors / Copilot agents, if enabled, would move this —
  their CT enablement is undocumented)*
- **1.5 Location ▲** — answered: inside the M365 applications (Teams, Outlook,
  Word, PowerPoint) and the Copilot Chat surface for signed-in state
  employees; a licensed product, no state code repository.

### 2 Capabilities and impact
- **2.1 Capability** — answered: `information_drafting`
- **2.2 Capability specifics** — answered: drafts documents/emails and images,
  summarizes meetings and communications, answers questions grounded in the
  user's M365 Graph data.
- **2.3 Model** — answered: Microsoft-hosted LLMs; admin can enable third-party
  models (Anthropic, OpenAI) as subprocessors. Model names and versions are not
  disclosed to the tenant.
- **2.4 Hosting and platform** — answered: hosting `vendor_cloud` (Microsoft);
  platform: Microsoft 365 Copilot.
- **2.5 High-impact determination (OMB M-25-21)** — answered:
  `not_high_impact` — **flagged tension:** the "material influence counts even
  when a human signs off" gloss sits in genuine tension with the register's
  `decision_making: No`; recorded as the register states, with the tension
  noted rather than papered over.
- **2.6 Determination record** — unknown (no written determination found; the
  register row is the only record).

### 3 Data and system access
- **3.1 Data sensitivity** — answered: `personal_pii` — employee emails,
  chats, documents via Graph grounding; two CT statements about data scope sit
  in unresolved tension.
- **3.2 Datasets / source of truth** — answered: Microsoft Graph user data;
  web content; user-uploaded files; Graph connector / agent data (if enabled).
- **3.3 Tools, systems & APIs it can reach** — answered: Microsoft Graph, M365
  apps, Graph connectors (if configured), Copilot agents/Studio (off by
  default; CT enablement unknown), web grounding.

### 4 Autonomy and human control
- **4.1 Autonomy level ▲** — answered: `informs` — output stays in the
  conversation; the human carries any effect outside it.
- **4.2 Reversibility of its actions** — answered: `fully_reversible` — judged
  at the agent's point of external effect; the agent itself has none.
- **4.3 Maximum consequence severity** — answered: `limited` — a
  plausible-but-unlikely path to `serious` (wrong benefits/legal text in a
  Copilot-drafted citizen mailing) was considered and graded down.
- **4.4 Safety red-line (the agentic trifecta)** — answered: `no` — no
  external action leg; leg (b) itself uncertain pending licensing-tier facts.
- **4.5 How a person stops or overrides it** — answered: the user reviews,
  edits, discards, or doesn't use the draft; admins control enablement
  tenant-wide.

### 5 Risk
- **5.1 Which base risks apply** — answered: all four
  (`confabulation_inaccurate_output`, `harmful_bias`, `data_privacy`,
  `information_security`)
- **5.2 Which agentic hazards apply** — answered: `prompt_injection` — whether
  this field should even be answered (vs `not_applicable`) hinges on whether
  Graph-grounded retrieval counts as acting on tools; answered conservatively.
- **5.3 Pre-deployment testing / evaluation done** — answered: **No** — the
  register's `impact_assessed: Yes` is a compliance flag, not a test result.
- **5.4 Public plain-language summary published ▲** — answered: Yes (arguable
  — a register one-liner is a thin summary; answered Yes because it is public
  and plain-language).
- **5.5 Disclosure ▲** — **unknown** (a notification rule exists in policy; its
  application to Copilot is exactly the unresolved tension).

### 6 Accountability
- **6.1 Accountable owner ▲** — answered: Policy Owner: OPM; Policy Sponsor: AI
  Advisory Board (per Policy AI-01 §11.0).
- **6.2 Deploying agency / unit + contact point ▲** — answered: multiple CT
  Executive Branch agencies; inventory published by DAS.
- **6.3 Vendor & exit basics** — answered: Microsoft, licensed product
  (vendor = platform = model provider); **no public procurement record found**
  (an evidenced absence, recorded as such).

### 7 Function and lifecycle
- **7.1 Government function served ▲** — answered: `administrative_functions`
- **7.2 Lifecycle stage ▲** — answered: `pilot` — tension with the register's
  `impact_assessed: Yes` and inventory date (which read as deployed); noted.

## → Impact Level

| | |
|---|---|
| **① OMB high-impact status** *(from 2.5)* | `not_high_impact` |
| **② Operational tier** *(from 3.1 · 4.1 · 4.2 · 4.3 · 4.4)* | `moderate` |
| **Fired triggers** | `op:personal_or_sensitive_data` |
| **Tier floored by unknown?** | no |
| **FINAL IMPACT LEVEL** | **MODERATE** — output ② drove it (3.1 `personal_pii`) |

**Moderate obligation:** complete Part 2 — done below.

## Part 2

### 8 Identity, credentials, and delegation
- **8.1 Acting identity** — answered: the signed-in user's identity and
  permissions (Graph access scoped by the user's RBAC).
- **8.2 Human principal** — answered: the signed-in employee; Policy AI-01
  requires supervisory approval per use case.
- **8.3 Authorized scope** — answered: product-surface description (drafting,
  summarizing, Q&A within M365); CT's tenant-specific allow-list undocumented.
- **8.4 Sub-agents** — answered: No.
- **8.5 Traceability to a person** — answered: Yes via user identity/RBAC;
  reconstruction-grade audit logging **not confirmed**.

### 9 Automation and approval
- **9.1 Automation boundary** — answered: generate drafts `confirm_first` ·
  send/publish externally `human_only` · Graph grounding `autonomous` ·
  connectors/agents `confirm_first`.
- **9.2 Actions requiring human approval** — answered: any external
  communication; any decision affecting rights/benefits/employment; new use
  cases (Policy AI-01); PII/PHI input is prohibited outright.

### 10 Oversight and monitoring
- **10.1 Logs** — **unknown** — weakest-evidenced field; only abuse monitoring
  is documented.
- **10.2 Live monitoring and alerts** — **not_in_place**
- **10.3 Oversight cadence** — **unknown** (none of the three values documented)
- **10.4 Independent review** — **unknown**
- **10.5 Drift trigger** — answered (inferred): scope change across agencies,
  enablement of agents/Studio or new connectors, model change.

### 11 Override, escalation, and redress
- **11.1 Appeal route ▲** — **not_in_place**
- **11.2 Affected people ▲** — answered: state employees (direct); supervisors;
  the public receiving Copilot-assisted communications (indirect); data
  subjects in Graph content (indirect).
- **11.3 Safeguard for fully-automated decisions** — not_applicable.

### 12 Cost and lock-in
- **12.1 Vendor and contract** — answered: Microsoft; no completed procurement
  checklist found (evidenced absence).
- **12.2 Expected value** — answered: vs manual drafting/summarizing; faster
  document and email production.
- **12.3 Exit terms (M-25-22)** — **unknown** — almost entirely undocumented
  for this deployment.

## Recorded gaps

- 2.6 determination record — `unknown` · 5.5 disclosure — `unknown`
- 10.1 logs — `unknown` · 10.2 live monitoring — `not_in_place` ·
  10.3 oversight cadence — `unknown` · 10.4 independent review — `unknown`
- 11.1 appeal route — `not_in_place`
- 12.3 exit terms — `unknown` (no procurement record found)

## Filler's closing note *(kept verbatim from the v0.2 fill — what honest ambiguity looks like; v0.4 numbers in brackets)*

> The card worked well for the product-classification and accountability
> fields (C1–C6, C13–C17 [1.1–2.3, 4.5–7.1]) where the register and Policy
> AI-01 give clear anchors. It fought me hardest on the high-impact /
> material-influence question (C7 [2.5]) and the operational-tier inputs that
> depend on facts CT never disclosed — licensing tier (Graph or web-only),
> tenant logging, and agent/connector enablement — which forced several
> Extended fields into unknown. The v0.2 "material influence counts even when
> a human signs off" gloss sits in genuine tension with the register's
> decision_making: No, and I flagged that rather than paper over it. Impact
> came out Moderate (driven by C8 [3.1] = personal_pii), which honestly
> reflects a productivity copilot handling employee PII at multi-agency scale
> without confirmed monitoring or appeal routes.
