"""
test_overloaded_animal_example.py

Tests for the overloaded responsibilities example.
"""

from datetime import date

from object_oriented.responsibilities.overloaded_animal_example import Animal


def test_carnivore_feeding_instructions() -> None:
    """Return carnivore feeding guidance for a carnivorous animal."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    assert (
        animal.feeding_instructions()
        == "Provide a carnivore diet appropriate to the species."
    )


def test_plant_based_feeding_instructions() -> None:
    """Return plant-based feeding guidance for a non-carnivorous animal."""
    animal = Animal(
        name="Bao",
        species="Giant Panda",
        diet="Herbivore",
        last_care_date=date(2026, 9, 1),
    )

    assert (
        animal.feeding_instructions()
        == "Provide plant-based food appropriate to the species."
    )


def test_next_care_date() -> None:
    """Schedule routine care thirty days after the previous care date."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    assert animal.next_care_date() == date(2026, 10, 1)


def test_keeper_report() -> None:
    """Format the complete keeper-facing report."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    assert animal.keeper_report() == (
        "Leo (Lion)\n"
        "  Diet: Carnivore\n"
        "  Feeding: Provide a carnivore diet appropriate to the species.\n"
        "  Next care date: 2026-10-01"
    )
