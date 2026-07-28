# DEPLOYMENT ADDENDUM — ⟨context/unit⟩ · ⟨agent name⟩

> Card v0.3 platform pattern (schema `unit_of_analysis`): a platform or product
> used by many units files **one parent card** for the shared layer plus **one
> short addendum like this per deployment context**. The parent card answers
> everything about the shared layer (model, vendor, identity architecture,
> exit terms); this addendum answers only what changes in THIS context.
> If any answer below moves a derivation input (⚙) relative to the parent
> card, re-derive the Impact Level for this context — the addendum carries its
> own level.

| | |
|---|---|
| **Parent card** | ⟨link/id + parent card version⟩ |
| **Deploying unit + contact** | ⟨unit, contact role⟩ |
| **Filled by / date** | ⟨name/role · YYYY-MM-DD⟩ |
| **Impact Level (this context)** | ⟨inherited from parent / re-derived: LOW · MODERATE · HIGH⟩ ⟨(provisional)⟩ |

## What changes in this context

- **Purpose in this context** *(C3)* — status: ____ · value: ____
- **High-impact determination for THIS use** *(C7 ⚙ — the parent's answer does
  not transfer: the same platform can be benign in one context and
  consequential in another)* — status: ____ · value: ____
  - **Determination record** *(C7a — who/role/date/rationale)* — status: ____ · value: ____
- **Data touched in this context & sensitivity** *(C8 ⚙ + C8a)* — status: ____ · value: ____
- **Tools/systems reachable in this context** *(C9, if narrower or wider than parent)* — status: ____ · value: ____
- **Autonomy in this context** *(C10 ⚙)* — status: ____ · value: ____
- **Reversibility · worst plausible consequence at this context's scale**
  *(C11 ⚙ · C11a ⚙)* — status: ____ · value: ____
- **Red-line check for this context** *(C12 ⚙ — the trifecta can hold here even
  if it doesn't on the platform in general)* — status: ____ · value: ____
- **Government function served** *(C17)* — status: ____ · value: ____
- **Lifecycle stage in this context** *(C18)* — status: ____ · value: ____
- **Disclosure in this context** *(C22 — are the people here told?)* — status: ____ · value: ____
- **Accountable owner for this deployment** *(C14 — role, not person)* — status: ____ · value: ____

## Derivation for this context

⟨run the six ⚙ answers through `scripts/derive_impact.py`; record level,
fired triggers, provisional flag⟩

## To resolve *(this context)*

- ⟨from the engine's `to_resolve`⟩

## Recorded gaps *(this context)*

- ⟨field⟩ — ⟨status⟩ — ⟨one line⟩
