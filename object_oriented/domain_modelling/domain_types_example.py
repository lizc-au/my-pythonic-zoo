"""
domain_types_example.py

Introduce distinct domain types when meaningful behaviour differs.

The companion ``data_model_example.py`` represents Ball Python, Giant Panda,
Lion, and African Savanna Elephant using one Animal type because their
differences are only recorded data. This example adds a new requirement:
the zoo must provide feeding instructions appropriate to each animal type.

That new behaviour changes the modelling pressure. Separate domain types now
have a responsibility to own because feeding instructions differ by animal.
BallPython, GiantPanda, Lion, and AfricanSavannaElephant therefore become
explicit subtypes of Animal rather than remaining only different attribute
values on one general-purpose object.

This does not mean that every domain difference should become inheritance.
Taxonomic ranks such as phylum, class, order, family, genus, and species still
remain data because this application only needs to record them. If feeding
behaviour later became complex, independently configurable, or reusable across
different animals, a collaborating feeding object could become a better owner;
the Composition exhibit demonstrates that alternative design direction.

A similar decision appears in business software. A general Document or
InsuranceClaim type may be sufficient while differences are limited to data
such as category, status, owner, or policy type. Distinct domain types become
more useful when those categories acquire meaningful behaviour or rules, such
as different validation, approval, retention, settlement, or processing
requirements. The important question is not whether the domain uses different
names, but whether the software needs those concepts to own different
responsibilities.

Movement and sounds are deliberately omitted because those concerns are
explored by other Object-Oriented Zoo exhibits. This keeps the example focused
on the decision to introduce explicit domain types.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Define the shared shape and behaviour of explicit animal domain types.

    Animal is an abstract base class because this model deliberately represents
    an explicit is-a relationship: BallPython, GiantPanda, Lion, and
    AfricanSavannaElephant are all Animal domain types. ``@abstractmethod``
    makes ``feeding_instructions()`` part of the required contract. A concrete
    Animal subtype cannot be instantiated until it provides that behaviour,
    preventing a new animal type from accidentally omitting a responsibility
    that the domain model requires.

    Attempting to instantiate a subtype that omits the required implementation
    raises TypeError.
    """

    common_name: str
    phylum: str
    taxonomic_class: str
    order: str
    family: str
    genus: str
    species: str
    diet: str

    @abstractmethod
    def feeding_instructions(self) -> str:
        """Return feeding instructions appropriate to this animal type."""

    def describe(self) -> str:
        """
        Return a readable summary of this animal type's fixed domain data.

        This behaviour remains shared because every animal is described in the
        same way. Feeding instructions are separate because that behaviour now
        varies by concrete domain type.
        """

        return (
            f"{self.common_name}\n"
            f"  Phylum: {self.phylum}\n"
            f"  Class: {self.taxonomic_class}\n"
            f"  Order: {self.order}\n"
            f"  Family: {self.family}\n"
            f"  Genus: {self.genus}\n"
            f"  Species: {self.species}\n"
            f"  Diet: {self.diet}"
        )


class BallPython(Animal):
    """Represent a Ball Python with its fixed taxonomy and feeding behaviour."""

    common_name = "Ball Python"
    phylum = "Chordata"
    taxonomic_class = "Reptilia"
    order = "Squamata"
    family = "Pythonidae"
    genus = "Python"
    species = "Python regius"
    diet = "Carnivore"

    def feeding_instructions(self) -> str:
        """Return feeding guidance specific to a Ball Python."""

        return "Offer appropriately sized prey and allow time to swallow undisturbed."


class GiantPanda(Animal):
    """Represent a Giant Panda with its fixed taxonomy and feeding behaviour."""

    common_name = "Giant Panda"
    phylum = "Chordata"
    taxonomic_class = "Mammalia"
    order = "Carnivora"
    family = "Ursidae"
    genus = "Ailuropoda"
    species = "Ailuropoda melanoleuca"
    diet = "Herbivore"

    def feeding_instructions(self) -> str:
        """Return feeding guidance specific to a Giant Panda."""

        return "Provide bamboo as the primary food source throughout the day."


class Lion(Animal):
    """Represent a Lion with its fixed taxonomy and feeding behaviour."""

    common_name = "Lion"
    phylum = "Chordata"
    taxonomic_class = "Mammalia"
    order = "Carnivora"
    family = "Felidae"
    genus = "Panthera"
    species = "Panthera leo"
    diet = "Carnivore"

    def feeding_instructions(self) -> str:
        """Return feeding guidance specific to a Lion."""

        return "Provide a carnivore diet appropriate to a large cat."


class AfricanSavannaElephant(Animal):
    """
    Represent an African Savanna Elephant with fixed taxonomy and
    feeding behaviour
    """

    common_name = "African Savanna Elephant"
    phylum = "Chordata"
    taxonomic_class = "Mammalia"
    order = "Proboscidea"
    family = "Elephantidae"
    genus = "Loxodonta"
    species = "Loxodonta africana"
    diet = "Herbivore"

    def feeding_instructions(self) -> str:
        """Return feeding guidance specific to an African Savanna Elephant."""

        return "Provide high-volume plant food, including grasses, leaves, and browse."


def main() -> None:
    """Describe explicit animal domain types and their specialised behaviour."""

    animals: list[Animal] = [
        BallPython(),
        GiantPanda(),
        Lion(),
        AfricanSavannaElephant(),
    ]

    print("Domain Model: Differences Represented as Types and Behaviour")
    print()

    for animal in animals:
        print(animal.describe())
        print(f"  Feeding: {animal.feeding_instructions()}")
        print()


if __name__ == "__main__":
    main()
