"""
test_appropriate_inheritance_example.py

Tests for the appropriate inheritance example.

The key test here is test_animal_subtypes_are_substitutable: it captures
the design reason we're using inheritance, rather than merely checking that
Python's inheritance syntax works.
"""

import pytest

from object_oriented.inheritance.appropriate_inheritance_example import (
    Animal,
    Elephant,
    Lion,
    Panda,
    Python,
    describe_animal,
)


def test_abstract_animal_cannot_be_instantiated() -> None:
    with pytest.raises(TypeError):
        # The test deliberately attempts an invalid construction to verify that the
        # abstract contract is enforced at runtime; the ignore permits that test case.
        Animal(name="Animal")  # type: ignore[abstract]


@pytest.mark.parametrize(
    ("animal", "expected"),
    [
        (
            Python(name="Python"),
            "Python: Provide an appropriately sized whole-prey diet.",
        ),
        (
            Panda(name="Panda"),
            "Panda: Provide a bamboo-dominated diet.",
        ),
        (
            Lion(name="Lion"),
            "Lion: Provide a nutritionally complete carnivore diet.",
        ),
        (
            Elephant(name="Elephant"),
            "Elephant: Provide a high-fibre herbivore diet.",
        ),
    ],
)
def test_animal_subtypes_are_substitutable(
    animal: Animal,
    expected: str,
) -> None:
    assert describe_animal(animal) == expected


def test_concrete_animals_are_animals() -> None:
    animals = (
        Python(name="Python"),
        Panda(name="Panda"),
        Lion(name="Lion"),
        Elephant(name="Elephant"),
    )

    assert all(isinstance(animal, Animal) for animal in animals)
