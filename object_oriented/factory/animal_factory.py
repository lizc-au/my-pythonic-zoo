"""
Factory Pattern: Creating Zoo Animals

A factory centralises object creation so client code can request an object
without knowing which concrete class must be instantiated.

This example uses a registry that maps a small identifier, such as ``"lion"``,
to the corresponding concrete animal class. The factory returns objects that
satisfy the ``Animal`` protocol, so callers depend on the required behaviour
rather than on particular implementations.

Benefits
--------
- Object creation logic has one clear responsibility and location.
- Client code does not need to import or select concrete animal classes.
- Adding a new registered animal does not require another branch in a long
  ``if`` or ``match`` statement.
- The factory exposes the stable ``Animal`` contract rather than a union of
  every concrete type it currently supports.

When not to use this approach
-----------------------------
Direct construction is usually clearer when callers already know exactly which
class they need and object creation has no meaningful selection logic. A
factory adds indirection, so it should solve a real creation problem rather
than being introduced merely because several classes exist.

See ``factory.animals.animal.Animal`` for the behavioural scope of animals in
this example and cross-references to other object-oriented design examples.
"""

from collections.abc import Callable
from typing import ClassVar

from object_oriented.factory.animals import Animal, Elephant, Lion, Panda, Python

AnimalCreator = Callable[[], Animal]


class AnimalFactory:
    """Create registered animal objects by type name."""

    _animal_types: ClassVar[dict[str, AnimalCreator]] = {
        "python": Python,
        "panda": Panda,
        "lion": Lion,
        "elephant": Elephant,
    }

    @classmethod
    def create(cls, animal_type: str) -> Animal:
        """
        Create an animal registered under ``animal_type``.

        Args:
            animal_type: Identifier of the animal type to create.

        Returns:
            A new object satisfying the ``Animal`` protocol.

        Raises:
            ValueError: If ``animal_type`` is not registered with the factory.
        """
        try:
            creator = cls._animal_types[animal_type]
        except KeyError as exc:
            available = ", ".join(sorted(cls._animal_types))
            raise ValueError(
                f"Unknown animal type {animal_type!r}. Available types: {available}."
            ) from exc

        return creator()
