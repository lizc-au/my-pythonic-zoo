# Factory Pattern - Creating Zoo Animals

The Factory Pattern separates **object creation** from the code that uses the
created objects.

This factory example uses four MyPythonicZoo animals:

- Python
- Panda
- Lion
- Elephant

The animals deliberately have very simple behaviour. The purpose of this
factory example is not to build a complete animal model, but to demonstrate a
production-shaped Factory design without unrelated complexity.

---

## The problem Factory Pattern solves

Without a Factory, client code that needs an animal may also need to know which
concrete class to import and instantiate.

For example, client code might directly create:

```python
lion = Lion()
```

That is perfectly reasonable when the caller already knows that it needs a
`Lion`.

A Factory becomes useful when **choosing and constructing the concrete object
is itself a responsibility that should be separated from the code using the
object**.

In this factory example, client code instead asks:

```python
animal = AnimalFactory.create("lion")
```

The caller requests what it needs. The Factory decides which concrete class
satisfies that request.

---

## The design used here

The factory example separates several responsibilities:

```text
animals/animal.py
    Defines the Animal Protocol - the behaviour Factory-created objects promise.

animals/python.py
animals/panda.py
animals/lion.py
animals/elephant.py
    Provide concrete implementations of that contract.

animals/__init__.py
    Defines the public interface of the animals package.

animal_factory.py
    Owns the mapping between identifiers and concrete animal creators.

factory_example.py
    Represents client code that asks the factory for animals and uses them.
```

`AnimalFactory` uses a registry rather than a growing chain of `if`, `elif`, or
`match` branches:

```python
_animal_types = {
    "python": Python,
    "panda": Panda,
    "lion": Lion,
    "elephant": Elephant,
}
```

Python classes are objects themselves, so they can be stored as values in the
registry and called later to create instances.

## Factory and polymorphism working together

The most important client code in the factory example is deliberately small:

```python
animal = AnimalFactory.create(animal_type)
animal.speak()
```

`AnimalFactory.create()` promises to return an object satisfying the `Animal`
Protocol.

The client therefore does not need to ask:

```python
if isinstance(animal, Lion):
    ...
elif isinstance(animal, Panda):
    ...
```

Nor does it need to know which concrete constructor the factory selected.

It knows only that the returned object satisfies the `Animal` contract and can
therefore call:

```python
animal.speak()
```

This is [polymorphism](../GLOSSARY.md#polymorphism) through
[structural typing](../GLOSSARY.md#structural-typing): the concrete classes satisfy
the Protocol because they provide the required behaviour, rather than because
they inherit from a shared base class.

---

## Why use a Protocol?

The concrete animal classes do not share implementation or state in this
factory example. They simply need to provide compatible behaviour.

Using a `Protocol` allows the design to express:

> An Animal is anything that satisfies the behaviour required by this contract.

That avoids introducing an inheritance hierarchy solely for the purpose of
typing.

An abstract base class may be more appropriate when related classes genuinely
need shared implementation, shared state, or an explicitly enforced
inheritance relationship.

See `animals/animal.py` for the complete contract and its scope.

---

## Real-world uses of factories

The construction in this factory example is intentionally small, but the same pattern
can isolate much more substantial creation decisions.

A factory can be useful for:

- **Configuration-driven creation** - select an implementation from a
  configuration file, command-line option, or application setting.
- **User-driven selection** - create the appropriate object for a type selected
  through a UI, API request, imported file, or other external input.
- **Dependency construction** - create objects that require different
  collaborators or services without making callers understand those details.
- **Environment-specific implementations** - select different implementations
  for development, testing, operating systems, deployment environments, or
  available capabilities.
- **Plug-in architectures** - create implementations registered by extensions
  without requiring client code to know every concrete type.
- **Complex construction** - encapsulate creation that requires validation,
  configuration, several constructor arguments, or collaborating objects.
- **Stable client interfaces** - allow concrete implementations to change while
  callers continue depending on the same contract.

A factory does not need to perform all of these jobs. They are examples of
creation responsibilities that can justify introducing a factory boundary.

---

## Benefits

This design provides several practical benefits:

- Client code is decoupled from concrete animal classes.
- Object-selection logic has one clear home.
- The factory returns a stable `Animal` contract.
- New registered implementations do not require another conditional branch.
- Concrete classes remain small and independently focused.
- Static type checking can verify the contract.
- Creation policy can change without forcing equivalent changes throughout
  client code.

---

## Trade-offs

A factory introduces another abstraction and another place a developer must
look when tracing object creation.

That cost is worthwhile when creation genuinely requires selection, policy, or
encapsulation. It is unnecessary when direct construction is already clear.

Do not replace:

```python
lion = Lion()
```

with a factory merely because factories are considered a design pattern.

A design pattern should solve an identifiable design problem.

---

## Related object-oriented examples

This factory example intentionally keeps the `Animal` contract narrow.

For other OO design questions, see the related example sets:

- **Composition** - modelling multiple or changeable behaviours separately and
  combining them with objects that use them.
- **Domain Modelling** - deciding whether differences between objects belong in
  data or justify separate types.
- **Responsibilities and Collaboration** - deciding which object should own a
  responsibility and how focused objects should work together.

These examples use familiar Zoo concepts, but the design principles apply
equally to objects such as documents, orders, notifications, reports, storage
providers, or payment processors.

---

## Run the factory example

From the repository root:

```text
python -m object_oriented.factory.factory_example
```

Expected output:

```text
Hiss!
Bleat!
Roar!
Trumpet!
```

The output is intentionally simple. The interesting part of this factory example is
how the objects are designed, created, typed, and used.

---

## Related concepts

The [Object-Oriented Python Glossary](../GLOSSARY.md) explains terminology used
throughout this factory example, including:

- [Abstraction](../GLOSSARY.md#abstraction)
- [Client Code](../GLOSSARY.md#client-code)
- [Concrete Class](../GLOSSARY.md#concrete-class)
- [Contract](../GLOSSARY.md#contract)
- [Coupling](../GLOSSARY.md#coupling)
- [Factory](../GLOSSARY.md#factory)
- [Polymorphism](../GLOSSARY.md#polymorphism)
- [Protocol](../GLOSSARY.md#protocol)
- [Public API](../GLOSSARY.md#public-api)
- [Registry](../GLOSSARY.md#registry)
- [Structural Typing](../GLOSSARY.md#structural-typing)

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/factory/README.md_ | _4 September 2026_ | _lizc-au_ |
