"""
Demonstrate construction-selected composition.

This example calls the approach construction-selected because the composition
decision belongs to the code responsible for constructing a complete animal.
That distinguishes it from client-selected composition, where ordinary client
code chooses the behaviour, and domain-type-selected composition, where a
specific domain type owns knowledge of its own behaviour.

In this version, ordinary client code does not choose an animal's movement
behaviour. A construction boundary owns the domain knowledge needed to assemble
the appropriate object.

For example::

    python = create_animal("Python")

The returned ``Animal`` is still composed with a separate ``Movement`` object.
Composition has not changed. What has changed is which part of the program owns
the decision about which behaviour should be supplied.

This is appropriate when the relationship represents established domain
knowledge rather than a choice the client should make. A caller wanting a
python should not also need to know that the python must be composed with
``Slither``.

A real-world example is a document-processing application where a document type
requires a particular validator. Ordinary client code may request an invoice
processor without needing to know which validation component correctly enforces
invoice rules. Construction code can assemble the processor with the required
validator while the client uses the completed object.

A factory is one possible way to own this construction responsibility. This
example uses a small function so that the Composition lesson remains focused on
composition rather than repeating the Factory Pattern implementation.

Object-oriented techniques and design patterns are not mutually exclusive.
Production software commonly combines them because each addresses a different
design concern. This example uses Composition to separate movement behaviour
from ``Animal``. A Factory could additionally own construction of the correctly
composed object, while responsibility and domain-modelling decisions determine
where that knowledge belongs and how the animal itself should be represented.

Domain modelling therefore raises a further question: should ``"Python"``
merely be data on a general ``Animal``, or should ``Python`` be a distinct
domain type? See the Domain Modelling examples for that separate design
decision.

As the Object-Oriented examples develop, look for places where several
techniques work together rather than assuming that a program should select one
pattern and use it in isolation.
"""

from collections.abc import Callable

from object_oriented.composition.animal import Animal
from object_oriented.composition.behaviours.movement import Movement, Slither, Walk


def create_animal(species: str) -> Animal:
    """Create an animal with the movement appropriate to its species."""
    movement_by_species: dict[str, Callable[[], Movement]] = {
        "Python": Slither,
        "Panda": Walk,
        "Lion": Walk,
        "Elephant": Walk,
    }

    try:
        movement_type = movement_by_species[species]
    except KeyError as exc:
        raise ValueError(f"Unknown species: {species!r}.") from exc

    return Animal(species=species, movement=movement_type())


def main() -> None:
    """Create animals without making client code select their movements."""
    animals = [
        create_animal("Python"),
        create_animal("Panda"),
        create_animal("Lion"),
        create_animal("Elephant"),
    ]

    print("Construction-selected composition:")

    for animal in animals:
        print(animal.describe_movement())


if __name__ == "__main__":
    main()
