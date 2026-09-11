"""
test_user_input_validation.py
"""

from unittest.mock import Mock

from native_gui.user_input_validation import (
    check_animal,
    normalise_animal_name,
    validate_animal_name,
)


def test_normalise_animal_name_removes_whitespace_and_folds_case() -> None:
    """Verify user-entered animal names are normalised for comparison."""
    assert normalise_animal_name("  PANDA  ") == "panda"


def test_validate_animal_name_rejects_blank_input() -> None:
    """Verify empty or whitespace-only input receives validation feedback."""
    assert validate_animal_name("   ") == "Please enter an animal name."


def test_validate_animal_name_accepts_known_animal() -> None:
    """Verify known animals return their normalised display name and sound."""
    assert validate_animal_name("  LION  ") == "Lion says: Roar!"


def test_validate_animal_name_rejects_unknown_animal() -> None:
    """Verify names outside the exhibit's animal set receive feedback."""
    assert validate_animal_name("duck") == "That animal is not in this zoo."


def test_check_animal_updates_result_and_clears_known_animal() -> None:
    """Verify successful GUI input updates feedback and clears the Entry."""
    animal_entry = Mock()
    result_label = Mock()
    animal_entry.get.return_value = "Panda"

    check_animal(animal_entry, result_label)

    result_label.config.assert_called_once_with(text="Panda says: Bleat!")
    animal_entry.delete.assert_called_once()
