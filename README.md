# The Agent Governance Card

State governments are moving past chatbots into **agentic AI — software that takes actions**: it uses tools, touches data, sends things, files things, completes multi-step tasks with real autonomy. The governance machinery states rely on today — intake, security review, procurement, audit — was not built for software that acts.

What's missing is not another framework. It's a simple, per-deployment record of the questions every state has to be able to answer before an agent goes live: **what is it allowed to do, what does it touch, who answers for it when it acts, how does a person step in — and what does it cost to leave.**

The Agent Governance Card is that record. A product team completes it *before* an agentic system gets production access to state data, tools, or users. It is a snapshot of what is true at go-live, not a list of promises. `unknown` and `not_in_place` are **formal answers**, because a missing mechanism recorded plainly is a governance finding, not a failure. From the team's own answers the card computes an **Impact Level** that routes proportionate obligations.

**It is a voluntary instrument.** The card records, computes, and recommends — it never blocks. Its recommendations become gates only where an adopting authority (a state CIO or agency directive) makes a completed card a precondition for production access.

## Two instruments

### 1 · The schema (the record)

One canonical, machine-readable file is the source of truth: [`schema/agent-governance-card.schema.yaml`](schema/agent-governance-card.schema.yaml). It holds the explicit metadata a state needs to know about every agent, across **12 dimensions** — what it does, what it touches, autonomy and human control, who answers for it, oversight, redress, the cost of getting out.

Each dimension is a set of fields, **45 in total: 27 Core**, for every in-scope agent, **and 18 Extended**, required at Moderate and High. The file also carries the **derivation rules** that compute the Impact Level from six of those answers.

Everything else is rendered from this one file — the skill below, and any form, report or register built on top of it.

### 2 · The skill (the way in)

The schema is the record. The skill exists so that a team never has to face it as a form: it asks the questions instead, in the order that makes sense, and helps you answer the hard ones.

[`skills/agent-governance-card/`](skills/agent-governance-card/) is an **AI interview that walks you through the schema**: plain-language questions one at a time, advice on what each option would mean in your context, honest handling of what you don't know yet — then it computes your Impact Level and emits the filled card, human-readable and machine-readable.

| Mode | What you get | Time |
|---|---|---|
| **Quick scan** | 7 questions — a provisional Impact Level and a to-do list. Explicitly *not* a fileable card. | 3–5 min |
| **Full card** | All of Core, plus Extended when your level routes there. The fileable record. | 15–20 min conversational; up to ~40 if you look things up |

You choose at the start, and the mode is stamped into the output so a quick scan can never masquerade as a filed card. A quick scan can be upgraded to a full card without re-answering anything.

The Impact Level is never computed by the model. It is computed by [`scripts/derive_impact.py`](skills/agent-governance-card/scripts/derive_impact.py), a deterministic engine pinned to the schema's derivation contract, so the same answers always produce the same tier.

Built on OMB M-25-21 and M-25-22, the UK's Algorithmic Transparency Recording Standard, NIST's AI RMF, and the emerging agentic-standards work — then stress-tested against 20 real deployments before asking anyone to trust it.

Nine of the 45 fields take **controlled answers** — a fixed set of values rather than free text — so that cards filled by different teams, in different states, can be read side by side. That is deliberate: a filled card is also the kernel of a **public agent register**. If you fill one in, we'd like to hear about it — publish it, or open an issue here and tell us what the card got wrong.

## Install

```bash
npx skills add The-Agentic-State/agent-governance-card
```

That works across 70+ coding agents — Claude Code, Codex, Cursor, OpenCode, Copilot, Gemini and others — installing into whichever locations your agents use. Add `-g` to install globally rather than into the current project.

Then just ask: *"help me fill in the Agent Governance Card for our new intake agent."*

**Requirements.** Python 3 for the derivation engine. Without it the skill still runs and derives the tier from the schema's prose rules, but it says so and recommends verifying by engine before the card is filed.

## What's in this repo

| Path | What it is |
|---|---|
| [`schema/agent-governance-card.schema.yaml`](schema/agent-governance-card.schema.yaml) | **The canonical card.** The single source of truth for every field, enum, gloss and derivation rule — plus `card_version` and `derivation_contract_version` in its header. |
| [`skills/agent-governance-card/SKILL.md`](skills/agent-governance-card/SKILL.md) | The interview procedure. Holds no field content — it reads the schema at run time. |
| [`skills/agent-governance-card/scripts/derive_impact.py`](skills/agent-governance-card/scripts/derive_impact.py) | The deterministic Impact Level engine, plus its regression cases under `scripts/anchors/`. |
| [`skills/agent-governance-card/templates/`](skills/agent-governance-card/templates/) | Blank card (also the no-AI fallback — fill it by hand) and the addendum for platform deployments. |
| [`skills/agent-governance-card/examples/`](skills/agent-governance-card/examples/) | Two worked cards: a High-tier composite, and a real deployment filled from public sources. |
| [`skills/agent-governance-card/references/`](skills/agent-governance-card/references/) | How the skill resolves the schema, and the schema copy it ships with. |

## Credits & license

Developed by [The Agentic State](https://agenticstate.org) with the **Center for Civic Futures (CCF)**.

Copyright © 2026 The Agentic State. Released under [**CC BY 4.0**](LICENSE) — use it, adapt it for your state, publish what you fill in. Share and adapt freely, including commercially, with credit:

> Agent Governance Card, developed by The Agentic State with the Center for Civic Futures, licensed CC BY 4.0. https://github.com/The-Agentic-State/agent-governance-card

If you adapt the card for your own jurisdiction, please keep `card_version` and `derivation_contract_version` in your fills, so a card can still be read against the rules that produced it.
