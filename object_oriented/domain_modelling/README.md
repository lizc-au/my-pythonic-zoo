# Domain Modelling

Domain modelling is the process of deciding which concepts in a problem
deserve representation in software, what information they own, and what
responsibilities belong to them.

This exhibit focuses on one deceptively important object-oriented design
question:

> **When is a difference important enough to deserve its own domain type,
> rather than being represented as data on a more general object?**

The two examples deliberately model the same four animals in different ways.
The first keeps their differences as data. The second introduces distinct
domain types only after a new behavioural requirement gives those types a
meaningful responsibility.

Movement and sounds are deliberately omitted from these examples. Those
behaviours are explored elsewhere in the Object-Oriented Zoo, and repeating
them here would add clutter without improving the domain-modelling lesson.
Keeping them out allows the examples to focus on one question: whether a
domain difference should be represented as data or as a distinct type with
its own responsibility.

---

## 1. When differences are data

[`data_model_example.py`](data_model_example.py) represents a Ball Python,
Giant Panda, Lion, and African Savanna Elephant using the same `Animal` type.

The animals have different:

- common names
- taxonomic classifications
- species
- diets

Those differences matter to the domain, but they are currently only facts that
the application needs to record. Every animal has the same responsibilities
and uses the same `describe()` behaviour.

Creating `BallPython`, `GiantPanda`, `Lion`, and `AfricanSavannaElephant`
classes at this point would therefore add types without giving those types
anything meaningfully different to do.

This illustrates an important distinction:

> **Different data values do not, by themselves, justify different software
> types.**

The biological taxonomy is itself a hierarchy, but that does not mean the
software needs a matching inheritance hierarchy. Phylum, class, order, family,
genus, and species remain data because recording them is all this application
currently requires.

### Why `slots=True` and `frozen=True`?

The first example defines `Animal` using:

```python
@dataclass(slots=True, frozen=True)
class Animal:
```

These options reinforce the particular model rather than define domain
modelling itself.

`slots=True` prevents arbitrary new attributes from being added to an
`Animal`. This helps keep the model closed to accidental attributes, including
ones created by misspelling an existing field name.

`frozen=True` prevents the recorded values from being reassigned after the
object has been created. That suits this example because facts such as an
animal's species and taxonomic classification are being treated as established
identity data rather than mutable application state.

A different domain model could legitimately require mutable objects or
additional attributes. Neither `slots=True` nor `frozen=True` is required in
order to practise domain modelling.

---

## 2. When behaviour creates a meaningful domain type

[`domain_types_example.py`](domain_types_example.py) starts with the same
animals and taxonomy, but introduces a new requirement:

> **The zoo must provide feeding instructions appropriate to each animal
> type.**

The modelling pressure has now changed. Feeding instructions are not merely
different recorded values in this example; they are behaviour that each kind
of animal is responsible for providing.

The model therefore introduces four explicit domain types:

- `BallPython`
- `GiantPanda`
- `Lion`
- `AfricanSavannaElephant`

Each is an `Animal`, inherits the shared `describe()` behaviour, and provides
its own implementation of `feeding_instructions()`.

The taxonomy still remains data. The new subclasses exist because the
application has acquired a behavioural requirement that gives the individual
animal types a meaningful responsibility, not simply because biology gives
the animals different names or classifications.

### Why use an abstract base class?

The second example defines `Animal` using `ABC` and marks
`feeding_instructions()` with `@abstractmethod`.

`ABC` establishes an explicit inheritance relationship: each concrete animal
type is intentionally modelled as an `Animal`.

`@abstractmethod` marks behaviour that every concrete `Animal` subtype must
provide. A subtype that does not implement `feeding_instructions()` remains
abstract and cannot be instantiated. Attempting to instantiate it raises
`TypeError`.

This differs from the Factory exhibit, where a `Protocol` is used for
structural typing. A protocol asks whether an object provides the required
interface, regardless of its inheritance hierarchy. An abstract base class is
useful here because the explicit **is-a** relationship is itself part of the
domain model.

Neither approach is universally more object-oriented or more correct. The
choice depends on what relationship the software is trying to express.

### Could feeding become composition instead?

Yes. The second example deliberately keeps feeding behaviour on the concrete
animal types because that makes the domain-modelling decision easy to see.

If feeding rules later became complex, independently configurable, reusable
across multiple animal types, or changeable at runtime, a separate feeding
object could become a better owner of that behaviour. The animal would then
collaborate with that object rather than implementing every feeding rule
itself.

That would move the design toward composition, as demonstrated in the
[Composition exhibit](../composition/README.md).

The important lesson is that introducing a domain type does not commit the
design permanently to inheritance. Responsibilities can move as the domain and
requirements become better understood.

---

## Beyond the zoo

The same modelling decision appears frequently in business applications.

A document system might initially represent invoices, insurance claims, and
correspondence using one `Document` type. If their differences are limited to
data such as document category, status, owner, or retention category, separate
Python classes may add little value.

Later, the requirements might introduce genuinely different responsibilities.
Invoices may require payment validation, insurance claims may require
assessment and settlement rules, and correspondence may require delivery or
retention processing. At that point, distinct domain types can become useful
because the concepts now have meaningful behaviour to own.

The same principle applies:

> **Discover the domain broadly, model it incrementally, and put each
> difference where its responsibility actually belongs.**

---

## Comparing the two models

| Question | Data model | Domain types |
| --- | --- | --- |
| Are the animals different? | Yes | Yes |
| Are taxonomy and diet important? | Yes | Yes |
| Do different values alone create subclasses? | No | No |
| Is `describe()` shared? | Yes | Yes |
| Is type-specific behaviour required? | No | Yes |
| Are separate animal types justified? | Not yet | Yes |
| What changed the design? | Nothing behavioural | Feeding responsibility |

The second model is not automatically "better" than the first. Each model is
appropriate for a different set of requirements. The point of domain modelling
is to make the simplest useful distinction that the current domain actually
requires.

---

## Choosing the appropriate model

Object-oriented design rarely provides one universally best representation of
a domain. A design that is clear and appropriate for today's requirements can
become awkward when those requirements change.

Avoid introducing subclasses merely because real-world things have different
names or classifications. Equally, avoid forcing increasingly different rules
and responsibilities into one general type simply to avoid inheritance.

Instead, ask:

- Is this difference only information that needs to be recorded?
- Does this concept have behaviour or rules that belong specifically to it?
- Is that behaviour shared, type-specific, or independently variable?
- Would introducing another type make the responsibility clearer?
- Has the requirement actually justified the additional abstraction?

The goal is not to predict every future requirement. It is to model the domain
clearly enough for the requirements that exist now, while leaving the design
understandable enough to change later.

---

## Related concepts

The [Object-Oriented Python Glossary](../GLOSSARY.md) explains terminology used
throughout this example, including:

- [Domain Modelling](../GLOSSARY.md#domain-modelling)
- [Abstract Base Class (ABC)](../GLOSSARY.md#abstract-base-class-abc)
- [Behaviour](../GLOSSARY.md#behaviour)
- [Class](../GLOSSARY.md#class)
- [Composition](../GLOSSARY.md#composition)
- [Concrete Class](../GLOSSARY.md#concrete-class)
- [Inheritance](../GLOSSARY.md#inheritance)
- [Nominal Typing](../GLOSSARY.md#nominal-typing)
- [Protocol](../GLOSSARY.md#protocol)
- [Responsibility](../GLOSSARY.md#responsibility)
- [State](../GLOSSARY.md#state)
- [Structural Typing](../GLOSSARY.md#structural-typing)

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/domain_modelling/README.md_ | _4 September 2026_ | _lizc-au_ |
