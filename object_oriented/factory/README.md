# Factory Pattern

A factory separates object creation from the code that uses the result. This exhibit selects a Python, Panda, Lion, or Elephant while client code works with one `Animal` contract.

## When a Factory Helps

| Situation | Construction choice |
| :--- | :--- |
| The code already knows it needs a Lion. | Use `lion = Lion()` directly. |
| The animal type comes from input or configuration. | Use `AnimalFactory.create(animal_type)` to select the constructor. |
| Different objects need different setup or collaborators. | Put that construction policy behind a clear boundary. |

A factory is useful when selection or assembly is a real responsibility. Direct construction remains clearer when the choice is already known.

## Follow the Design

| File | Role |
| :--- | :--- |
| [`animals/animal.py`](./animals/animal.py) | Define the `Animal` Protocol and its `speak()` contract. |
| [Concrete animals](./animals/) | Provide `Python`, `Panda`, `Lion`, and `Elephant` implementations. |
| [`animals/__init__.py`](./animals/__init__.py) | Expose the intended public animal imports. |
| [`animal_factory.py`](./animal_factory.py) | Map identifiers to concrete constructors. |
| [`factory_example.py`](./factory_example.py) | Ask the factory for animals, then use the returned contract. |

The registry maps strings such as `"lion"` to class objects such as `Lion`. Python classes can be stored as values and called later to create instances.

Run `python -m object_oriented.factory.factory_example` from the repository root. The animals respond in order with `Hiss!`, `Bleat!`, `Roar!`, and `Trumpet!`.

<details>
<summary>How the factory and Protocol work together</summary>

Client code can request `animal = AnimalFactory.create(animal_type)` and then call `animal.speak()`. It does not need to import each concrete class or branch on `isinstance(animal, Lion)`.

| Idea | Role here |
| :--- | :--- |
| Factory | Owns the choice and construction of a concrete animal. |
| `Animal` Protocol | Describes the behaviour returned objects must provide. |
| Polymorphism | Lets the client call `speak()` on different concrete animals. |
| Structural typing | Recognises compatible behaviour without requiring concrete classes to inherit from `Animal`. |

The concrete classes share neither implementation nor state in this example, so a Protocol expresses the narrow contract. An abstract base class may fit a design that needs shared code, state, or an explicit inheritance relationship.

</details>

<details>
<summary>Where factories are useful and what they cost</summary>

| Use case | Creation responsibility |
| :--- | :--- |
| User input or configuration | Select an implementation by name or setting. |
| Environment or testing | Choose a suitable implementation or test double. |
| Plug-ins | Construct a registered extension without teaching every client its class. |
| Complex setup | Validate configuration and assemble required collaborators. |

A factory keeps selection logic in one place and gives clients a stable contract. It also adds another abstraction to trace, so use it when the creation decision justifies that cost.

Related exhibits explore [Composition](../composition/README.md), [Domain Modelling](../domain_modelling/README.md), and [Responsibilities & Collaboration](../responsibilities/README.md). Those techniques may work alongside a factory because each addresses a different design decision.

</details>

The [Object-Oriented Python Glossary](../GLOSSARY.md) defines [factory](../GLOSSARY.md#factory), [registry](../GLOSSARY.md#registry), [Protocol](../GLOSSARY.md#protocol), and [polymorphism](../GLOSSARY.md#polymorphism).

---

[Return to Object-Oriented Python](../README.md) for other design questions.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
