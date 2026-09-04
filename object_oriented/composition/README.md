# Composition - Building Objects from Behaviours

Composition builds objects by combining them with other objects that provide
part of their behaviour.

Instead of asking:

> What specialised class should this object inherit from?

Composition often asks:

> What behaviours or collaborators should this object have?

This example uses movement to demonstrate that distinction.

A general `Animal` has a [Movement](../GLOSSARY.md#behaviour) collaborator:

```python
@dataclass(slots=True, frozen=True)
class Animal:
    species: str
    movement: Movement
```

The animal does not need to inherit from `WalkingAnimal`, `SlitheringAnimal`,
or some increasingly specialised hierarchy.

It delegates movement description to the object it contains.

---

## Has-a rather than is-a

[Inheritance](../GLOSSARY.md#inheritance) commonly represents an **is-a**
relationship.

For example:

```text
Lion is an Animal
```

[Composition](../GLOSSARY.md#composition) represents a **has-a** relationship:

```text
Animal has a Movement
```

The distinction matters because behaviours often vary independently from the
objects using them.

Python, Panda, Lion, and Elephant do not need separate inheritance branches
merely because they move differently.

---

## The Movement contract

`behaviours/movement.py` defines a small
[Protocol](../GLOSSARY.md#protocol):

```python
class Movement(Protocol):
    def description(self) -> str: ...
```

Concrete movement behaviours provide that contract:

```python
class Slither:
    def description(self) -> str:
        return "slithers"


class Walk:
    def description(self) -> str:
        return "walks"
```

The general `Animal` depends on `Movement`, not on `Slither` or `Walk`
specifically.

That reduces [coupling](../GLOSSARY.md#coupling) between the animal and the
particular movement implementation.

This terminal example exposes only a textual description because that is all
the demonstration requires. In larger software, a composed behaviour might
perform calculations, update state, issue commands, access another service, or
drive an animation.

---

## Composition does not decide who selects the behaviour

This example set demonstrates an important distinction:

> **Composition determines how objects collaborate. It does not, by itself,
> determine who should choose the objects being composed.**

The same Composition technique can therefore be used with different ownership
models.

The three runnable examples deliberately produce the same animal behaviour
while placing the selection decision in three different locations.

---

## 1. Client-selected composition

See `client_selected_example.py`.

The client explicitly supplies the behaviour:

```python
Animal(species="Python", movement=Slither())
```

The client therefore knows:

```text
Python -> Slither
```

### When this is useful

Client-selected composition is appropriate when selecting the behaviour is a
genuine choice available to the caller.

For example, a reporting component might support:

```python
Report(formatter=PdfFormatter())
Report(formatter=CsvFormatter())
```

PDF versus CSV is genuinely something the caller may need to choose.

Other examples include configurable storage providers, notification channels,
export formats, test doubles, algorithms, or behaviours selected from
application settings.

### Strength

The dependency is explicit and highly configurable.

### Trade-off

The client must know which collaborator to supply.

That is undesirable when the relationship is an established domain rule rather
than a choice the client should make.

Run:

```text
python -m object_oriented.composition.client_selected_example
```

Output:

```text
Client-selected composition:
A python slithers.
A panda walks.
A lion walks.
An elephant walks.
```

---

## 2. Construction-selected composition

See `construction_selected_example.py`.

Here the ordinary client requests an animal:

```python
python = create_animal("Python")
```

The construction boundary knows:

```text
Python -> Slither
```

The returned animal is still composed with a separate `Movement` object. The
Composition mechanism has not changed.

Only ownership of the **selection decision** has changed.

### When this is useful

Construction-selected composition is appropriate when callers should receive a
correctly assembled object without needing to understand its internal
dependencies.

For example, a document-processing application might create an invoice
processor with the validator required for invoices. Ordinary client code needs
an invoice processor; it should not necessarily need to know which validator
must be supplied.

A [Factory](../GLOSSARY.md#factory) is one possible construction boundary.

This example deliberately uses a small `create_animal()` function so the lesson
remains focused on Composition rather than repeating the complete Factory
Pattern example.

### Strength

Construction knowledge is centralised and kept away from ordinary client code.

### Trade-off

The construction boundary must now own and maintain the mapping between
requests and collaborators.

Run:

```text
python -m object_oriented.composition.construction_selected_example
```

Output:

```text
Construction-selected composition:
A python slithers.
A panda walks.
A lion walks.
An elephant walks.
```

---

## 3. Domain-type-selected composition

See `domain_type_selected_example.py`.

Here a concrete domain type owns the relationship:

```python
python = Python().create_animal()
```

`Python` knows that a Python should be composed with `Slither`, but it still
returns the same shared `Animal` model used by the other examples.

The domain type therefore owns the rule: `Python` -> `Slither`
while the finished behaviour still flows through the common
`Animal.describe_movement()` implementation.

Client code neither selects nor needs to know about the movement collaborator.

This is still Composition. The resulting `Animal` has a separate `Movement`
object and delegates movement behaviour to that collaborator.

### When this is useful

Domain-type-selected composition is useful when the collaborator represents an
intrinsic rule of that particular domain type rather than something callers
should configure.

For example, if a `BankTransferPayment` must always use a particular bank
transfer validation policy, the domain type could own that relationship while
delegating the validation work to a separate validator object.

### Strength

The rule stays close to the domain type it describes, and callers cannot
accidentally construct the type with an inappropriate collaborator through its
normal constructor.

### Trade-off

The design is less configurable.

If the same domain type legitimately needs different behaviours in different
situations, hard-wiring one selection into the type can become restrictive.

Run:

```text
python -m object_oriented.composition.domain_type_selected_example
```

Output:

```text
Domain-type-selected composition:
A python slithers.
A panda walks.
A lion walks.
An elephant walks.
```

---

## Comparing the three approaches

All three examples use Composition.

The difference is **who knows which pieces belong together**:

| Approach | Who selects the movement? | Best fit |
| --- | --- | --- |
| Client-selected | Ordinary client code | The behaviour is genuinely configurable |
| Construction-selected | Construction boundary | Clients should receive correctly assembled objects |
| Domain-type-selected | Concrete domain type | The relationship is an intrinsic rule of that type |

None of these is universally the "correct" form of Composition.

The correct placement depends on the responsibility being modelled.

That is an important architectural question in its own right.

---

## Composition and dependency injection

The client-selected example also demonstrates
[dependency](../GLOSSARY.md#dependency) injection.

The movement dependency is supplied from outside:

```python
Animal(species="Python", movement=Slither())
```

Dependency injection and Composition are related, but they are not synonyms.

**Composition** describes building an object from collaborating parts.

**Dependency injection** describes supplying a dependency to an object from
outside rather than having the object construct that dependency itself.

The domain-type-selected example demonstrates why the distinction matters: it
still uses Composition, even though ordinary client code does not inject the
movement.

---

## Composition versus inheritance

Composition and inheritance are not enemies, and "always favour composition"
is too simplistic.

Use inheritance when an **is-a** relationship is meaningful and the hierarchy
provides genuine value.

Use Composition when a **has-a** relationship better describes the design,
particularly when behaviours:

- vary independently;
- can be shared by unrelated types;
- need to be replaceable;
- should have their own focused responsibility; or
- would otherwise cause an inheritance hierarchy to multiply combinations.

The question is not:

> Which OO technique is better?

The better question is:

> Which relationship accurately represents this responsibility?

---

## Patterns can work together

Object-oriented techniques and design patterns are not mutually exclusive.

Production software commonly combines them because each addresses a different
design concern.

In these examples:

- **Composition** determines how an animal collaborates with a movement object.
- **Factory** can determine how a correctly composed object is constructed.
- **Domain Modelling** determines whether distinctions such as Python, Panda,
  Lion, and Elephant should be data values or separate domain types.
- **Responsibilities and Collaboration** helps determine which component should
  own each decision.

A program therefore does not have to be "a Factory design" or "a Composition
design."

Different patterns and techniques can operate at different boundaries of the
same system.

As the Object-Oriented examples develop, look for places where several
techniques cooperate rather than assuming that one pattern must be selected in
isolation.

---

## When not to use Composition

Composition introduces another object and another relationship that developers
must understand.

Do not extract every tiny piece of behaviour into its own class merely because
Composition is considered good OO design.

If behaviour is simple, fixed, cohesive with the object, and has no independent
reason to vary, keeping it directly on the object may be clearer.

The goal is not to maximise the number of collaborating objects.

The goal is to place responsibilities where they make the software easier to
understand, change, test, and maintain.

---

## Related concepts

The [Object-Oriented Python Glossary](../GLOSSARY.md) explains terminology used
throughout this example, including:

- [Behaviour](../GLOSSARY.md#behaviour)
- [Composition](../GLOSSARY.md#composition)
- [Coupling](../GLOSSARY.md#coupling)
- [Dependency](../GLOSSARY.md#dependency)
- [Dependency Injection](../GLOSSARY.md#dependency-injection)
- [Factory](../GLOSSARY.md#factory)
- [Inheritance](../GLOSSARY.md#inheritance)
- [Protocol](../GLOSSARY.md#protocol)
- [Responsibility](../GLOSSARY.md#responsibility)
- [Structural Typing](../GLOSSARY.md#structural-typing)

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/composition/README.md_ | _4 September 2026_ | _lizc-au_ |

