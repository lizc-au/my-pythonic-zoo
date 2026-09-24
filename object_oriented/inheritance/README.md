# Inheritance

Inheritance lets a class specialise a base type and take part in its contract. The syntax is simple; deciding whether the subtype relationship is meaningful takes more care.

## Compare the Examples

| Question | [Movement Hierarchy](./inappropriate_inheritance_example.py) | [Animal Specialisations](./appropriate_inheritance_example.py) |
| :--- | :--- | :--- |
| What does the base represent? | `WalkingAnimal` or `SlitheringAnimal` | An abstract `Animal` contract |
| Why do subclasses exist? | To reuse movement code | To provide animal-specific feeding behaviour |
| Does the relationship fit the domain? | Movement is a capability that can vary independently. | Each concrete type is an `Animal` with required behaviour. |
| What does client code depend on? | Movement-based classes | The shared `Animal` abstraction |
| Main lesson | Working code can still express an awkward hierarchy. | Subtypes can honour a useful shared contract. |

Run them from the repository root:

| Order | Command |
| :--- | :--- |
| 1 | `python -m object_oriented.inheritance.inappropriate_inheritance_example` |
| 2 | `python -m object_oriented.inheritance.appropriate_inheritance_example` |

Code reuse alone does not establish an *is-a* relationship. Ask whether code written for the base type can receive the subtype without special knowledge of that subtype.

<details>
<summary>Why movement is a poor hierarchy here</summary>

In the first example, `Panda` inherits walking and `Python` inherits slithering. Python permits that design, but it makes a movement capability part of each animal's fundamental type.

| New requirement | Pressure on a movement hierarchy |
| :--- | :--- |
| An animal can walk and swim. | Capabilities no longer fit one simple branch. |
| Movement changes with circumstances. | Fixed ancestry cannot express the choice cleanly. |
| Another independent capability varies. | Combinations of subclasses multiply. |

The [Composition exhibit](../composition/README.md) instead gives an `Animal` a `Movement` collaborator. Inheritance describes a type relationship; composition assembles behaviour from parts.

</details>

<details>
<summary>Why the Animal hierarchy is meaningful</summary>

The second example has a concrete requirement: each supported animal must provide appropriate feeding instructions. An abstract `Animal` supplies shared `describe()` behaviour and requires `feeding_instructions()` through `@abstractmethod`.

| Concrete subtype | What it supplies |
| :--- | :--- |
| `Python` | Feeding instructions appropriate to a python. |
| `Panda` | Feeding instructions appropriate to a panda. |
| `Lion` and `Elephant` | Their own implementations of the same contract. |

Code accepting `Animal` can use these subtypes without branching on their concrete classes. [The substitution test](../../tests/test_appropriate_inheritance_example.py) checks that intention with each animal type.

An abstract base class (`ABC`) makes the inheritance relationship explicit, which is nominal typing. The [Factory exhibit](../factory/README.md) instead uses a `Protocol` to describe compatible behaviour through structural typing.

</details>

<details>
<summary>Substitutability and domain modelling</summary>

The Liskov Substitution Principle (LSP) asks whether a subtype can be used where its base type is expected without breaking the base contract. Merely inheriting or passing `isinstance()` is not enough if a subtype rejects valid uses or changes the meaning of an operation.

[Domain Modelling](../domain_modelling/README.md) asks whether a difference deserves a distinct type. Inheritance adds a second question: whether that distinct type genuinely specialises another.

Biological taxonomy need not become a Python class hierarchy. If the application only records class, order, family, genus, and species, those distinctions can remain data.

</details>

<details>
<summary>Questions before creating a subclass</summary>

| Ask | Consider |
| :--- | :--- |
| Is this genuinely a specialised form of the base? | The relationship should mean more than shared implementation. |
| What contract do callers expect? | The subtype must preserve relevant behaviour and rules. |
| Can client code use it as the base type? | Special-case branches may signal a broken abstraction. |
| Does the software require this distinction? | Real-world categories alone do not require software subclasses. |
| Does a capability vary independently? | Composition or a function may express it more clearly. |

Payment types sharing a meaningful `authorise()` contract may form a useful hierarchy. Unrelated objects needing email delivery are more likely to share a service than an `EmailSendingObject` superclass.

</details>

The [Object-Oriented Python Glossary](../GLOSSARY.md) defines [inheritance](../GLOSSARY.md#inheritance), [contract](../GLOSSARY.md#contract), [ABC](../GLOSSARY.md#abstract-base-class-abc), and [LSP](../GLOSSARY.md#liskov-substitution-principle-lsp).

---

[Return to Object-Oriented Python](../README.md) for the next design question.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
