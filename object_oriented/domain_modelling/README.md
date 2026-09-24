# Domain Modelling

Domain modelling decides which concepts, data, rules, and responsibilities a program needs to represent. This pair of exhibits asks when a difference should stay as data and when it deserves a distinct type.

## Compare the Two Models

| Question | [Differences as Data](./data_model_example.py) | [Differences as Types](./domain_types_example.py) |
| :--- | :--- | :--- |
| What animals appear? | Ball Python, Giant Panda, Lion, and African Savanna Elephant | The same four animals |
| Where do taxonomy and diet live? | Values on one `Animal` type | Values on each animal type |
| Who provides `describe()`? | The shared `Animal` type | The shared `Animal` base |
| Is type-specific behaviour required? | No | Yes: feeding instructions |
| Are separate animal classes useful? | Not for recorded differences alone | Yes, because each owns its feeding behaviour |

Run both from the repository root:

| Order | Command |
| :--- | :--- |
| 1 | `python -m object_oriented.domain_modelling.data_model_example` |
| 2 | `python -m object_oriented.domain_modelling.domain_types_example` |

The second design is not automatically better. Each fits a different requirement; different data values alone do not justify different Python classes.

<details>
<summary>Why the first model keeps differences as data</summary>

The first example records common names, taxonomy, species, and diets on one `Animal` type. Every animal has the same responsibility and uses the same `describe()` behaviour.

Biological taxonomy is a hierarchy, but the software does not need to copy that hierarchy merely to record facts. Distinct classes would add complexity without a distinct responsibility.

| Dataclass option | Role in this example |
| :--- | :--- |
| `slots=True` | Prevents accidental extra instance attributes, including misspelled names. |
| `frozen=True` | Prevents reassignment of the recorded fields after construction. |

These options suit this particular model, but neither is required for domain modelling. Other applications may need mutable state or additional attributes.

</details>

<details>
<summary>Why the second model introduces domain types</summary>

The new requirement is to provide feeding instructions appropriate to each animal. `BallPython`, `GiantPanda`, `Lion`, and `AfricanSavannaElephant` now each own a meaningful `feeding_instructions()` behaviour.

The shared `Animal` abstract base class supplies `describe()` and requires the feeding method with `@abstractmethod`. A subtype that does not implement that method remains abstract and cannot be instantiated.

| Choice | Relationship expressed |
| :--- | :--- |
| Abstract base class (`ABC`) | Each concrete animal explicitly *is an* `Animal` in this domain model. |
| `Protocol` | An object satisfies a required interface by its behaviour, without necessarily inheriting from it. |

The Factory exhibit uses a Protocol for structural typing; this example uses an ABC because the explicit inheritance relationship matters. Neither choice is universally preferable.

</details>

<details>
<summary>Could feeding become composition?</summary>

Yes. Feeding stays on the concrete animal types here to make the modelling decision visible.

If feeding rules become complex, reusable, configurable, or changeable at runtime, a separate feeding object may be a clearer owner. The animal could collaborate with it, as explored in [Composition](../composition/README.md).

Introducing a domain type does not lock the design into one permanent inheritance structure. Responsibilities can move when requirements change.

</details>

<details>
<summary>How this applies beyond the zoo</summary>

A document system might first record invoices, claims, and correspondence as categories on one `Document` type. If those categories later acquire separate payment, assessment, or delivery rules, distinct types may become useful.

| Question to ask | Why it matters |
| :--- | :--- |
| Is this difference only information to record? | Data may be enough. |
| Does the concept own a distinct rule or behaviour? | A separate type may express that responsibility. |
| Is the behaviour shared or independently variable? | Composition may fit better than inheritance. |
| Does another type clarify today's requirements? | Avoid predicting abstractions without a current need. |

Model the domain broadly, but introduce software distinctions when the application's actual responsibilities justify them.

</details>

The [Object-Oriented Python Glossary](../GLOSSARY.md) explains terms such as [domain modelling](../GLOSSARY.md#domain-modelling), [ABC](../GLOSSARY.md#abstract-base-class-abc), [Protocol](../GLOSSARY.md#protocol), and [structural typing](../GLOSSARY.md#structural-typing).

---

[Return to Object-Oriented Python](../README.md) for the next design question.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
