# The Agent Governance Card — the skill

A per-deployment governance record for agentic AI in government, as an AI
interview skill. A product team runs it before an agentic system gets
production access to state data, tools, or users. It asks plain-language
questions one at a time, helps with the hard ones, computes an **Impact Level**
deterministically from six of the answers, and emits the filled card, human-
and machine-readable.

The card is a voluntary instrument: it records, computes, and recommends. It
never blocks. Its recommendations become gates only where an adopting
authority, such as a state CIO or an agency directive, makes a completed card
a precondition for production access.

**Card v0.4 · derivation contract 3.** Twelve dimensions, 47 fields: 29 in
Part 1 for every in-scope agent, 18 in Part 2 at Moderate and High. Fourteen
fields plus the Impact Level form the public layer. The full document — every
question, its allowed values, and the rationale behind each field — is
published by the Center for Civic Futures; this repository holds only what an
assistant needs to run the interview.

## Install

```bash
npx skills add The-Agentic-State/agent-governance-card
```

Works across Claude Code, Codex, Cursor, Copilot, Gemini and other agents that
follow the open Agent Skills layout. Add `-g` to install globally. Then ask:
*"help me fill in the Agent Governance Card for our new intake agent."*

**Requirements.** Python 3 for the derivation engine. Without it the skill
still runs, derives the level from the schema's written rules, says so, and
recommends verifying by engine before the card is filed.

## Microsoft 365 Copilot

Agent Builder cannot install a skill. Use
[`skills/agent-governance-card/agent-builder/`](skills/agent-governance-card/agent-builder/)
instead: paste `instructions.txt` as the agent's instructions and add the two
`.txt` files as knowledge. The README there has the ten-minute set-up and the
note for Government Community Cloud tenants.

## What's in this repository

| Path | What it is |
|---|---|
| [`skills/agent-governance-card/SKILL.md`](skills/agent-governance-card/SKILL.md) | The interview procedure. Holds no field content — it reads the schema. |
| [`skills/agent-governance-card/references/schema.snapshot.yaml`](skills/agent-governance-card/references/schema.snapshot.yaml) | The card: every field, value, gloss and derivation rule, with `card_version` and `derivation_contract_version` in its header. |
| [`skills/agent-governance-card/scripts/derive_impact.py`](skills/agent-governance-card/scripts/derive_impact.py) | The deterministic Impact Level engine, with its regression cases under `scripts/anchors/`. |
| [`skills/agent-governance-card/templates/`](skills/agent-governance-card/templates/) | The blank card (fill it by hand if you prefer) and the addendum for platform deployments. |
| [`skills/agent-governance-card/examples/`](skills/agent-governance-card/examples/) | Two worked cards: a High-tier composite and a real deployment filled from public sources. |
| [`skills/agent-governance-card/agent-builder/`](skills/agent-governance-card/agent-builder/) | The Microsoft 365 Copilot Agent Builder variant. |

## Credits & license

Developed by [The Agentic State](https://agenticstate.org) with the **Center
for Civic Futures (CCF)**. Copyright © 2026 The Agentic State. Released under
[**CC BY 4.0**](LICENSE): use it, adapt it for your state, publish what you
fill in, with credit:

> Agent Governance Card, developed by The Agentic State with the Center for Civic Futures, licensed CC BY 4.0. https://github.com/The-Agentic-State/agent-governance-card

If you adapt the card for your own jurisdiction, keep `card_version` and
`derivation_contract_version` in your fills, so a card can still be read
against the rules that produced it.
