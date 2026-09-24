# Responsibilities & Collaboration

Object-oriented design asks which component should own each piece of work. These two examples produce the same keeper report but place the work in different objects.

## Compare the Designs

| Responsibility | [Overloaded Animal](./overloaded_animal_example.py) | [Collaborating Objects](./collaborating_objects_example.py) |
| :--- | :--- | :--- |
| Animal identity and data | `Animal` | `Animal` |
| Feeding guidance | `Animal` | `FeedingGuide` |
| Routine care scheduling | `Animal` | `CareSchedule` |
| Keeper-facing report | `Animal` | `KeeperReport` |
| How the report gets its information | One class performs every step | `KeeperReport` asks focused collaborators |

Run both from the repository root:

| Order | Command |
| :--- | :--- |
| 1 | `python -m object_oriented.responsibilities.overloaded_animal_example` |
| 2 | `python -m object_oriented.responsibilities.collaborating_objects_example` |

The first design is intentionally plausible: each new method seems reasonable on its own. The pressure appears when animal data, feeding policy, care scheduling, and presentation start changing for different reasons.

## What Collaboration Changes

`KeeperReport` delegates feeding guidance to `FeedingGuide` and date calculation to `CareSchedule`. It then combines their results into the report that it owns.

| Term | Meaning in this example |
| :--- | :--- |
| Responsibility | The work a component owns. |
| Collaboration | Components working together across their responsibility boundaries. |
| Delegation | One component asking another to perform a specific piece of work. |
| Cohesion | How closely a component's responsibilities fit together. |

The collaborating design still has connections between objects. Its advantage is clearer ownership when those concerns genuinely evolve independently.

<details>
<summary>What the Single Responsibility Principle means here</summary>

The Single Responsibility Principle (SRP) is often described as giving a class one reason to change. It does not mean one method or field per class.

| Change | Likely owner in the collaborating design |
| :--- | :--- |
| Animal-domain information | `Animal` |
| Husbandry or feeding guidance | `FeedingGuide` |
| Operational care dates | `CareSchedule` |
| Report presentation | `KeeperReport` |

Several methods can support one coherent job. In a tiny application, combining some of these responsibilities may still be simpler than introducing collaborators prematurely.

</details>

<details>
<summary>Why use classes rather than functions?</summary>

Functions such as `feeding_instructions_for(animal)` and `format_keeper_report(animal)` could be a clear choice in a small program. This exhibit uses classes to make ownership, delegation, and collaboration visible.

A class becomes more useful when a responsibility has related operations, configuration, state, interchangeable implementations, or an interface others depend on. `Animal` is a frozen, slotted dataclass because it stores domain data; the stateless collaborators need no dataclass machinery today.

Only one Lion appears because species variation is not this exhibit's design question. [Domain Modelling](../domain_modelling/README.md) explores when those differences deserve separate types.

</details>

<details>
<summary>How to choose a boundary</summary>

| Question | What to consider |
| :--- | :--- |
| What job is the code doing? | Name the responsibility before moving methods. |
| Why might it change? | Unrelated change drivers may point to different owners. |
| Which component has the relevant rules? | Keep domain rules with a coherent owner. |
| Is another object justified now? | Avoid creating tiny classes for hypothetical future needs. |
| Would a function be clearer? | Not every useful operation needs a class. |
| Does delegation help? | Make ownership clearer rather than merely moving code around. |

The same pressure appears when an `Order`, `Document`, or `InsuranceClaim` gradually acquires approval, storage, notification, scheduling, and reporting work. Each operation may involve that domain object without belonging inside it.

[Composition](../composition/README.md) explores how objects obtain behaviour from collaborators. This exhibit focuses on deciding which collaborator should own the behaviour in the first place.

</details>

The [Object-Oriented Python Glossary](../GLOSSARY.md) defines [cohesion](../GLOSSARY.md#cohesion), [collaboration](../GLOSSARY.md#collaboration), [delegation](../GLOSSARY.md#delegation), and [SRP](../GLOSSARY.md#single-responsibility-principle-srp).

---

[Return to Object-Oriented Python](../README.md) for the next design question.

[Return to the Zoo map](../../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
