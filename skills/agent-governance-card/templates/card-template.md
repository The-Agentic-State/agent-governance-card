# AGENT GOVERNANCE CARD — ⟨agent name⟩

> Blank card, card **v0.3**. Rendered from the canonical schema
> (`schema/agent-governance-card.schema.yaml`, derivation contract 2) — the
> schema is authoritative if this template ever disagrees. Works standalone:
> fill it by hand, or let the `agent-governance-card` skill interview you.
> **The card never blocks:** whatever comes up, it completes — unresolved
> items land in **To resolve** as strong recommendations.

| | |
|---|---|
| **Filled by** | ⟨name / role⟩ |
| **Date** | ⟨YYYY-MM-DD⟩ |
| **Card version** | 0.3 (derivation contract 2) |
| **Impact Level** | ⟨computed below⟩ |

**How to answer.** Every field takes a status: `answered` (you have the fact) ·
`unknown` (the fact exists but you can't determine it) · `not_applicable` (the
question genuinely doesn't apply) · `not_in_place` (the mechanism does not
exist — a governance finding, and a legal answer). An `unknown` on any
derivation input (marked **⚙**) keeps the tier at Moderate or above; a
non-answered High-impact determination (C7) makes the level **provisional**
(it may rise to High once determined). The six ⚙ fields are never genuinely
`not_applicable`.
**◆** = comparability field (controlled values) · **▲** = appears in the
public record.

## Scope check *(before filling)*

- [ ] Interacts directly with the public, **or** materially influences a
      decision with effect on the public or state resources
- [ ] Does more than return static search results
- [ ] Not an embedded commodity feature or purely predictive back-office model

*(All three must hold, else no card is required — record the system in the AI
inventory instead.)*

**Unit of analysis:** one card = one agent deployment in one operational
context. Platform used by many units → one parent card (shared layer) + a
deployment addendum per context. **This card covers:** ⟨deployment/context⟩

---

## Part 1 · Core *(every agent)*

### Identity & description
- **Name ▲** — status: ____ · value: ____
- **What it is, in plain language ▲** *(2–3 sentences)* — status: ____ · value: ____
- **Purpose / what it's for ▲** — status: ____ · value: ____
- **Agent type ◆ ▲** — status: ____ · value: ____
  `assistant_copilot · autonomous_single · orchestrator_subagents · agent_as_a_service`

### What it does
- **Capability ◆** *(choose every one that applies)* — status: ____ · value: ____
  `information_drafting · official_communication · business_transaction · computer_use · code_execution · data_analysis · physical_actuation`
- **Capability specifics** — status: ____ · value: ____
- **Underlying model(s) & how it decides** — status: ____ · value: ____
- **High-impact determination (OMB M-25-21) ◆ ⚙** — status: ____ · value: ____
  `high_impact · presumed_high_but_determined_not · not_high_impact · not_yet_determined`
  *Principal basis for a decision with legal/material/significant effect on:
  (a) civil rights, liberties, privacy · (b) access to education, housing,
  insurance, credit, employment, and other programs · (c) access to critical
  government resources or services · (d) human health and safety · (e) critical
  infrastructure or public safety · (f) strategic assets. Human sign-off does
  not exempt. `not_yet_determined` → the level below is provisional.*
- **Determination record** *(who, in what role, on what date, on what
  rationale — REQUIRED when stepping down from a presumed-high purpose,
  M-25-21 §4(a))* — status: ____ · value: ____

### What it touches
- **Data sensitivity ◆ ⚙** *(most sensitive data touched in operation, incl. user input)* — status: ____ · value: ____
  `none_public · internal · personal_pii · sensitive`
- **Datasets / source of truth** — status: ____ · value: ____
- **Tools, systems & APIs it can reach** *(everything it can call or act on)* — status: ____ · value: ____

### Autonomy & human control
- **Autonomy level ◆ ▲ ⚙** *("acts" includes any effect outside the conversation)* — status: ____ · value: ____
  `informs · recommends · acts_with_approval · acts_without_approval`
- **Reversibility of its actions ◆ ⚙** *(judged at the point of external effect)* — status: ____ · value: ____
  `fully_reversible · reversible_with_effort · hard_to_reverse`
- **Maximum consequence severity ◆ ⚙** *(worst plausible consequence at operating scale)* — status: ____ · value: ____
  `negligible · limited · serious · severe`
- **Safety red-line (the agentic trifecta) ⚙** *(untrusted input + non-public data + external effect, no human in the loop)* — status: ____ · value: ____
  `"no" · yes_with_compensating_controls (name the controls) · yes_unresolved (High + strong recommendation not to enter production until resolved)`
  *(in YAML, quote `"no"` — bare `no` reads as boolean false)*
- **How a person stops or overrides it** — status: ____ · value: ____

### Who answers for it
- **Accountable owner (role, not person) ▲** — status: ____ · value: ____
- **Deploying agency / unit + contact point ▲** — status: ____ · value: ____
- **Vendor & exit basics** *(vendor or in-house; contract vehicle; what leaves with you if you switch)* — status: ____ · value: ____

### Where it sits
- **Government function served ◆ ▲** — status: ____ · value: ____
  `administrative_functions · cybersecurity · emergency_management · energy_and_environment · government_benefits_processing · health_and_medical · human_resources · information_technology · international_affairs · law_enforcement · procurement_and_financial_management · science · service_delivery · transportation · other`
- **Lifecycle stage ◆ ▲** — status: ____ · value: ____
  `pre_deployment · pilot · deployed · retired` *(on retirement the card is closed, not deleted)*

### Risk (core)
- **Which base risks apply** *(every AI system)* — status: ____ · value: ____
  suggested: `confabulation_inaccurate_output · harmful_bias · data_privacy · information_security`
- **Which agentic hazards apply** *(no-tool system: `not_applicable` is complete)* — status: ____ · value: ____
  suggested: `prompt_injection · unsafe_irreversible_actuation · over_privileged_tools · memory_poisoning · cascading_failure`
- **Pre-deployment testing / evaluation done** *(actual evaluation of THIS system, with results — a register flag is not testing)* — status: ____ · value: ____ + link: ____
- **Public plain-language summary published ▲** — status: ____ · value: ____ + link: ____
- **Disclosure — are people told they're dealing with an agent ▲** *(+ how; internal-only agents: `not_applicable` is complete)* — status: ____ · value: ____

---

## → Your Impact Level *(two outputs; take the higher)*

| | |
|---|---|
| **① OMB high-impact status** *(from C7)* | ⟨high_impact / not_high_impact / not_yet_determined⟩ |
| **② Operational tier** *(from C8 · C10 · C11 · C11a · C12)* | ⟨low / moderate / high⟩ |
| **Fired triggers** | ⟨from the engine's `fired_triggers`⟩ |
| **Tier floored by unknown?** | ⟨yes: which inputs / no⟩ |
| **Provisional?** | ⟨yes — determination pending, may rise to HIGH / no⟩ |
| **FINAL IMPACT LEVEL** | **⟨LOW / MODERATE / HIGH⟩** ⟨(provisional)⟩ |

- **Low** → Core card only. Public-facing agent: Low must be confirmed by a
  named reviewer outside the build team — **reviewer:** ⟨name/role⟩
- **Moderate** → Part 2 per the engine's `part2_groups`: all groups for a
  substantive Moderate; **automation & approval detail + oversight only** when
  Moderate purely by the unknown-floor.
- **High** → all of Part 2 **plus** the full OMB M-25-21 §4(b) minimum-practice
  set: pre-deployment testing · documented AI impact assessment · independent
  review · ongoing monitoring with periodic human review · operator training ·
  tested fail-safe/kill-switch · appeal/contest route · user & public feedback
  channel · named senior sign-off.

---

## Part 2 · Extended *(Moderate / High)*

### Identity, credentials & delegation
- **Whose identity does it act under** — status: ____ · value: ____
- **On whose authority — human principal/sponsor** — status: ____ · value: ____
- **What it's allowed to do** *((a) tasks/workflows; (b) tools/data/APIs)* — status: ____ · value: ____
- **Sub-agents** *(can it create agents; can they exceed it; is creation recorded)* — status: ____ · value: ____
- **Actions traceable to responsible human** *(+ how)* — status: ____ · value: ____

### Automation & approval detail
- **Automation boundary** *(per action type: `autonomous · confirm_first · human_only` — be specific)* — status: ____ · value: ____
- **Actions always requiring human approval** — status: ____ · value: ____

### Oversight & monitoring
- **What's logged** *(enough to reconstruct a decision; agent-initiated vs human-directed distinguished?)* — status: ____ · value: ____
- **Live monitoring + alert triggers** — status: ____ · value: ____
- **Oversight cadence** — status: ____ · value: ____ `event_triggered · continuous`
- **Independent review (who, not on build team)** — status: ____ · value: ____
- **What change forces the card to be re-done (drift trigger)** — status: ____ · value: ____

### Override, escalation & redress
- **Appeal / contest route ▲** — status: ____ · value: ____
- **Who's affected, incl. indirectly ▲** — status: ____ · value: ____
- **Extra safeguard for fully-automated consequential decisions** — status: ____ · value: ____
  *(disclosure moved to Core in v0.3 — see the Risk section)*

### Cost & lock-in
- **Vendor & procurement basis** *(supplier, procurement route, data-access terms)* — status: ____ · value: ____
- **Value vs. the status quo** — status: ____ · value: ____
- **Getting out (M-25-22)** *(walk the checklist: knowledge transfer · data AND
  model portability (prompts, traces, fine-tunes, vector stores) ·
  licensing/pricing transparency · rights to code and models produced under
  the contract · vendor-change notice · rollback and closeout plan)* — status: ____ · value: ____

---

## To resolve *(strong recommendations, not prohibitions — from the engine's `to_resolve`)*

- ⟨code⟩ — ⟨recommendation + concrete next step⟩

## Recorded gaps *(every `unknown` / `not_in_place` answer)*

- ⟨field⟩ — ⟨status⟩ — ⟨one line on what's missing⟩

## Suggested next steps *(advice, not card fields)*

- ⟨surfaced during the interview⟩
