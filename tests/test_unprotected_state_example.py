"""
test_unprotected_state_example.py

Tests for the unprotected encapsulation example.
"""

import pytest

from object_oriented.encapsulation.unprotected_state_example import Animal

INITIAL_WEIGHT_KG = 190.0
INVALID_WEIGHT_KG = -25.0


def test_initial_weight_must_be_positive() -> None:
    """Reject an invalid weight when the animal is created."""
    with pytest.raises(ValueError, match="weight_kg must be greater than zero"):
        Animal(
            name="Leo",
            species="Lion",
            weight_kg=0.0,
        )


def test_valid_initial_weight_is_stored() -> None:
    """Store a valid weight supplied during construction."""
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=INITIAL_WEIGHT_KG,
    )

    assert animal.weight_kg == INITIAL_WEIGHT_KG


def test_public_weight_can_be_replaced_with_invalid_state() -> None:
    """
    Show that direct assignment can bypass the object's construction rule.

    The assignment is deliberately demonstrating the weakness of the
    unprotected design.
    """
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=INITIAL_WEIGHT_KG,
    )

    animal.weight_kg = INVALID_WEIGHT_KG

    assert animal.weight_kg == INVALID_WEIGHT_KG
