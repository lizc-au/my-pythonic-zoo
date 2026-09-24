# Encapsulation & Invariants

Encapsulation lets an object own its state and the rules for changing it through a deliberate public interface. These examples use one invariant: **an animal's recorded weight must remain greater than zero**.

## Compare the Two Examples

| Question | [Unprotected State](./unprotected_state_example.py) | [Protected State](./protected_state_example.py) |
| :--- | :--- | :--- |
| Is the starting weight validated? | Yes | Yes |
| How is weight read? | Public `weight_kg` attribute | Read-only `weight_kg` property |
| How is weight changed normally? | Assign `animal.weight_kg = value` | Call `animal.record_weight(value)` |
| Can ordinary assignment bypass the rule later? | Yes | No; the property has no setter |
| What happens to an invalid change request? | The invalid value can be stored | `ValueError` is raised and the valid weight stays in place |

Run both from the repository root:

| Order | Command |
| :--- | :--- |
| 1 | `python -m object_oriented.encapsulation.unprotected_state_example` |
| 2 | `python -m object_oriented.encapsulation.protected_state_example` |

Construction checks alone cannot preserve an invariant if callers can later replace the relevant state without validation. Public attributes are often appropriate in Python; this attribute needs a controlled change because it carries a domain rule.

<details>
<summary>How the protected interface works</summary>

Callers read `animal.weight_kg` and request changes with `animal.record_weight(195.0)`. The method validates the new value before updating the stored weight.

| Operation | Outcome |
| :--- | :--- |
| `animal.record_weight(-25.0)` | Raises `ValueError`; the previous valid weight remains. |
| `animal.weight_kg = -25.0` | Raises `AttributeError` because the read-only property has no setter. |
| `animal.weight_kg` | Returns the current weight through the public interface. |

The property and method make correct normal use clear. They do not make the underlying value impossible to reach deliberately.

</details>

<details>
<summary>What underscores do and do not protect</summary>

| Form | Meaning | Limit |
| :--- | :--- | :--- |
| `_weight_kg` | A convention that marks an implementation detail. | A caller can still assign to it. |
| `__weight_kg` | Triggers name mangling inside `Animal`, producing a name like `_Animal__weight_kg`. | A determined caller can still use the mangled name. |

A double underscore helps prevent accidental interference; it is not a security boundary. [The deliberate bypass test](../../tests/test_protected_state_example.py) assigns through the mangled name to demonstrate that limit.

Application code should respect the object's public contract. The test intentionally breaks it so the exhibit does not imply stronger privacy than Python provides.

</details>

<details>
<summary>Mutation, immutability, and other choices</summary>

A `@dataclass(slots=True, frozen=True)` can suit a model whose fields should not normally be reassigned after construction. Recorded weight differs because changing it is a legitimate operation, so this example permits controlled mutation.

| Choice | When it may fit |
| :--- | :--- |
| Public attribute | No invariant needs to govern later assignment. |
| Read-only property and method | Callers should inspect a value but request meaningful, validated changes. |
| Immutable object | The domain concept should not change after construction. |
| Custom `__setattr__()` | Lower-level interception is genuinely needed; it would obscure this introductory lesson. |

Only one animal appears because species differences are not the question here. Other exhibits explore [Domain Modelling](../domain_modelling/README.md) and [Responsibilities & Collaboration](../responsibilities/README.md).

</details>

<details>
<summary>Where the same question appears elsewhere</summary>

| Domain object | Possible invariant | Meaningful operation |
| :--- | :--- | :--- |
| `Order` | Quantity stays above zero. | Change quantity with validation. |
| `InsuranceClaim` | Status follows allowed transitions. | Move from Submitted to Assessed before Approved. |
| Bank account | A withdrawal respects available funds. | Withdraw through a checked operation instead of replacing a balance. |

Ask which object owns the rule and whether normal client code can change its state without going through it. An invariant matters when it reflects an actual requirement of the application.

</details>

The [Object-Oriented Python Glossary](../GLOSSARY.md) defines [encapsulation](../GLOSSARY.md#encapsulation), [invariant](../GLOSSARY.md#invariant), [public API](../GLOSSARY.md#public-api), and related terms.

---

[Return to Object-Oriented Python](../README.md) for the next design question.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
