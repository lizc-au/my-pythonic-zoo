"""
Tests for the Factory Pattern animal factory.

These tests verify the factory's responsibility: selecting and creating the
correct concrete animal type for a supported identifier, and rejecting unknown
identifiers with a useful error.
"""

import pytest

from object_oriented.factory.animal_factory import AnimalFactory
from object_oriented.factory.animals import Elephant, Lion, Panda, Python


@pytest.mark.parametrize(
    ("animal_type", "expected_type"),
    [
        ("python", Python),
        ("panda", Panda),
        ("lion", Lion),
        ("elephant", Elephant),
    ],
)
def test_create_returns_requested_animal(
    animal_type: str,
    expected_type: type[object],
) -> None:
    """Factory should create the concrete type registered for the identifier."""
    animal = AnimalFactory.create(animal_type)

    assert isinstance(animal, expected_type)


def test_create_returns_new_instance_each_time() -> None:
    """Factory should create a fresh object for each request."""
    first_lion = AnimalFactory.create("lion")
    second_lion = AnimalFactory.create("lion")

    assert first_lion is not second_lion


def test_create_rejects_unknown_animal_type() -> None:
    """Factory should report an unsupported identifier clearly."""
    with pytest.raises(
        ValueError,
        match=(
            r"Unknown animal type 'giraffe'\. "
            r"Available types: elephant, lion, panda, python\."
        ),
    ):
        AnimalFactory.create("giraffe")
