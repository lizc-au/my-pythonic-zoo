"""
test_protected_state_example.py

Tests for the protected encapsulation example.
"""

import pytest

from object_oriented.encapsulation.protected_state_example import Animal

INITIAL_WEIGHT_KG = 190.0
UPDATED_WEIGHT_KG = 195.0
INVALID_WEIGHT_KG = -25.0


def test_initial_weight_must_be_positive() -> None:
    """Reject an invalid weight when the animal is created."""
    with pytest.raises(ValueError, match="weight_kg must be greater than zero"):
        Animal(
            name="Leo",
            species="Lion",
            weight_kg=0.0,
        )


def test_record_weight_updates_valid_state() -> None:
    """Allow a valid weight change through the public operation."""
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=INITIAL_WEIGHT_KG,
    )

    animal.record_weight(UPDATED_WEIGHT_KG)

    assert animal.weight_kg == UPDATED_WEIGHT_KG


def test_record_weight_rejects_invalid_state() -> None:
    """Prevent the public operation from violating the weight invariant."""
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=INITIAL_WEIGHT_KG,
    )

    with pytest.raises(ValueError, match="weight_kg must be greater than zero"):
        animal.record_weight(INVALID_WEIGHT_KG)

    assert animal.weight_kg == INITIAL_WEIGHT_KG


def test_weight_property_has_no_public_setter() -> None:
    """Prevent normal client code from assigning through the public property."""
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=INITIAL_WEIGHT_KG,
    )

    with pytest.raises(AttributeError):
        animal.weight_kg = INVALID_WEIGHT_KG  # type: ignore[misc]

    assert animal.weight_kg == INITIAL_WEIGHT_KG


def test_name_mangled_storage_can_still_be_bypassed_deliberately() -> None:
    """
    Show that double-underscore storage is name-mangled, not truly private.

    This deliberately bypasses the public API to document Python's actual
    encapsulation boundary. Application code should not do this.
    """
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=INITIAL_WEIGHT_KG,
    )

    animal._Animal__weight_kg = INVALID_WEIGHT_KG  # type: ignore[attr-defined]

    assert animal.weight_kg == INVALID_WEIGHT_KG
