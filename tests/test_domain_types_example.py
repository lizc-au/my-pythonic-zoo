"""
test_domain_types_example.py
"""

import pytest

from object_oriented.domain_modelling.domain_types_example import (
    AfricanSavannaElephant,
    Animal,
    BallPython,
    GiantPanda,
    Lion,
)


def test_animal_cannot_be_instantiated_directly() -> None:
    """
    Verify at runtime that Python rejects the abstract Animal type.

    Mypy already detects this invalid construction statically. The targeted
    type ignore is used only so this test can deliberately perform the invalid
    operation and confirm that Python raises TypeError at runtime.
    """
    with pytest.raises(TypeError):
        Animal()  # type: ignore[abstract]


def test_concrete_domain_types_are_animals() -> None:
    animals = [
        BallPython(),
        GiantPanda(),
        Lion(),
        AfricanSavannaElephant(),
    ]

    assert all(isinstance(animal, Animal) for animal in animals)


def test_ball_python_contains_expected_domain_data() -> None:
    animal = BallPython()

    assert animal.common_name == "Ball Python"
    assert animal.phylum == "Chordata"
    assert animal.taxonomic_class == "Reptilia"
    assert animal.order == "Squamata"
    assert animal.family == "Pythonidae"
    assert animal.genus == "Python"
    assert animal.species == "Python regius"
    assert animal.diet == "Carnivore"


def test_describe_is_shared_by_concrete_domain_types() -> None:
    animal = Lion()

    assert animal.describe() == (
        "Lion\n"
        "  Phylum: Chordata\n"
        "  Class: Mammalia\n"
        "  Order: Carnivora\n"
        "  Family: Felidae\n"
        "  Genus: Panthera\n"
        "  Species: Panthera leo\n"
        "  Diet: Carnivore"
    )


def test_concrete_domain_types_provide_feeding_instructions() -> None:
    animals = [
        BallPython(),
        GiantPanda(),
        Lion(),
        AfricanSavannaElephant(),
    ]

    instructions = [animal.feeding_instructions() for animal in animals]

    assert instructions == [
        "Offer appropriately sized prey and allow time to swallow undisturbed.",
        "Provide bamboo as the primary food source throughout the day.",
        "Provide a carnivore diet appropriate to a large cat.",
        "Provide high-volume plant food, including grasses, leaves, and browse.",
    ]
