"""
test_collaborating_objects_example.py

Tests for the collaborating responsibilities example.

The delegation test is the important one for this exhibit: it proves
KeeperReport is actually collaborating rather than quietly duplicating
feeding and scheduling logic.
"""

from datetime import date

from object_oriented.responsibilities.collaborating_objects_example import (
    Animal,
    CareSchedule,
    FeedingGuide,
    KeeperReport,
)


def test_feeding_guide_returns_carnivore_instructions() -> None:
    """Return carnivore guidance for a carnivorous animal."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    assert (
        FeedingGuide().instructions_for(animal)
        == "Provide a carnivore diet appropriate to the species."
    )


def test_care_schedule_returns_next_routine_date() -> None:
    """Calculate the next routine care date."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    assert CareSchedule().next_date_for(animal) == date(2026, 10, 1)


def test_keeper_report_delegates_to_collaborators() -> None:
    """Use collaborator results rather than reimplementing their rules."""

    class StubFeedingGuide(FeedingGuide):
        def instructions_for(self, animal: Animal) -> str:
            return "Stub feeding guidance."

    class StubCareSchedule(CareSchedule):
        def next_date_for(self, animal: Animal) -> date:
            return date(2030, 1, 2)

    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    report = KeeperReport().format_for(
        animal=animal,
        feeding_guide=StubFeedingGuide(),
        care_schedule=StubCareSchedule(),
    )

    assert report == (
        "Leo (Lion)\n"
        "  Diet: Carnivore\n"
        "  Feeding: Stub feeding guidance.\n"
        "  Next care date: 2030-01-02"
    )


def test_keeper_report_formats_real_collaborator_results() -> None:
    """Format the complete report using the real collaborators."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    report = KeeperReport().format_for(
        animal=animal,
        feeding_guide=FeedingGuide(),
        care_schedule=CareSchedule(),
    )

    assert report == (
        "Leo (Lion)\n"
        "  Diet: Carnivore\n"
        "  Feeding: Provide a carnivore diet appropriate to the species.\n"
        "  Next care date: 2026-10-01"
    )
