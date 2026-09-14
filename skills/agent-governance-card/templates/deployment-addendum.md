# DEPLOYMENT ADDENDUM — ⟨context/unit⟩ · ⟨agent name⟩

> Card v0.4 platform pattern (schema `unit_of_analysis`): a platform or product
> used by many units files **one parent card** for the shared layer plus **one
> short addendum like this per deployment context**. The parent card answers
> everything about the shared layer (model, hosting and platform, vendor,
> identity architecture, exit terms); this addendum answers only what changes
> in THIS context. If any answer below moves one of the six derivation inputs
> (2.5, 3.1, 4.1, 4.2, 4.3, 4.4) relative to the parent card, re-derive the
> Impact Level for this context — the addendum carries its own level.

| | |
|---|---|
| **Parent card** | ⟨link/id + parent card version⟩ |
| **Deploying unit + contact** | ⟨unit, contact role⟩ |
| **Filled by / date** | ⟨name/role · YYYY-MM-DD⟩ |
| **Impact Level (this context)** | ⟨inherited from parent / re-derived: LOW · MODERATE · HIGH⟩ ⟨(provisional)⟩ |

## What changes in this context

- **1.3 Purpose in this context** — status: ____ · value: ____
- **1.5 Location in this context** *(where this deployment is reached)* — status: ____ · value: ____
- **2.5 High-impact determination for THIS use** *(derivation input — the
  parent's answer does not transfer: the same platform can be benign in one
  context and consequential in another)* — status: ____ · value: ____
  - **2.6 Determination record** *(who/role/date/rationale)* — status: ____ · value: ____
- **3.1 Data sensitivity in this context** *(derivation input)* + **3.2 datasets touched** — status: ____ · value: ____
- **3.3 Tools/systems reachable in this context** *(if narrower or wider than parent)* — status: ____ · value: ____
- **4.1 Autonomy in this context** *(derivation input)* — status: ____ · value: ____
- **4.2 Reversibility · 4.3 worst plausible consequence at this context's scale**
  *(derivation inputs)* — status: ____ · value: ____
- **4.4 Red-line check for this context** *(derivation input — the trifecta can
  hold here even if it doesn't on the platform in general)* — status: ____ · value: ____
- **5.5 Disclosure in this context** *(are the people here told?)* — status: ____ · value: ____
- **6.1 Accountable owner for this deployment** *(role, not person)* — status: ____ · value: ____
- **7.1 Government function served** — status: ____ · value: ____
- **7.2 Lifecycle stage in this context** — status: ____ · value: ____

## Derivation for this context

⟨run the six derivation inputs through `scripts/derive_impact.py`; record
level, fired triggers, provisional flag⟩

## To resolve *(this context)*

- ⟨from the engine's `to_resolve`⟩

## Recorded gaps *(this context)*

- ⟨field⟩ — ⟨status⟩ — ⟨one line⟩
