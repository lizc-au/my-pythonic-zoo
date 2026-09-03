"""
Demonstrate client-selected composition.

In this version, client code chooses both the animal and the movement behaviour
used to construct it.

For example::

    Animal(species="Python", movement=Slither())

This makes the dependency explicit and gives the client control over which
behaviour is supplied. That is useful when the behaviour is genuinely
configurable, selectable, or expected to vary independently from the object.

A real-world example is a reporting component whose output format is selected
by its caller. The same ``Report`` could be composed with ``PdfFormatter`` for
one request and ``CsvFormatter`` for another. In that case the caller genuinely
owns the choice, so supplying the behaviour from client code is appropriate.

There is an important trade-off. The client must know that a python should be
given ``Slither`` and that a panda, lion, or elephant should be given ``Walk``.
If those relationships represent established domain rules rather than choices
the client should make, this exposes domain knowledge at the wrong boundary.

See ``construction_selected_example.py`` for an alternative in which a
construction boundary owns the selection decision.

The distinction is not whether composition is being used. Both examples use
composition. The distinction is which part of the program owns the composition
decision.
"""

from object_oriented.composition.animal import Animal
from object_oriented.composition.behaviours.movement import Slither, Walk


def main() -> None:
    """Create animals with client-selected movement behaviours."""
    animals = [
        Animal(species="Python", movement=Slither()),
        Animal(species="Panda", movement=Walk()),
        Animal(species="Lion", movement=Walk()),
        Animal(species="Elephant", movement=Walk()),
    ]

    print("Client-selected composition:")

    for animal in animals:
        print(animal.describe_movement())


if __name__ == "__main__":
    main()
