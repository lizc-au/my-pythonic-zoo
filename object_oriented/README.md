# Object-Oriented Python

This section explores object-oriented design through small, runnable Python
examples.

The goal is not to collect patterns for their own sake. Each exhibit starts
with a specific design pressure and shows how a particular object-oriented
technique can help address it.

The examples are intentionally small, but the design questions are the same
ones that appear in larger production systems.

---

## Suggested learning order

1. [Factory Pattern](factory/README.md)
   - Centralise object creation.
   - Return a stable abstraction rather than exposing construction details.
   - Understand registries, protocols, polymorphism, and client code.

2. [Composition](composition/README.md)
   - Build objects from collaborating behaviours.
   - Compare client-selected, construction-selected, and domain-type-selected
     composition.
   - Explore dependency injection and responsibility placement.

3. [Domain Modelling](domain_modelling/README.md)
   - Decide when a difference should remain data and when it should become a
     distinct domain type.
   - Compare one shared `Animal` model with explicit animal types introduced
     only when type-specific behaviour creates a meaningful responsibility.

4. Responsibilities & Collaboration
   - Decide which object should own which work.
   - Explore cohesion, responsibility boundaries, collaboration, and the
     Single Responsibility Principle.

The final exhibit is a planned addition to this category.

---

## Patterns are not mutually exclusive

Object-oriented techniques and design patterns solve different kinds of
problems.

A production design might use several of them together.

For example:

```text
Factory
    chooses what to construct
        |
        v
Animal
    is composed with
        |
        v
Movement
```

At the same time:

- **Composition** defines how `Animal` collaborates with `Movement`.
- **Factory** may own construction of the correctly composed object.
- **Domain Modelling** determines whether differences such as animal species
  should remain data or justify distinct domain types with their own
  responsibilities.
- **Responsibilities & Collaboration** determines which object should own each
  decision.

The important question is therefore not:

> Which pattern should this program use?

A better question is:

> What design responsibility am I trying to place, and which technique helps
> express it clearly?

---

## Why the examples stay small

The code in this section is deliberately compact so that the design decision
remains visible.

Real applications usually contain additional concerns such as persistence,
configuration, logging, validation, user interfaces, APIs, and external
services. Adding all of those concerns to a teaching example can hide the
relationship being demonstrated.

Small examples make it easier to isolate one design question at a time.

That does not mean the examples should be intentionally poor or unrealistic.
Where an abstraction is introduced, it should have a genuine reason to exist
and should be defensible for the scope of the example.

---

## Run the examples

From the repository root:

```text
python -m object_oriented.factory.factory_example
```

Composition provides three runnable variants:

```text
python -m object_oriented.composition.client_selected_example
python -m object_oriented.composition.construction_selected_example
python -m object_oriented.composition.domain_type_selected_example
```

Domain Modelling provides two contrasting models:

```text
python -m object_oriented.domain_modelling.data_model_example
python -m object_oriented.domain_modelling.domain_types_example
```

---

## Glossary

The [Object-Oriented Python Glossary](GLOSSARY.md) provides plain-language
definitions for terminology used throughout these exhibits.

Useful starting points include:

- [Abstraction](GLOSSARY.md#abstraction)
- [Composition](GLOSSARY.md#composition)
- [Coupling](GLOSSARY.md#coupling)
- [Dependency](GLOSSARY.md#dependency)
- [Dependency Injection](GLOSSARY.md#dependency-injection)
- [Domain Modelling](GLOSSARY.md#domain-modelling)
- [Factory](GLOSSARY.md#factory)
- [Inheritance](GLOSSARY.md#inheritance)
- [Polymorphism](GLOSSARY.md#polymorphism)
- [Protocol](GLOSSARY.md#protocol)
- [Responsibility](GLOSSARY.md#responsibility)
- [Structural Typing](GLOSSARY.md#structural-typing)

---

## Approach used throughout this section

These exhibits favour:

- focused objects with clear responsibilities;
- explicit contracts where they improve understanding;
- composition over unnecessary inheritance hierarchies;
- immutable data structures where mutation is not required;
- small modules rather than large files containing unrelated concerns;
- practical trade-offs rather than absolute rules;
- documentation that explains **why** a design exists, not merely what the code
  does.

The aim is to make object-oriented design easier to reason about by connecting
terminology directly to executable examples.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/README.md_ | _4 September 2026_ | _lizc-au_ |

