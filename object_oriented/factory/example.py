"""
Run the Factory Pattern example from the client's point of view.

Client code asks ``AnimalFactory`` for an animal by identifier and then works
with the returned object through the ``Animal`` contract. It does not need to
import or instantiate the concrete ``Python``, ``Panda``, ``Lion``, or
``Elephant`` classes itself.

This is the practical benefit of the factory boundary: creation decisions stay
inside the factory while client code depends only on the behaviour it needs.
"""

from object_oriented.factory.animal_factory import AnimalFactory


def main() -> None:
    """Create each registered animal and demonstrate the shared contract."""
    for animal_type in ("python", "panda", "lion", "elephant"):
        animal = AnimalFactory.create(animal_type)
        animal.speak()


if __name__ == "__main__":
    main()
