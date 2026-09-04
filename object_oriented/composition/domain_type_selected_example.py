"""
Demonstrate domain-type-selected composition.

In this version, a concrete domain type owns the knowledge of which movement
behaviour belongs to it.

For example::

    python = Python()

Client code does not choose ``Slither``. The ``Python`` type knows that a
python moves by slithering and composes itself with that behaviour.

This is still composition: the object has a separate ``Movement`` collaborator.
What changes is ownership of the selection decision.

This approach is useful when the behaviour is an intrinsic rule of the domain
type rather than a configurable choice. It keeps that knowledge close to the
type it describes and prevents ordinary client code from having to know how the
object should be assembled.

A real-world example is a payment type that always uses a specific validation
policy. If ``BankTransferPayment`` must always use ``BankTransferValidator``,
the payment type can own that relationship while still delegating validation to
a separate composed object.

The trade-off is reduced configurability. If movement needs to vary for the
same domain type, hard-wiring the selection inside that type may be too
restrictive. Client-selected or construction-selected composition may then be a
better fit.

Object-oriented techniques and design patterns can also be combined. A Factory
could create these domain types, while each domain type still uses Composition
internally.

See the Domain Modelling examples for the related question of when a
distinction such as ``Python`` should be represented as a separate type rather
than merely as data on a general ``Animal``.
"""

from dataclasses import dataclass

from object_oriented.composition.animal import Animal
from object_oriented.composition.behaviours.movement import Slither, Walk


@dataclass(slots=True, frozen=True)
class Python:
    """Represent a Python that owns its movement-selection rule."""

    def create_animal(self) -> Animal:
        """Create the composed Animal representation for this domain type."""
        return Animal(species="Python", movement=Slither())


@dataclass(slots=True, frozen=True)
class Panda:
    """Represent a Panda that owns its movement-selection rule."""

    def create_animal(self) -> Animal:
        """Create the composed Animal representation for this domain type."""
        return Animal(species="Panda", movement=Walk())


@dataclass(slots=True, frozen=True)
class Lion:
    """Represent a Lion that owns its movement-selection rule."""

    def create_animal(self) -> Animal:
        """Create the composed Animal representation for this domain type."""
        return Animal(species="Lion", movement=Walk())


@dataclass(slots=True, frozen=True)
class Elephant:
    """Represent an Elephant that owns its movement-selection rule."""

    def create_animal(self) -> Animal:
        """Create the composed Animal representation for this domain type."""
        return Animal(species="Elephant", movement=Walk())


def main() -> None:
    """Demonstrate domain-type-selected composition."""
    animals = [
        Python().create_animal(),
        Panda().create_animal(),
        Lion().create_animal(),
        Elephant().create_animal(),
    ]

    print("Domain-type-selected composition:")

    for animal in animals:
        print(animal.describe_movement())


if __name__ == "__main__":
    main()
