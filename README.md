# Agent Governance Card — Skill

State governments are moving past chatbots into agentic AI: software that
acts. Agents can use tools, touch data, receive and send files, and complete
multi-step tasks with autonomy.

The IT governance machinery states rely on today, including intake, security
review, procurement, and audit, wasn't built for software that acts. Agents
in government bring governance challenges, and a first step to address them
is visibility on what agents do in public organisations. What is an agent
allowed to do? What did it touch? Who answers for it? How does a person step
in? And what does it cost to leave?

The Agent Governance Card exists to assess and record this information,
bringing structured, comparable transparency to agentic deployments that
interact directly with the public or materially influence a decision
affecting the public or state resources.

**Who uses it.** Most often a product team: the people who build or configure
the agent and know what it actually does. A CIO's office, a procurement
officer, or an auditor may also fill one in for a deployment. When a vendor is
engaged, the accountable public agency fills it.

**When.** Most often before an agentic system gets production access to state
data, tools, or users. The card also works earlier, during development, as a
running checklist of the governance questions a team will eventually have to
answer. And later, for systems already live whose details were never
recorded, or were recorded without structure. Once filled, a card is meant to
be revisited on a rolling basis, so the record keeps pace with the deployment.

**What it delivers.** A snapshot of one deployment: the agent's capabilities,
the data it uses, who answers for it, how a person can step in, and more.
From the team's own answers the card also computes an **Impact Level**,
deterministically from six of them, which routes the deployment to
proportionate obligations. The card records, computes, and recommends. It
never blocks. Its recommendations become gates only where an adopting
authority, such as a state CIO or an agency directive, makes a completed card
a precondition for production access.

**Card v0.4 · derivation contract 3.** The schema has twelve dimensions,
spanning what an agent does and touches, who answers for it, its risks, and
more. Across them, 47 fields: 29 in Part 1 for every in-scope agent, 18 in
Part 2 at Moderate and High. For each field the schema holds the
plain-language question a team answers, the values the answer can take, and
the rationale behind the field. The full document is published by the Center
for Civic Futures; this repository holds what an assistant needs to run the
interview.

## Two ways to fill it

Work through the schema by hand, starting from the blank card in
[`templates/`](skills/agent-governance-card/templates/), or install this
skill and let an assistant act as the interviewer. The skill asks the
questions one at a time, helps with the hard ones, computes the Impact Level,
and emits the filled card, human- and machine-readable.

## Install

```bash
npx skills add The-Agentic-State/agent-governance-card
```

Works in any assistant that supports the open Agent Skills layout: Claude
Code, Codex, Cursor, GitHub Copilot, Gemini and others. Add `-g` to install
globally. Then ask: *"help me fill in the Agent Governance Card for our new
intake agent."*

**Requirements.** Python 3 for the derivation engine. Without it the skill
still runs, derives the level from the schema's written rules, says so, and
recommends verifying by engine before the card is filed.

## Microsoft 365 Copilot

Agent Builder cannot install a skill. Use
[`skills/agent-governance-card/agent-builder/`](skills/agent-governance-card/agent-builder/)
instead: paste `instructions.txt` as the agent's instructions and add the two
`.txt` files as knowledge. The README there has the ten-minute set-up and the
note for Government Community Cloud tenants.

## Publishing the card

Once a card is filled, our invitation to states is to make it visible. At
minimum it belongs in an internal register. We recommend publishing it openly
for citizens to see, in particular the **public layer**: the fourteen fields,
plus the Impact Level, that the schema sets aside for publication, marked ▲
in the schema and the template. The card was built as the unit of a public
register of agent deployments in government.

A submission route to the Center for Civic Futures is in preparation. When
it opens, a run of the skill will end with a link to a form with the public
fields already filled in. Nothing is submitted until you review them and
choose to send. CCF assembles submissions into a public register of
government agents, so publishing a card also builds the comparative picture
states currently lack.

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
