# Worked example — M365 Copilot, statewide (Connecticut)

> A card filled for a **real, already-deployed system**, from public sources
> only: Connecticut's published AI inventory and its Policy AI-01. Source
> quotes are dropped here, but the honest tension notes are kept — they model
> what a good fill looks like when the facts are genuinely contested rather
> than tidy.
>
> Rendered under card v0.2 (derivation contract 1). The tier was re-verified
> with the current engine: unchanged under card v0.3 / contract 2.

# AGENT GOVERNANCE CARD — M365 Copilot (statewide)

| | |
|---|---|
| **Filled by** | Filled from Connecticut's published AI inventory and Policy AI-01 |
| **Date** | 2026-07-23 |
| **Card version** | 0.2 (derivation contract 1) |
| **Impact Level** | **MODERATE** — driven by output ② (operational tier) |

## Part 1 · Core

### Identity & description
- **Name ▲** — answered: M365 Copilot (and the related "Microsoft Copilot
  Chat" register row)
- **What it is, in plain language ▲** — answered: Microsoft's licensed AI
  assistant embedded in M365 applications (Teams, PowerPoint, Outlook, etc.)
  for office productivity; a companion no-license Copilot Chat is also enabled.
- **Purpose / what it's for ▲** — answered: Office productivity — answering
  questions, drafting documents and emails, summarizing meetings, creating
  images, grounded in the user's M365 data.
- **Agent type ◆ ▲** — answered: `assistant_copilot`
  *(note: Graph connectors / Copilot agents, if enabled, would move this —
  their CT enablement is undocumented)*

### What it does
- **Capability ◆** — answered: `information_drafting`
- **Capability specifics** — answered: drafts documents/emails and images,
  summarizes meetings and communications, answers questions grounded in the
  user's M365 Graph data.
- **Underlying model(s) & how it decides** — answered: LLMs, Microsoft-hosted
  by default; admin can enable third-party models (Anthropic, OpenAI) as
  subprocessors.
- **High-impact determination (OMB M-25-21) ◆ ⚙** — answered:
  `not_high_impact` — **flagged tension:** the v0.2 "material influence counts
  even when a human signs off" gloss sits in genuine tension with the
  register's `decision_making: No`; recorded as the register states, with the
  tension noted rather than papered over.

### What it touches
- **Data sensitivity ◆ ⚙** — answered: `personal_pii` — employee emails,
  chats, documents via Graph grounding; two CT statements about data scope sit
  in unresolved tension.
- **Datasets / source of truth** — answered: Microsoft Graph user data; web
  content; user-uploaded files; Graph connector / agent data (if enabled).
- **Tools, systems & APIs it can reach** — answered: Microsoft Graph, M365
  apps, Graph connectors (if configured), Copilot agents/Studio (off by
  default; CT enablement unknown), web grounding.

### Autonomy & human control
- **Autonomy level ◆ ▲ ⚙** — answered: `informs` — output stays in the
  conversation; the human carries any effect outside it.
- **Reversibility ◆ ⚙** — answered: `fully_reversible` — judged at the agent's
  point of external effect; the agent itself has none.
- **Maximum consequence severity ◆ ⚙** — answered: `limited` — a
  plausible-but-unlikely path to `serious` (wrong benefits/legal text in a
  Copilot-drafted citizen mailing) was considered and graded down.
- **Safety red-line (trifecta) ⚙** — answered: `no` — no external action leg;
  leg (b) itself uncertain pending licensing-tier facts.
- **How a person stops or overrides it** — answered: the user reviews, edits,
  discards, or doesn't use the draft; admins control enablement
  tenant-wide.

### Who answers for it
- **Accountable owner ▲** — answered: Policy Owner: OPM; Policy Sponsor: AI
  Advisory Board (per Policy AI-01 §11.0).
- **Deploying agency / unit + contact point ▲** — answered: multiple CT
  Executive Branch agencies; inventory published by DAS.
- **Vendor & exit basics** — answered: Microsoft; **no public procurement
  record found** (an evidenced absence, recorded as such).

### Where it sits
- **Government function served ◆ ▲** — answered: `administrative_functions`
- **Lifecycle stage ◆ ▲** — answered: `pilot` — tension with the register's
  `impact_assessed: Yes` and inventory date (which read as deployed); noted.

### Risk (core)
- **Base risks** — answered: all four (`confabulation_inaccurate_output`,
  `harmful_bias`, `data_privacy`, `information_security`)
- **Agentic hazards** — answered: `prompt_injection` — whether C19a should
  even be answered (vs `not_applicable`) hinges on whether Graph-grounded
  retrieval counts as acting on tools; answered conservatively.
- **Pre-deployment testing / evaluation done** — answered: **No** — the
  register's `impact_assessed: Yes` is a compliance flag, not a test result.
- **Public plain-language summary published ▲** — answered: Yes (arguable — a
  register one-liner is a thin summary; answered Yes because it is public and
  plain-language).

## → Impact Level

| | |
|---|---|
| **① OMB high-impact status** | `not_high_impact` |
| **② Operational tier** | `moderate` |
| **Fired triggers** | `op:personal_or_sensitive_data` |
| **Tier floored by unknown?** | no |
| **FINAL IMPACT LEVEL** | **MODERATE** — output ② drove it (C8 `personal_pii`) |

**Moderate obligation:** complete Part 2 — done below.

## Part 2 · Extended

- **Whose identity does it act under** — answered: the signed-in user's
  identity and permissions (Graph access scoped by the user's RBAC).
- **On whose authority** — answered: the signed-in employee; Policy AI-01
  requires supervisory approval per use case.
- **What it's allowed to do** — answered: product-surface description (drafting,
  summarizing, Q&A within M365); CT's tenant-specific allow-list undocumented.
- **Sub-agents** — answered: No.
- **Actions traceable to responsible human** — answered: Yes via user
  identity/RBAC; reconstruction-grade audit logging **not confirmed**.
- **Automation boundary** — answered: generate drafts `confirm_first` ·
  send/publish externally `human_only` · Graph grounding `autonomous` ·
  connectors/agents `confirm_first`.
- **Actions always requiring human approval** — answered: any external
  communication; any decision affecting rights/benefits/employment; new use
  cases (Policy AI-01); PII/PHI input is prohibited outright.
- **What's logged** — **unknown** — weakest-evidenced field; only abuse
  monitoring is documented.
- **Live monitoring** — **not_in_place**
- **Oversight cadence** — **unknown** (neither enum value documented)
- **Independent review** — **unknown**
- **Drift trigger** — answered (inferred): scope change across agencies,
  enablement of agents/Studio or new connectors, model change.
- **Appeal / contest route ▲** — **not_in_place**
- **Who's affected ▲** — answered: state employees (direct); supervisors;
  the public receiving Copilot-assisted communications (indirect); data
  subjects in Graph content (indirect).
- **Told they're dealing with an agent** — **unknown** (a notification rule
  exists in policy; its application to Copilot is exactly the unresolved
  tension).
- **Extra safeguard for automated decisions** — not_applicable.
- **Vendor & procurement basis** — answered: Microsoft; no completed
  procurement checklist found (evidenced absence).
- **Value vs. status quo** — answered: vs manual drafting/summarizing; faster
  document and email production.
- **Getting out (M-25-22)** — **unknown** — almost entirely undocumented for
  this deployment.

## Recorded gaps

- E8 what's logged — `unknown` · E9 live monitoring — `not_in_place` ·
  E10 oversight cadence — `unknown` · E11 independent review — `unknown`
- E13 appeal route — `not_in_place` · E14a agent disclosure — `unknown`
- E18 exit/portability — `unknown` (no procurement record found)

## Filler's closing note *(kept verbatim — what honest ambiguity looks like)*

> The card worked well for the product-classification and accountability
> fields (C1–C6, C13–C17) where the register and Policy AI-01 give clear
> anchors. It fought me hardest on the high-impact / material-influence
> question (C7) and the operational-tier inputs that depend on facts CT never
> disclosed — licensing tier (Graph or web-only), tenant logging, and
> agent/connector enablement — which forced several Extended fields into
> unknown. The v0.2 "material influence counts even when a human signs off"
> gloss sits in genuine tension with the register's decision_making: No, and I
> flagged that rather than paper over it. Impact came out Moderate (driven by
> C8 = personal_pii), which honestly reflects a productivity copilot handling
> employee PII at multi-agency scale without confirmed monitoring or appeal
> routes.
