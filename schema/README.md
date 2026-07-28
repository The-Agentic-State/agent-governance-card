# `schema/` — the canonical card

[`agent-governance-card.schema.yaml`](agent-governance-card.schema.yaml) is the
source of truth, and the only file here by design. Every other face of the card
— the interview skill, a web form, a published report — renders from it, and
nothing downstream should carry its own copy of a question, an enum value or a
rule.

It is hand-edited, and stamps its own version in the header (`card_version`,
`derivation_contract_version`, `updated`). YAML rather than JSON because the
card is prose-heavy — multi-line glosses and help text — and because the file
carries explanatory comments that a JSON copy could not.

If your tooling wants JSON, convert it at build time and treat the result as a
build artifact rather than a second source of truth:

```bash
python3 -c "import yaml,json,sys; json.dump(yaml.safe_load(open(sys.argv[1])), sys.stdout, indent=2)" \
  agent-governance-card.schema.yaml > schema.json
```

## How the file is laid out

- **Front matter** — `adoption` (voluntary instrument), `answer_statuses`,
  `scope_trigger` (when a card is required, and the M-25-22 §2(b) boundary test
  for what is out of scope), and `unit_of_analysis` (one card = one agent
  deployment in one operational context; platform deployments use a parent card
  plus one addendum per context).
- **`core_fields`** — 27 entries, every in-scope agent, in 7 dimensions.
- **`extended_fields`** — 18 entries, required at Moderate and High, in 5
  dimensions.
- **`impact_derivation`** — the two outputs (OMB high-impact status ①,
  operational tier ②), the trigger rules, the unknown-floor, and what each level
  additionally requires.
- **`comparability_spine`** — the 9 controlled values that make cards
  comparable across states.
- **`public_layer`** — the subset of fields marked as publishable, for an
  adopting authority that chooses to publish part of a card. What is actually
  published is that authority's decision, not the schema's.

Each field entry carries its `id`, `group`, `label`, the plain-language
`question`, its `type` and enum `values` where controlled, `public: true` when
it belongs to the public layer, `comparability: true` when it is on the spine,
and — for the six derivation inputs — the glosses and help text that keep
answers honest.

## Two layers, two change rules

**The content layer** — question wording, glosses, help text, ordering,
non-derivation fields — is edited freely. Changes flow straight into the next
interview, because the skill reads the schema at run time rather than embedding
it.

**The derivation contract** — the ids and enum values of C7, C8, C10, C11, C11a
and C12, and the rules over them — changes only with an explicit bump of
`derivation_contract_version`. Consumers that compute a tier must declare which
contract they were built for and refuse to compute against a different one. The
engine in this repo does exactly that: a mismatch exits non-zero rather than
risk publishing a wrong Impact Level.

## Using it in your own tooling

Read the YAML, then walk `core_fields` and `extended_fields`. Two rules keep a downstream renderer honest:

1. **Never hard-code field content.** Labels, questions and enum values come
   from the file, so a schema update reaches your surface for free.
2. **Never compute the Impact Level yourself unless you implement
   `impact_derivation` exactly and pin the contract version.** Otherwise call
   [`../skills/agent-governance-card/scripts/derive_impact.py`](../skills/agent-governance-card/scripts/derive_impact.py),
   which takes a JSON fill and returns the verdict.

A filled card should always record `card_version` and
`derivation_contract_version` alongside the answers, so it can be read later
against the rules that produced it.
