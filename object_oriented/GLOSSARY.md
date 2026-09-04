# Object-Oriented Python Glossary

This glossary explains object-oriented programming terms used throughout the
MyPythonicZoo Object-Oriented Python examples.

Definitions are written for practical software development rather than as
formal computer-science definitions. Zoo examples are used where helpful, but
the concepts apply equally to other domains such as documents, orders,
notifications, reports, storage systems, and payment processing.

---

## Abstraction

An **abstraction** exposes the important parts of something while hiding details
that other code does not need to know.

For example, client code can ask an `Animal` to `speak()` without knowing how a
particular animal implements that behaviour.

Good abstractions reduce the amount of knowledge one part of a program needs
about another.

---

## Abstract Base Class (ABC)

An **abstract base class** defines a common base for related classes and can
require subclasses to implement particular methods.

Unlike a `Protocol`, an ABC normally establishes an explicit inheritance
relationship.

An ABC is useful when classes genuinely belong to the same inheritance
hierarchy, particularly when they also share implementation or state.

---

## Attribute

An **attribute** is data or behaviour associated with an object or class.

Instance attributes commonly describe the state of one particular object, such
as an animal's name or age.

Methods are also attributes, although in everyday discussion "attribute" often
refers specifically to stored data.

---

## Behaviour

A **behaviour** is something an object can do.

In the Factory example, `speak()` is behaviour provided by each concrete animal
class.

More complex designs may model behaviours separately and combine them with the
objects that use them. See the Composition examples.

---

## Class

A **class** defines a type of object.

It describes the data and behaviour that its instances can provide.

For example, `Lion` is a class. Individual lion objects can be created from
that class.

---

## Client Code

**Client code** is code that uses another component through its public
interface.

In the Factory example, `factory_example.py` is client code. It asks `AnimalFactory`
for an animal and then uses the returned `Animal` without needing to understand
the factory's internal construction logic.

"Client" here does not necessarily mean a person, web browser, or remote
computer. It simply means code consuming another piece of code.

---

## Cohesion

**Cohesion** describes how closely the responsibilities within a module, class,
or component belong together.

High cohesion is generally desirable: a class should have a clear purpose
rather than accumulating unrelated jobs.

For example, an `Animal` object should not automatically become responsible
for persistence, reporting, notifications, veterinary scheduling, and every
other operation that happens to involve an animal.

---

## Collaboration

**Collaboration** is the way objects or other components work together to
complete a larger task while retaining their own responsibilities.

Rather than one object performing every operation itself, collaborating objects
ask one another for the behaviour or information they own. This can make
responsibility boundaries clearer and reduce the need for one class to know how
every part of a process works.

In the [Responsibilities & Collaboration examples](responsibilities/README.md),
`KeeperReport` collaborates with `FeedingGuide` and `CareSchedule` to produce a
report. Each object contributes the part of the work it owns.

Collaboration describes the interaction between components. It does not by
itself determine whether those responsibility boundaries are well designed.

---

## Composition

**Composition** builds an object by combining it with other objects that provide
parts of its behaviour or functionality.

It expresses a **has-a** relationship rather than an **is-a** inheritance
relationship.

For example, an object could have a movement behaviour rather than inheriting
from increasingly specialised movement-based classes.

Composition is particularly useful when behaviours can vary independently.

---

## Concrete Class

A **concrete class** is a class that can be instantiated to create usable
objects.

In the Factory example, `Python`, `Panda`, `Lion`, and `Elephant` are concrete
classes.

They provide the real `speak()` implementations required by the `Animal`
Protocol.

---

## Contract

A **contract** describes what other code can rely on a component to provide.

A contract may describe required methods, accepted inputs, returned values,
exceptions, or other guarantees.

In the Factory example, the `Animal` Protocol forms a contract requiring a
compatible `speak()` method.

Programming contracts are design agreements expressed through code,
documentation, types, tests, or a combination of these.

---

## Coupling

**Coupling** describes how strongly one part of a program depends on the
details of another.

Lower coupling generally makes components easier to change, test, and reuse.

The Factory example reduces coupling by allowing client code to depend on the
`Animal` contract rather than importing and selecting every concrete animal
class itself.

Low coupling does not mean "no dependencies." Useful software components must
collaborate. The goal is to avoid unnecessary knowledge of implementation
details.

---

## Delegation

**Delegation** occurs when one object asks another object to perform work that
belongs to the second object's responsibility.

Delegation allows an object to participate in a larger operation without
implementing every rule itself. The delegating object remains responsible for
its own part of the process while relying on collaborators for work they own.

In the [Responsibilities & Collaboration examples](responsibilities/README.md),
`KeeperReport` delegates feeding guidance to `FeedingGuide` and care-date
calculation to `CareSchedule`. It then uses those results to perform its own
responsibility: formatting the keeper-facing report.

Delegation is commonly used with composition and collaboration, but the terms
describe different ideas. Composition describes how objects are assembled,
collaboration describes how components work together, and delegation describes
one component handing a specific piece of work to another.

---

## Dependency

A **dependency** is something a piece of code needs in order to perform its
responsibility.

For example, a reporting service might depend on a repository that supplies
data.

Dependencies can be classes, objects, functions, configuration, external
services, or other resources.

Making dependencies clear helps keep responsibilities and relationships
understandable.

---

## Dependency Injection

A technique in which an object receives a [dependency](#dependency) from
outside rather than creating that dependency itself.

For example:

```python
animal = Animal(species="Python", movement=Slither())
```

`Animal` depends on a movement behaviour, but it does not construct `Slither`
itself. The movement object is supplied when the animal is created.

Dependency injection can make dependencies explicit and allow implementations
to be replaced without changing the object that uses them. This is particularly
useful for configurable behaviour, testing, and reducing coupling.

Dependency injection is often used with [Composition](#composition), but the
terms are not interchangeable. Composition describes building an object from
collaborating parts; dependency injection describes how one of those parts is
supplied.

---

## Domain Modelling

**Domain modelling** is the process of representing important concepts,
relationships, data, rules, and responsibilities from a problem domain in
software.

A domain model does not need to reproduce every distinction that exists in the
real world. It represents the distinctions that matter to the application's
requirements.

For example, different animal species may initially be represented by data on
one `Animal` type. Separate animal types become useful when the application
needs those concepts to own meaningfully different rules or behaviour.

Good domain modelling therefore asks not only what things exist in the domain,
but which differences the software actually needs to represent and where the
resulting responsibilities belong.

---

## Encapsulation

**Encapsulation** keeps related state and behaviour together and controls which
details other code should depend upon.

It allows an object or component to expose a useful public interface while
keeping implementation details internal.

Encapsulation is not merely making attributes "private." Its broader purpose is
to protect boundaries and prevent unrelated code from depending on details that
should be free to change.

Encapsulation also helps an object preserve its [invariants](#invariant) by
providing deliberate operations for valid state changes. In Python, conventions
such as a leading underscore and mechanisms such as name mangling communicate
and support these boundaries, but they do not create an enforced security
boundary. See [Encapsulation & Invariants](encapsulation/README.md) for a
detailed example.

---

## Factory

A **factory** is an object, function, or method responsible for creating other
objects.

Factories are useful when selecting or constructing the correct concrete
object is a responsibility worth separating from the code that will use it.

In the Factory example:

```python
animal = AnimalFactory.create("lion")
```

The caller requests an animal. `AnimalFactory` owns the decision that `"lion"`
maps to the `Lion` class.

A factory is unnecessary when direct construction is already the clearest
solution.

---

## Inheritance

**Inheritance** creates a new class based on another class.

It commonly represents an **is-a** relationship and allows a subclass to
inherit behaviour or state from a base class.

Inheritance is useful when the relationship is genuine and shared behaviour or
a common hierarchy provides value.

It should not be introduced merely because two classes contain similar code.
Composition or another form of reuse may provide a cleaner design.

---

## Instance

An **instance** is a particular object created from a class.

For example:

```python
lion = Lion()
```

`Lion` is the class.

`lion` is an instance of `Lion`.

Multiple independent instances can normally be created from the same class.

---

## Interface

An **interface** describes the operations through which other code interacts
with a component.

Python does not require one special language construct called `interface`.
Interfaces can be expressed through protocols, abstract base classes, public
methods, functions, or other deliberately exposed operations.

A good interface tells callers what they can do without requiring them to know
how the component does it internally.

---

## Invariant

An **invariant** is a condition that must remain true for an object to be in a
valid state.

An invariant is more than an input-validation rule. If an object owns the rule,
the condition should continue to hold throughout the object's valid lifetime,
including after state changes.

In the [Encapsulation & Invariants examples](encapsulation/README.md), an
`Animal` has the invariant that its recorded weight must be greater than zero.
Checking the weight only during construction is insufficient if client code can
later replace it with an invalid value.

Encapsulation can help an object preserve its invariants by exposing operations
that validate meaningful state changes rather than allowing relevant state to
be changed arbitrarily.

---

## Liskov Substitution Principle (LSP)

The **Liskov Substitution Principle (LSP)** states that a subtype should be
usable where its base type is expected without breaking the expectations
established by that base type.

This means more than simply inheriting from a class or passing an
`isinstance()` check. A subtype should honour the relevant contract of its base
type so that client code does not need special handling simply because a
particular subtype was supplied.

In the [Inheritance examples](inheritance/README.md), `Python`, `Panda`, `Lion`,
and `Elephant` can each be supplied to code written to work with `Animal`.

---

## Method

A **method** is a function associated with a class.

Instance methods normally operate on a particular object and receive that
instance as `self`.

For example:

```python
animal.speak()
```

calls the `speak()` method belonging to the object referenced by `animal`.

Python also supports class methods and static methods, which have different
relationships with the class and its instances.

---

## Nominal Typing

**Nominal typing** determines type compatibility from explicitly declared type
relationships.

Inheritance is a common example:

```python
class Lion(Animal): ...
```

Here `Lion` explicitly declares that it derives from `Animal`.

Compare this with structural typing, where compatibility can be based on the
behaviour an object provides rather than its declared ancestry.

---

## Object

An **object** is a runtime value that combines identity, state, behaviour, or
some combination of these.

Objects are created from classes.

For example:

```python
lion = Lion()
```

creates a `Lion` object and assigns a reference to it to `lion`.

In Python, many things are objects, including classes themselves.

That is why the Factory example can store classes such as `Lion` inside a
dictionary and call them later.

---

## Polymorphism

**Polymorphism** allows different kinds of objects to be used through the same
interface or contract.

For example:

```python
animal = AnimalFactory.create(animal_type)
animal.speak()
```

`animal` might refer to a `Python`, `Panda`, `Lion`, or `Elephant`.

The client code does not need separate logic for each concrete type because
each object satisfies the same `Animal` contract.

Polymorphism is often associated with inheritance, but inheritance is not
required. Python can also achieve polymorphism through structural typing and
protocols.

---

## Protocol

A **Protocol** describes behaviour an object must provide without requiring the
object's class to inherit from the Protocol.

For example:

```python
class Animal(Protocol):
    def speak(self) -> None: ...
```

A class with a compatible `speak()` method can satisfy this contract even when
it does not explicitly inherit from `Animal`.

Protocols therefore work naturally with Python's structural typing.

---

## Public API

A **public API** is the deliberately exposed interface that other code is
expected to use.

"API" does not necessarily mean a web service.

A Python package, class, or module can have a public API.

For example, `factory.animals.__init__.py` exposes the animal types that other
parts of the Factory example are intended to import.

Keeping a deliberate public API reduces unnecessary dependence on internal
implementation details.

---

## Registry

A **registry** stores a relationship between identifiers and objects,
functions, classes, or other values that can later be selected by identifier.

The Factory example uses:

```python
_animal_types = {
    "python": Python,
    "panda": Panda,
    "lion": Lion,
    "elephant": Elephant,
}
```

This allows the factory to look up the appropriate creator rather than growing
a long sequence of conditional branches.

Registries are useful when a set of implementations must be selected by name
or another key.

---

## Responsibility

A **responsibility** is a job that a class, object, function, module, or other
component owns.

Good object-oriented design involves deciding not only how something should be
done, but **which component should be responsible for doing it**.

The Factory example gives `AnimalFactory` responsibility for selecting and
creating concrete animal objects. Client code is responsible for using the
returned object, not deciding how it should be constructed.

See the Responsibilities and Collaboration examples for deeper treatment.

---

## Single Responsibility Principle (SRP)

The **Single Responsibility Principle (SRP)** is the design principle that a
class or other component should have one coherent responsibility, often
expressed as having one reason to change.

SRP does not mean that every class should contain only one method or that every
small piece of behaviour requires its own class. A class can have several
methods when those methods contribute to the same responsibility. For example,
a `KeeperReport` might have methods to create a report heading, format report
details, and produce the final report. Those methods all support the same
responsibility: presenting keeper-facing information. Feeding rules, however,
change for different reasons and belong to a different responsibility. Several
methods are fine when they are all part of the same job.

In the [Responsibilities & Collaboration examples](responsibilities/README.md),
the overloaded `Animal` can change because of animal-domain requirements,
feeding policy, care scheduling, or report formatting. The collaborating design
gives those distinct responsibilities more focused owners.

Applying SRP therefore requires judgement. Separating responsibilities can
improve cohesion and make change safer, but creating abstractions before the
current requirements justify them can make a design unnecessarily complex.

---

## State

**State** is the data describing an object's current condition at a particular
point in time.

For example, an animal object might contain a name, age, or current status.

Behaviour may depend on state, and behaviour may change state.

Not every descriptive difference needs to become another class. See the Domain
Modelling examples for deciding when information belongs in state/data and when
a separate type is justified.

---

## Structural Typing

**Structural typing** determines compatibility from the structure or behaviour
an object provides rather than requiring an explicitly declared inheritance
relationship.

If the `Animal` Protocol requires:

```python
def speak(self) -> None: ...
```

then a `Lion` providing a compatible `speak()` method can satisfy that Protocol
without writing:

```python
class Lion(Animal):
```

This differs from nominal typing, where the declared type relationship itself
determines compatibility.

Structural typing formalises an idea closely related to Python's traditional
duck typing while allowing static type checkers to verify the contract.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/GLOSSARY.md_ | _4 September 2026_ | _lizc-au_ |
