# Inheritance

Inheritance allows one class to specialise another class and participate in the
contract defined by that base type.

The syntax is simple. The design decision is not.

A useful question is:

> When does one type genuinely represent a specialised form of another type,
> rather than merely sharing some of its code?

This exhibit compares two designs:

1. [inappropriate_inheritance_example.py](inappropriate_inheritance_example.py)
   uses inheritance to model movement.
2. [appropriate_inheritance_example.py](appropriate_inheritance_example.py)
   uses inheritance to represent meaningful specialisations of a shared
   `Animal` abstraction.

The first design works. That does not make it a good inheritance hierarchy.

---

## 1. Inheritance used only to share behaviour

The first example contains:

```python
class WalkingAnimal:
    def move(self) -> str:
        return "Walk"


class Panda(WalkingAnimal):
    name = "Panda"
```

and:

```python
class SlitheringAnimal:
    def move(self) -> str:
        return "Slither"


class Python(SlitheringAnimal):
    name = "Python"
```

`Panda` gets walking behaviour from `WalkingAnimal`, while `Python` gets
slithering behaviour from `SlitheringAnimal`.

Python allows this perfectly well.

The problem is not syntax. The problem is what the hierarchy says about the
domain.

It says that a panda **is a walking animal** and a python **is a slithering
animal**, making movement part of their fundamental type hierarchy.

Movement is better understood here as a capability.

It can vary independently of many other characteristics of an animal, and an
animal may have more than one form of movement.

Inheritance has therefore been chosen mainly because it provides convenient
behaviour reuse.

That is a warning sign.

---

## Code reuse is not enough to justify inheritance

Inheritance can reuse implementation, but implementation reuse alone does not
establish a meaningful subtype relationship.

Before introducing a subclass, ask whether the subtype genuinely represents a
specialised form of the base type.

A useful test is:

> Should code written for the base type be able to receive the subtype without
> needing special knowledge about which subtype it received?

If the answer is no, the inheritance relationship deserves closer examination.

There are other ways to reuse or share behaviour, including composition and
ordinary functions.

Choosing inheritance creates a stronger relationship between types than simply
sharing some implementation.

---

## Why movement is a poor hierarchy here

Suppose the zoo later needs to represent animals that:

- walk and swim;
- climb and walk;
- change movement according to circumstances;
- require movement behaviour to be configured independently.

A movement-based inheritance hierarchy quickly becomes awkward.

Should an animal inherit from both `WalkingAnimal` and `SwimmingAnimal`?

What happens when another independent capability also varies?

The model begins trying to encode combinations of capabilities into the class
hierarchy.

The [Composition exhibit](../composition/README.md) demonstrates the more
flexible alternative used elsewhere in the zoo:

```text
Animal
  |
  has a
  |
Movement
```

An `Animal` can collaborate with a `Movement` object rather than being defined
by a movement superclass.

This is an important distinction:

> Inheritance models a type relationship. Composition assembles collaborating
> behaviour.

---

## 2. Inheritance used for meaningful specialisation

The second example begins with an abstract base class:

```python
@dataclass(slots=True, frozen=True)
class Animal(ABC):
    name: str

    @abstractmethod
    def feeding_instructions(self) -> str: ...
```

The zoo has a concrete software requirement:

> Every supported animal must provide feeding instructions appropriate to that
> animal type.

The subclasses implement that shared contract:

```python
class Python(Animal):
    def feeding_instructions(self) -> str:
        return "Provide an appropriately sized whole-prey diet."


class Panda(Animal):
    def feeding_instructions(self) -> str:
        return "Provide a bamboo-dominated diet."
```

`Lion` and `Elephant` do the same for their own feeding requirements.

The inheritance hierarchy now represents something the application actually
needs.

Each concrete class is a specialised `Animal` that honours the behaviour
required by `Animal`.

---

## The important idea: substitutability

Consider:

```python
def describe_animal(animal: Animal) -> str:
    return animal.describe()
```

This function does not need:

```python
if isinstance(animal, Python):
    ...
elif isinstance(animal, Panda):
    ...
```

It works with the abstraction.

A `Python`, `Panda`, `Lion`, or `Elephant` can be supplied wherever this code
expects an `Animal`.

Each subtype preserves the expectations established by the base type while
providing its specialised feeding behaviour.

That property is more important than the fact that the subclasses happen to
inherit some code.

The tests make this design intention executable in
[tests/test_appropriate_inheritance_example.py](../../tests/test_appropriate_inheritance_example.py).

In particular, `test_animal_subtypes_are_substitutable()` passes each concrete
animal through code written against the `Animal` abstraction.

---

## Inheritance is about contracts as well as implementation

A base class can provide shared implementation:

```python
def describe(self) -> str:
    return f"{self.name}: {self.feeding_instructions()}"
```

That reuse is useful, but it is not the main reason for the hierarchy.

The more important feature is the contract:

```python
@abstractmethod
def feeding_instructions(self) -> str: ...
```

Every concrete `Animal` must supply that behaviour.

Code working with `Animal` can therefore depend on the operation without
depending on a particular concrete animal type.

The shared implementation and the shared contract reinforce the same domain
abstraction.

---

## Biological taxonomy does not automatically become software inheritance

The zoo theme makes this distinction especially important.

A python, panda, lion, and elephant occupy different positions in biological
taxonomy.

That fact alone does **not** mean the software should contain a large hierarchy
such as:

```text
Animal
├── Mammal
│   ├── Carnivore
│   │   └── Lion
│   └── ...
└── Reptile
    └── ...
```

A software model exists to support software requirements, not to reproduce
every classification that exists in the real world.

If the application only needs to store taxonomy, values such as class, order,
family, genus, and species can simply be data.

The [Domain Modelling exhibit](../domain_modelling/README.md) demonstrates this
directly.

Introduce a subtype when the distinction matters to the behaviour or rules of
the software.

Do not introduce one merely because the real world provides a classification
you could model.

---

## Inheritance and domain modelling

These two topics are closely related.

Domain modelling asks:

> Is this difference important enough to deserve its own domain type?

Inheritance adds another question:

> If distinct types are justified, do they form a meaningful subtype
> relationship?

Those are separate decisions.

Two concepts can deserve separate classes without either being a subtype of the
other.

Likewise, two objects can share behaviour without inheritance being the right
way to share it.

---

## Inheritance and composition

A common OO guideline is:

> Favour composition over inheritance.

That does not mean inheritance is bad.

It means inheritance should not be the automatic mechanism for obtaining
behaviour from another class.

Use inheritance when the subtype relationship itself is meaningful.

Use composition when an object needs a capability or collaborator that can vary
independently.

In this zoo:

- species-specific feeding behaviour can justify specialised `Animal` types
  when the application requires those types;
- movement is demonstrated as a separately varying capability in the
  [Composition exhibit](../composition/README.md).

The appropriate choice follows the domain requirement rather than a blanket
rule.

---

## Inheritance and abstract base classes

The appropriate example uses `ABC` and `@abstractmethod`.

This is **nominal typing**: a concrete animal explicitly inherits from `Animal`
and becomes part of that declared hierarchy.

The abstract method also prevents an incomplete `Animal` from being
instantiated without the required feeding behaviour.

This is different from the structural typing demonstrated by the
[Factory exhibit](../factory/README.md), where a `Protocol` allows an object to
satisfy a contract because it has the required shape rather than because it
inherits from a particular base class.

Neither technique is universally better.

They communicate different relationships.

---

## What about the Liskov Substitution Principle?

The substitutability idea is commonly formalised as the **Liskov Substitution
Principle (LSP)**.

In practical terms, a subtype should be usable where its base type is expected
without breaking the expectations established by that base type.

This is deeper than simply passing an `isinstance()` check.

A subclass that technically inherits from a base class but changes the meaning
of its operations, rejects valid uses expected by the base class, or otherwise
breaks the base contract may be a poor subtype.

For this starter exhibit, the important habit is straightforward:

> When creating a subclass, ask whether callers can genuinely treat it as the
> base type.

More advanced inheritance hierarchies can require much more careful reasoning
about contracts, preconditions, postconditions, and invariants.

---

## Beyond the zoo

The same decision appears in application and business software.

Suppose several payment types must all support:

```python
payment.authorise()
```

If `CardPayment`, `BankTransferPayment`, and other payment types genuinely
participate in the same payment contract and callers can work with them through
that abstraction, inheritance may be appropriate.

By contrast, suppose several unrelated objects need to send email.

Creating an `EmailSendingObject` superclass merely so they can inherit
`send_email()` would probably encode the wrong type relationship.

Email delivery is more naturally a collaborator or service.

The question remains:

> Is this a genuine subtype relationship, or am I using inheritance because I
> want some code that another class already has?

---

## Choosing inheritance

Before creating a subclass, ask:

1. Does the subclass genuinely represent a specialised form of the base type?
2. Is there a meaningful shared contract?
3. Can callers use the subtype wherever they expect the base type?
4. Does the subtype preserve the expectations and rules of the base type?
5. Is the distinction required by the software domain rather than merely by
   real-world classification?
6. Am I choosing inheritance mainly to reuse implementation?
7. Would composition represent independently varying behaviour more clearly?

Inheritance is strongest when the answers describe a meaningful type
relationship.

If the main justification is "these classes share some code," consider another
design.

---

## Related concepts

See the [Object-Oriented Glossary](../GLOSSARY.md) for:

- [Abstract Base Class (ABC)](../GLOSSARY.md#abstract-base-class-abc)
- [Abstraction](../GLOSSARY.md#abstraction)
- [Composition](../GLOSSARY.md#composition)
- [Contract](../GLOSSARY.md#contract)
- [Domain Modelling](../GLOSSARY.md#domain-modelling)
- [Inheritance](../GLOSSARY.md#inheritance)
- [Interface](../GLOSSARY.md#interface)
- [Nominal Typing](../GLOSSARY.md#nominal-typing)
- [Polymorphism](../GLOSSARY.md#polymorphism)
- [Responsibility](../GLOSSARY.md#responsibility)

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/inheritance/README.md_ | _4 September 2026_ | _lizc-au_ |
