# Composition

Composition builds an object from collaborators that provide parts of its behaviour. In these exhibits, an `Animal` *has a* `Movement` object and delegates its movement description to it.

## Three Ways to Choose a Behaviour

All three examples produce the same movements: a Python slithers, while a Panda, Lion, and Elephant walk. They differ in **who decides** which movement object belongs with each animal.

| Approach | Who selects `Movement`? | Example | Strength | Trade-off |
| :--- | :--- | :--- | :--- | :--- |
| [Client-selected](./client_selected_example.py) | Ordinary caller | `Animal(species="Python", movement=Slither())` | Explicit and configurable | Caller must know which behaviour fits. |
| [Construction-selected](./construction_selected_example.py) | Construction function | `create_animal("Python")` | Centralises assembly knowledge | The constructor must maintain the mapping. |
| [Domain-type-selected](./domain_type_selected_example.py) | Concrete domain type | `Python().create_animal()` | Keeps an intrinsic rule close to its type | Harder to vary for the same type. |

Run them from the repository root:

| Order | Command |
| :--- | :--- |
| 1 | `python -m object_oriented.composition.client_selected_example` |
| 2 | `python -m object_oriented.composition.construction_selected_example` |
| 3 | `python -m object_oriented.composition.domain_type_selected_example` |

The composition mechanism stays the same in every version. Choosing the collaborator is a separate responsibility.

<details>
<summary>How the Movement contract works</summary>

[`behaviours/movement.py`](./behaviours/movement.py) defines a `Movement` Protocol requiring `description() -> str`. `Slither` and `Walk` provide compatible methods, so the general [`Animal`](./animal.py) depends on the contract rather than either concrete movement class.

| Relationship | Meaning |
| :--- | :--- |
| A specialised animal *is an* Animal | Inheritance can represent a genuine subtype relationship in another design. |
| This `Animal` *has a* Movement | Composition supplies the collaborator used in these examples. |

The terminal examples need only a textual description. In a larger application, a composed behaviour could perform calculations, change state, issue commands, or drive an animation.

</details>

<details>
<summary>When each selection point fits</summary>

| Selection point | Suitable situation |
| :--- | :--- |
| Client | The caller genuinely chooses a formatter, storage provider, notification channel, or test double. |
| Construction boundary | Callers need a correctly assembled object but should not know all of its internal dependencies. |
| Domain type | A collaborator expresses an intrinsic rule of that type, such as a required validation policy. |

The construction example uses a small function rather than a full Factory Pattern implementation. A factory is one possible owner of construction, as explored in [Factory](../factory/README.md).

If one domain type later needs several valid behaviours, selecting a single fixed collaborator inside that type may become restrictive.

</details>

<details>
<summary>Composition, injection, inheritance, and responsibility</summary>

| Idea | Question it answers |
| :--- | :--- |
| Composition | Which collaborating parts does an object have? |
| Dependency injection | How does a required part get supplied from outside? |
| Inheritance | Does one type genuinely specialise another and honour its contract? |
| Domain Modelling | Should an animal distinction be data or a separate type? |
| Responsibilities & Collaboration | Who should own the selection and the work? |

Client-selected composition also demonstrates dependency injection. Domain-type-selected composition remains composition even though ordinary client code does not inject the movement.

Use composition when behaviours vary independently, are shared, need replacement, or deserve their own responsibility. Keep simple, fixed behaviour on the object when another collaborator would add complexity without clarifying the design.

</details>

The [Object-Oriented Python Glossary](../GLOSSARY.md) defines [composition](../GLOSSARY.md#composition), [dependency injection](../GLOSSARY.md#dependency-injection), [Protocol](../GLOSSARY.md#protocol), and related terms.

---

[Return to Object-Oriented Python](../README.md) for the next design question.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
