# Responsibilities & Collaboration

Object-oriented design is not only about creating classes. It is also about
deciding which object should own which work.

The central question in this exhibit is:

> When several operations involve the same domain object, should that object
> perform all of them itself, or should some responsibilities belong elsewhere?

The examples deliberately produce the same useful result. The difference is
where the responsibilities live.

---

## 1. When one object owns too much

[`overloaded_animal_example.py`](overloaded_animal_example.py) gives one
`Animal` class several jobs:

- store animal data
- decide feeding guidance
- calculate routine care dates
- format keeper reports

None of those methods is unreasonable on its own. The design pressure appears
because they have different reasons to change.

For example:

- feeding policy may change because husbandry guidance changes
- care scheduling may change because operational rules change
- report formatting may change because users want a different presentation
- animal data may change because the domain model changes

If all of those concerns are owned by `Animal`, unrelated changes repeatedly
touch the same class.

This is a cohesion problem. A highly cohesive object contains responsibilities
that belong closely together. As unrelated responsibilities accumulate,
cohesion usually decreases.

The overloaded example is intentionally plausible rather than exaggerated.
Real systems often become difficult gradually because a convenient class keeps
acquiring one more reasonable-looking method.

---

## 2. Redistributing responsibilities

[`collaborating_objects_example.py`](collaborating_objects_example.py) assigns
the work to more focused owners:

| Responsibility | Owner |
| --- | --- |
| Animal identity and domain data | `Animal` |
| Feeding guidance | `FeedingGuide` |
| Routine care scheduling | `CareSchedule` |
| Keeper-facing presentation | `KeeperReport` |

`KeeperReport` still needs feeding and scheduling information, but it does not
reimplement those rules. It asks the objects that own those responsibilities.

That interaction is collaboration.

`KeeperReport` delegates feeding guidance to `FeedingGuide` and care-date
calculation to `CareSchedule`, then combines their results into the report it
owns.

The result is not less connected. The objects still work together. The
difference is that each collaboration crosses a clearer responsibility
boundary.

---

## The Single Responsibility Principle

The Single Responsibility Principle is often shortened to:

> A class should have one reason to change.

That does **not** mean:

- one method per class
- one field per class
- every operation must become its own object
- every possible future concern should be separated immediately

The useful question is whether the responsibilities grouped together belong to
the same conceptual job and tend to change for the same reasons.

In this example, animal identity, feeding policy, care scheduling, and report
formatting have sufficiently different change drivers to make the separation
easy to justify.

In a much smaller application, keeping some of those responsibilities together
could still be perfectly reasonable.

---

## Avoiding premature micro-classes

Responsibility design requires judgement.

A useful approach is:

1. Identify the responsibilities required by the current use cases.
2. Put obvious responsibilities with the objects that naturally own them.
3. Keep the design simple while those boundaries remain coherent.
4. Reassess when new requirements cause unrelated work to accumulate.
5. Split responsibilities when clearer ownership improves the design.

The goal is neither one class that does everything nor dozens of tiny classes
created in anticipation of requirements that may never exist.

Good boundaries are clear, justified, and appropriate to the current
application.

---

## Why are the collaborator classes not dataclasses?

`Animal` uses:

```python
@dataclass(slots=True, frozen=True)
```
because it stores domain data.

`FeedingGuide`, `CareSchedule`, and `KeeperReport` currently store no instance
data. They own behaviour, so ordinary classes are sufficient.

If a responsibility later gained meaningful state or configuration, a
dataclass might become appropriate. For example, a configurable
`CareSchedule` could eventually store an interval or scheduling policy.

The choice of class structure should follow the responsibility and state being
modelled rather than applying the same machinery to every object.

---

## Could these stateless collaborators be functions?

Yes.

For a small program, functions such as:

```python
feeding_instructions_for(animal)
next_care_date_for(animal)
format_keeper_report(animal)
```

could be a simpler design.

The collaborating example uses classes because the purpose of this exhibit is
to make object responsibility, delegation, and collaboration visible.

A class becomes more compelling when a responsibility has characteristics such
as:

- related operations that belong together
- configuration or state
- multiple interchangeable implementations
- an interface that other objects depend on
- behaviour that forms a meaningful concept in the domain or application

Object-oriented design does not require every useful function to become a
class.

---

## Why only one animal?

Only one animal is used because animal type is not the design question here.

Repeating Python, Panda, Lion, and Elephant would add more construction code
without improving the responsibility comparison. The examples therefore use a
single Lion so attention remains on ownership and collaboration.

Other exhibits explore the differences between animal types directly.

---

## Relationship to Composition

Composition and responsibility design overlap, but they ask different
questions.

Composition asks:

> How can an object obtain behaviour by working with other objects?

Responsibilities & Collaboration asks:

> Which object should own each piece of work in the first place?

The collaborating example uses composition-like collaboration, but the main
lesson is responsibility ownership rather than the mechanics of composing
behaviour.

See the [Composition examples](../composition/README.md) for that topic in
detail.

---

## Relationship to Domain Modelling

Domain Modelling asks which concepts and distinctions deserve representation in
the software.

Responsibilities & Collaboration asks what those concepts should own once they
exist.

For example, introducing an `Animal` type is a modelling decision. Deciding
whether `Animal` should also own feeding policy, scheduling, and report
formatting is a responsibility decision.

See the [Domain Modelling examples](../domain_modelling/README.md) for the
earlier part of that design process.

---

## Beyond the zoo

The same pressure appears frequently in business software.

An `Order`, `Document`, or `InsuranceClaim` might begin as a straightforward
domain object and gradually acquire:

- validation logic
- approval rules
- persistence operations
- notifications
- scheduling
- reporting
- presentation formatting

Every operation may involve the domain object, but that does not make the domain
object the appropriate owner of every operation.

A more cohesive design may let the domain object retain its own data and
domain-specific rules while collaborating with focused components for concerns
such as validation, scheduling, notifications, or reporting.

The important question is not:

> Can this class perform the work?

It is:

> Is this class the appropriate owner of the work?

---

## Comparing the two designs

| Design question | Overloaded `Animal` | Collaborating objects |
| --- | --- | --- |
| Stores animal data | `Animal` | `Animal` |
| Owns feeding policy | `Animal` | `FeedingGuide` |
| Owns care scheduling | `Animal` | `CareSchedule` |
| Owns report formatting | `Animal` | `KeeperReport` |
| Number of reasons `Animal` may change | Several | Mostly animal-domain concerns |
| Collaboration visible | Minimal | Explicit |
| Appropriate for a tiny program | Possibly | Possibly more structure than needed |
| Easier to evolve when concerns diverge | Usually less so | Usually more so |

The collaborating design is not automatically superior in every program.

Its advantage appears when the separated responsibilities are real,
independently changing concerns. If those distinctions do not yet matter, extra
objects can create complexity without delivering useful separation.

---

## Choosing appropriate responsibility boundaries

When deciding where work belongs, ask:

- What responsibility is this code actually performing?
- Which object has the information and rules needed to own it coherently?
- Does this responsibility change for the same reasons as the surrounding code?
- Is the class accumulating unrelated reasons to change?
- Would delegation make ownership clearer?
- Is a new object justified by current requirements?
- Would a simple function be clearer than another class?
- Am I improving cohesion, or merely moving code around?

Responsibility boundaries are design decisions, not mechanical rules.

---

## Related concepts

The [Object-Oriented Python Glossary](../GLOSSARY.md) explains terminology used
throughout this example, including: Cohesion, Collaboration, Composition,
Delegation, Dependency, Domain Modelling, Responsibility, Single Responsibility
Principle (SRP), and State.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _object_oriented/responsibilities/README.md_ | _4 September 2026_ | _lizc-au_ |
