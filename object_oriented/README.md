# Object-Oriented Python

Explore object-oriented design through small, runnable Python examples. Each learning path begins with a design question and shows what a technique helps you decide.

## Suggested Learning Order

| Step | Topic | Design question |
| :--- | :--- | :--- |
| 1 | [Domain Modelling](./domain_modelling/README.md) | Should a difference remain data, or does it justify a distinct type with its own behaviour? |
| 2 | [Encapsulation & Invariants](./encapsulation/README.md) | Which rules govern an object's state, and how should changes be controlled? |
| 3 | [Responsibilities & Collaboration](./responsibilities/README.md) | Which object should own each task, and how should objects work together? |
| 4 | [Composition](./composition/README.md) | Which behaviours should be combined, and who should choose them? |
| 5 | [Inheritance](./inheritance/README.md) | Does a subtype genuinely specialise a base type and honour its contract? |
| 6 | [Factory Pattern](./factory/README.md) | Who should construct a correctly configured object for its clients? |

Each linked guide compares runnable designs and explains their trade-offs. Follow the order for a gradual introduction, or open the question most relevant to your own code.

## Try an Example

From the repository root, run `python -m object_oriented.domain_modelling.data_model_example`. Then compare it with `python -m object_oriented.domain_modelling.domain_types_example` to see when differences remain data and when they become types.

<details>
<summary>Commands for every learning path</summary>

| Topic | Command |
| :--- | :--- |
| Domain Modelling | `python -m object_oriented.domain_modelling.data_model_example` |
| Domain Modelling | `python -m object_oriented.domain_modelling.domain_types_example` |
| Encapsulation | `python -m object_oriented.encapsulation.unprotected_state_example` |
| Encapsulation | `python -m object_oriented.encapsulation.protected_state_example` |
| Responsibilities | `python -m object_oriented.responsibilities.overloaded_animal_example` |
| Responsibilities | `python -m object_oriented.responsibilities.collaborating_objects_example` |
| Composition | `python -m object_oriented.composition.client_selected_example` |
| Composition | `python -m object_oriented.composition.construction_selected_example` |
| Composition | `python -m object_oriented.composition.domain_type_selected_example` |
| Inheritance | `python -m object_oriented.inheritance.inappropriate_inheritance_example` |
| Inheritance | `python -m object_oriented.inheritance.appropriate_inheritance_example` |
| Factory | `python -m object_oriented.factory.factory_example` |

</details>

## How the Techniques Work Together

A program may use several techniques at once because each answers a different design question.

| Technique | Responsibility in a shared animal example |
| :--- | :--- |
| Domain Modelling | Decide whether species differences are data or distinct domain types. |
| Encapsulation & Invariants | Control changes to an animal's state and preserve its rules. |
| Responsibilities & Collaboration | Assign work to focused objects rather than overloading one `Animal`. |
| Composition | Connect an `Animal` with a `Movement` behaviour. |
| Inheritance | Use specialisation only when the subtype honours the base contract. |
| Factory | Construct and return the correctly configured object. |

The question to ask is: **What responsibility needs a home, and which technique expresses that choice clearly?**

<details>
<summary>Why the examples stay small</summary>

Small examples keep one design decision visible at a time. Real applications also need persistence, configuration, logging, interfaces, APIs, and other concerns that can obscure the relationship being taught.

The examples still aim to be defensible for their scope. An abstraction should solve a real design problem in the example, rather than exist merely to demonstrate a pattern.

</details>

<details>
<summary>Design approach used in these exhibits</summary>

| Preference | Why it helps |
| :--- | :--- |
| Focused objects | Responsibilities are easier to find and change. |
| Explicit contracts | Expectations become clear when an abstraction needs them. |
| Composition when appropriate | Avoid hierarchies that imply the wrong relationship. |
| Limited mutation | State is simpler to reason about when changes have a purpose. |
| Small modules | Related concepts can be studied without unrelated concerns. |
| Practical trade-offs | A technique is useful in context, not as an absolute rule. |
| Explanatory documentation | Readers can see why a design exists as well as what it does. |

</details>

## Glossary

The [Object-Oriented Python Glossary](./GLOSSARY.md) defines terms used throughout these exhibits, including abstraction, cohesion, coupling, delegation, polymorphism, and responsibility. Consult it whenever a design term is unfamiliar.

---

[Return to the Zoo map](../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_