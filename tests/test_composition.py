"""
Tests for the Object-Oriented Composition examples.

These tests verify the shared movement behaviours and the three different
places where responsibility for selecting a composed behaviour can live.
"""

import pytest

from object_oriented.composition.animal import Animal
from object_oriented.composition.behaviours.movement import Slither, Walk
from object_oriented.composition.construction_selected_example import create_animal
from object_oriented.composition.domain_type_selected_example import (
    Elephant,
    Lion,
    Panda,
    Python,
)


@pytest.mark.parametrize(
    ("movement", "expected"),
    [
        (Slither(), "slithers"),
        (Walk(), "walks"),
    ],
)
def test_movement_descriptions(
    movement: Slither | Walk,
    expected: str,
) -> None:
    """Movement implementations should describe their behaviour."""
    assert movement.description() == expected


@pytest.mark.parametrize(
    ("species", "movement", "expected"),
    [
        ("Python", Slither(), "A python slithers."),
        ("Panda", Walk(), "A panda walks."),
        ("Lion", Walk(), "A lion walks."),
        ("Elephant", Walk(), "An elephant walks."),
    ],
)
def test_client_selected_animal_describes_composed_movement(
    species: str,
    movement: Slither | Walk,
    expected: str,
) -> None:
    """A general Animal should use the movement supplied by its client."""
    animal = Animal(species=species, movement=movement)

    assert animal.describe_movement() == expected


@pytest.mark.parametrize(
    ("species", "expected"),
    [
        ("Python", "A python slithers."),
        ("Panda", "A panda walks."),
        ("Lion", "A lion walks."),
        ("Elephant", "An elephant walks."),
    ],
)
def test_construction_selected_animal_uses_domain_movement(
    species: str,
    expected: str,
) -> None:
    """Construction code should select the movement associated with the species."""
    animal = create_animal(species)

    assert animal.describe_movement() == expected


def test_construction_selected_animal_rejects_unknown_species() -> None:
    """Construction code should reject species for which it has no rule."""
    with pytest.raises(ValueError, match=r"Unknown species: 'Giraffe'\."):
        create_animal("Giraffe")


@pytest.mark.parametrize(
    ("domain_type", "expected"),
    [
        (Python(), "A python slithers."),
        (Panda(), "A panda walks."),
        (Lion(), "A lion walks."),
        (Elephant(), "An elephant walks."),
    ],
)
def test_domain_type_selects_its_own_movement(
    domain_type: Python | Panda | Lion | Elephant,
    expected: str,
) -> None:
    """Each domain type should create an Animal with its required movement."""
    animal = domain_type.create_animal()

    assert animal.describe_movement() == expected
