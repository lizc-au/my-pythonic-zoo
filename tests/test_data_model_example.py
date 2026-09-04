"""
test_data_model_example.py
"""

from object_oriented.domain_modelling.data_model_example import (
    Animal,
    create_african_savanna_elephant,
    create_ball_python,
    create_giant_panda,
    create_lion,
)


def test_all_animals_use_same_domain_type() -> None:
    animals = [
        create_ball_python(),
        create_giant_panda(),
        create_lion(),
        create_african_savanna_elephant(),
    ]

    assert all(type(animal) is Animal for animal in animals)


def test_ball_python_contains_expected_domain_data() -> None:
    animal = create_ball_python()

    assert animal.common_name == "Ball Python"
    assert animal.phylum == "Chordata"
    assert animal.taxonomic_class == "Reptilia"
    assert animal.order == "Squamata"
    assert animal.family == "Pythonidae"
    assert animal.genus == "Python"
    assert animal.species == "Python regius"
    assert animal.diet == "Carnivore"


def test_describe_returns_shared_animal_representation() -> None:
    animal = create_lion()

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
