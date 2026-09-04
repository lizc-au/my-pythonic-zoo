"""
protected_state_example.py

Protect an object's invariant through a deliberate public interface.

The companion ``unprotected_state_example.py`` validates an animal's weight
when the object is created but then allows client code to replace that value
directly. The object therefore cannot guarantee that its own weight rule
continues to hold when callers use the exposed attribute.

This example gives ``Animal`` a deliberate public interface. Construction and
later updates both pass through validation, while the stored weight is treated
as an internal implementation detail.

Python does not provide truly private attributes in the same way as some other
object-oriented languages.

A single leading underscore, such as ``_weight_kg``, is only a convention. It
tells callers that the attribute is internal, but code can still assign to it
directly.

A double leading underscore, such as ``__weight_kg``, triggers name mangling.
That makes accidental access harder and helps protect the public interface, but
it is still not a security boundary. A determined caller can discover and use
the mangled attribute name.

Misunderstanding these conventions can have practical consequences. Code that
assumes either form provides enforced protection may accidentally bypass an
object's intended interface, violate its invariants, and potentially corrupt
valuable data. ``encapsulation/README.md`` explores these limitations and their
implications in more detail.

Encapsulation in Python is therefore primarily about designing a clear public
API, making the correct operations obvious, and keeping validation and state
rules with the object that owns them.

Only one animal is used because animal type is not the design question in this
example. Repeating all four zoo animals would add code without helping to show
how encapsulation supports controlled state changes.

A similar design appears in business software when an ``Order`` controls
quantity changes or an ``InsuranceClaim`` controls status transitions. Rather
than encouraging arbitrary state changes, the domain object exposes operations
that validate and preserve the rules it owns.
"""

from dataclasses import dataclass, field


@dataclass(slots=True, init=False)
class Animal:
    """
    Represent an animal with a controlled interface for recorded weight.

    The constructor accepts the public concept ``weight_kg``. Internally, the
    value is stored as ``__weight_kg`` so ordinary client code does not work
    directly with the storage attribute.

    ``record_weight()`` owns later changes, while the read-only ``weight_kg``
    property provides normal access to the current value.
    """

    name: str
    species: str
    __weight_kg: float = field(repr=False)

    def __init__(self, name: str, species: str, weight_kg: float) -> None:
        """Create an animal with a valid initial weight."""
        self._validate_weight(weight_kg)

        self.name = name
        self.species = species
        self.__weight_kg = weight_kg

    @property
    def weight_kg(self) -> float:
        """Return the animal's current recorded weight."""
        return self.__weight_kg

    def record_weight(self, weight_kg: float) -> None:
        """Record a new weight after checking the animal's invariant."""
        self._validate_weight(weight_kg)
        self.__weight_kg = weight_kg

    @staticmethod
    def _validate_weight(weight_kg: float) -> None:
        """Reject weights that would violate the animal's invariant."""
        if weight_kg <= 0:
            raise ValueError("weight_kg must be greater than zero")


def main() -> None:
    """Run the protected-state example."""
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=190.0,
    )

    print("Initially valid:")
    print(f"{animal.name}: {animal.weight_kg} kg")

    animal.record_weight(195.0)

    print()
    print("After controlled update:")
    print(f"{animal.name}: {animal.weight_kg} kg")


if __name__ == "__main__":
    main()
