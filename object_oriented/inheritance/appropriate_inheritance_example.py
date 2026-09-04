"""
appropriate_inheritance_example.py

Show inheritance used for meaningful specialisation of a shared abstraction.

Inheritance is appropriate when a subtype genuinely represents a specialised
form of its base type and honours the contract expected from that base type.

In this example, the zoo has a requirement to produce species-appropriate
feeding instructions. Every supported animal is an ``Animal`` and must provide
that behaviour, while shared animal data and reporting behaviour belong to the
base class.

The concrete animal classes therefore specialise a meaningful domain
abstraction rather than inheriting merely to reuse convenient code.

The important property is substitutability. ``describe_animal()`` works with an
``Animal`` without needing to know whether it receives a ``Python``, ``Panda``,
``Lion``, or ``Elephant``. Each subclass honours the same contract while
providing its own implementation of ``feeding_instructions()``.

Biological classification alone would not justify this hierarchy. The
subclasses exist because the software has a behavioural requirement that varies
meaningfully by animal type. If species differences were only descriptive data,
the data-oriented design in ``domain_modelling/data_model_example.py`` would be
simpler and more appropriate.

Likewise, independently varying capabilities such as movement should generally
not be forced into this hierarchy. The [Composition examples]
(../composition/README.md) demonstrate how those behaviours can instead belong
to collaborating objects.

A similar design can appear in business software when several specialised
document, payment, or notification types must all honour a common application
contract while implementing one required operation differently.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Animal(ABC):
    """Define the shared state and behavioural contract for zoo animals."""

    name: str

    @abstractmethod
    def feeding_instructions(self) -> str:
        """Return feeding instructions appropriate to this animal."""

    def describe(self) -> str:
        """Describe the animal through the shared ``Animal`` interface."""
        return f"{self.name}: {self.feeding_instructions()}"


class Python(Animal):
    """Represent a python with species-appropriate feeding behaviour."""

    def feeding_instructions(self) -> str:
        """Return feeding instructions for a python."""
        return "Provide an appropriately sized whole-prey diet."


class Panda(Animal):
    """Represent a giant panda with species-appropriate feeding behaviour."""

    def feeding_instructions(self) -> str:
        """Return feeding instructions for a giant panda."""
        return "Provide a bamboo-dominated diet."


class Lion(Animal):
    """Represent a lion with species-appropriate feeding behaviour."""

    def feeding_instructions(self) -> str:
        """Return feeding instructions for a lion."""
        return "Provide a nutritionally complete carnivore diet."


class Elephant(Animal):
    """Represent an elephant with species-appropriate feeding behaviour."""

    def feeding_instructions(self) -> str:
        """Return feeding instructions for an elephant."""
        return "Provide a high-fibre herbivore diet."


def describe_animal(animal: Animal) -> str:
    """Use any subtype that honours the ``Animal`` contract."""
    return animal.describe()


def main() -> None:
    """Run the appropriate inheritance example."""
    animals: tuple[Animal, ...] = (
        Python(name="Python"),
        Panda(name="Panda"),
        Lion(name="Lion"),
        Elephant(name="Elephant"),
    )

    print("Meaningful Specialisation Through Inheritance")
    print()

    for animal in animals:
        print(describe_animal(animal))


if __name__ == "__main__":
    main()
