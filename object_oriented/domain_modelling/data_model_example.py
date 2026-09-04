"""
data_model_example.py

Model domain differences as data when behaviour is shared.

This example asks whether Ball Python, Giant Panda, Lion, and African
Savanna Elephant need separate Python classes simply because their biological
classification and diets differ. They do not yet have different
responsibilities or behaviour, so one Animal type represents all four. Their
common names, taxonomy, and diets are data describing individual Animal
objects rather than reasons to introduce subclasses.

The modelling decision matters because real-world categories do not map
automatically to software inheritance hierarchies. Phylum, biological class,
order, family, genus, and species form a taxonomic hierarchy, but this
application currently only needs to record those classifications. Turning
each taxonomic rank or animal name into a Python class would add abstraction
without solving a behavioural problem.

A similar decision occurs in business applications. A document system might
represent invoices, insurance claims, and correspondence using one Document
type while their differences are limited to attributes such as document type,
status, owner, or retention category. Separate InvoiceDocument or ClaimDocument
types become more useful only when those concepts acquire meaningful rules or
behaviour that the general Document model should not own.

The companion ``domain_types_example.py`` introduces such a requirement:
animal-specific feeding instructions. It demonstrates when distinct domain
types can become useful. Movement and sounds are deliberately omitted here
because those concerns are explored by other Object-Oriented Zoo exhibits,
allowing this example to stay focused on domain-modelling decisions.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Animal:
    """
    Represent an animal whose domain differences are currently data.

    ``slots=True`` keeps the model closed to undeclared attributes, helping
    catch mistakes such as misspelled field names. ``frozen=True`` prevents
    these domain facts from being reassigned after construction. Those
    constraints suit this example because an animal's recorded taxonomy is
    treated as established identity data rather than mutable application
    state. They are modelling choices, not requirements of domain modelling.
    """

    common_name: str
    phylum: str
    taxonomic_class: str
    order: str
    family: str
    genus: str
    species: str
    diet: str

    def describe(self) -> str:
        """
        Return a readable summary of this animal's recorded domain data.

        This shared behaviour is deliberately kept on Animal because every
        animal is described in exactly the same way. It provides a contrast
        with the companion example, where feeding instructions vary by animal
        type and therefore create a new domain-modelling decision.
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


def create_ball_python() -> Animal:
    """Create an Animal containing the fixed domain data for a Ball Python."""

    return Animal(
        common_name="Ball Python",
        phylum="Chordata",
        taxonomic_class="Reptilia",
        order="Squamata",
        family="Pythonidae",
        genus="Python",
        species="Python regius",
        diet="Carnivore",
    )


def create_giant_panda() -> Animal:
    """Create an Animal containing the fixed domain data for a Giant Panda."""

    return Animal(
        common_name="Giant Panda",
        phylum="Chordata",
        taxonomic_class="Mammalia",
        order="Carnivora",
        family="Ursidae",
        genus="Ailuropoda",
        species="Ailuropoda melanoleuca",
        diet="Herbivore",
    )


def create_lion() -> Animal:
    """Create an Animal containing the fixed domain data for a Lion."""

    return Animal(
        common_name="Lion",
        phylum="Chordata",
        taxonomic_class="Mammalia",
        order="Carnivora",
        family="Felidae",
        genus="Panthera",
        species="Panthera leo",
        diet="Carnivore",
    )


def create_african_savanna_elephant() -> Animal:
    """
    Create an Animal containing the fixed domain data for an African
    Savanna Elephant.
    """

    return Animal(
        common_name="African Savanna Elephant",
        phylum="Chordata",
        taxonomic_class="Mammalia",
        order="Proboscidea",
        family="Elephantidae",
        genus="Loxodonta",
        species="Loxodonta africana",
        diet="Herbivore",
    )


def main() -> None:
    """Describe animals whose domain differences are represented as data."""

    animals = [
        create_ball_python(),
        create_giant_panda(),
        create_lion(),
        create_african_savanna_elephant(),
    ]

    print("Domain Model: Differences Represented as Data")
    print()

    for animal in animals:
        print(animal.describe())
        print()


if __name__ == "__main__":
    main()
