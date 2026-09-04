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

1. [Domain Modelling](domain_modelling/README.md)
   - Decide when a difference should remain data and when it should become a
     distinct domain type.
   - Compare one shared `Animal` model with explicit animal types introduced
     only when type-specific behaviour creates a meaningful responsibility.

2. [Encapsulation & Invariants](encapsulation/README.md)
   - Explore how objects can own and protect the rules governing their state.
   - Compare freely assignable state with a deliberate public interface for
    controlled state changes.
   - Examine what `_name`, `__name`, properties, and name mangling actually do
    and do not protect in Python.

3. [Responsibilities & Collaboration](responsibilities/README.md)
   - Decide which object should own which work.
   - Compare an overloaded `Animal` with focused collaborating objects.
   - Explore cohesion, delegation, responsibility boundaries, and the
     Single Responsibility Principle.    

4. [Composition](composition/README.md)
   - Build objects from collaborating behaviours.
   - Compare client-selected, construction-selected, and domain-type-selected
     composition.
   - Explore dependency injection and responsibility placement.

5. [Inheritance](inheritance/README.md)
   - Decide when a subtype genuinely represents a specialised form of its base
     type rather than merely sharing some implementation.
   - Compare inappropriate capability-based inheritance with meaningful
     specialisation of a shared `Animal` abstraction.
   - Explore contracts, substitutability, abstract base classes, and when
     composition is a better design.

6. [Factory Pattern](factory/README.md)
   - Centralise object creation.
   - Return a stable abstraction rather than exposing construction details.
   - Understand registries, protocols, polymorphism, and client code.            

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
- **Domain Modelling** determines whether differences such as animal species
  should remain data or justify distinct domain types with their own
  responsibilities.
- **Encapsulation & Invariants** determines how an object controls access to its
  state and preserves the rules that must remain true as that state changes.
- **Factory** may own construction of the correctly composed object.  
- **Inheritance** determines when one type genuinely specialises another and
  can honour the same contract, rather than using a superclass merely to reuse
  implementation.
- **Responsibilities & Collaboration** determines which object should own each
  responsibility and how objects should collaborate to complete larger tasks.

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

**Composition** provides three runnable variants:

```text
python -m object_oriented.composition.client_selected_example
python -m object_oriented.composition.construction_selected_example
python -m object_oriented.composition.domain_type_selected_example
```

**Domain Modelling** provides two contrasting models:

```text
python -m object_oriented.domain_modelling.data_model_example
python -m object_oriented.domain_modelling.domain_types_example
```

**Encapsulation & Invariants** provides two contrasting examples:

```text
python -m object_oriented.encapsulation.unprotected_state_example
python -m object_oriented.encapsulation.protected_state_example
```

**Factory** provides a runnable example:

```text
python -m object_oriented.factory.factory_example
```

**Inheritance** provides two contrasting examples:

```text
python -m object_oriented.inheritance.inappropriate_inheritance_example
python -m object_oriented.inheritance.appropriate_inheritance_example
```

**Responsibilities & Collaboration** provides two contrasting designs:

```text
python -m object_oriented.responsibilities.overloaded_animal_example
python -m object_oriented.responsibilities.collaborating_objects_example
```

---

## Glossary

The [Object-Oriented Python Glossary](GLOSSARY.md) provides plain-language
definitions for terminology used throughout these exhibits.

Useful starting points include:

- [Abstraction](GLOSSARY.md#abstraction)
- [Attribute](GLOSSARY.md#attribute)
- [Behaviour](GLOSSARY.md#behaviour)
- [Class](GLOSSARY.md#class)
- [Cohesion](GLOSSARY.md#cohesion)
- [Collaboration](GLOSSARY.md#collaboration)
- [Composition](GLOSSARY.md#composition)
- [Coupling](GLOSSARY.md#coupling)
- [Delegation](GLOSSARY.md#delegation)
- [Dependency](GLOSSARY.md#dependency)
- [Dependency Injection](GLOSSARY.md#dependency-injection)
- [Domain Modelling](GLOSSARY.md#domain-modelling)
- [Encapsulation](GLOSSARY.md#encapsulation)
- [Factory](GLOSSARY.md#factory)
- [Inheritance](GLOSSARY.md#inheritance)
- [Invariant](GLOSSARY.md#invariant)
- [Liskov Substitution Principle (LSP)](GLOSSARY.md#liskov-substitution-principle-lsp)
- [Method](GLOSSARY.md#method)
- [Object](GLOSSARY.md#object)
- [Polymorphism](GLOSSARY.md#polymorphism)
- [Protocol](GLOSSARY.md#protocol)
- [Responsibility](GLOSSARY.md#responsibility)
- [Single Responsibility Principle (SRP)](GLOSSARY.md#single-responsibility-principle-srp)
- [State](GLOSSARY.md#state)
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

