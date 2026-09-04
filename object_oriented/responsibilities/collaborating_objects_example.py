"""
collaborating_objects_example.py

Redistribute responsibilities among collaborating objects.

The companion ``overloaded_animal_example.py`` places animal data, feeding
guidance, care scheduling, and keeper-report formatting on one ``Animal`` class.
That design works, but it gives one class several unrelated reasons to change.

This collaborating example assigns those responsibilities to more focused owners:

- ``Animal`` owns animal identity and domain data.
- ``FeedingGuide`` owns feeding guidance.
- ``CareSchedule`` owns routine care-date calculation.
- ``KeeperReport`` owns presentation of keeper-facing information.

The collaborator classes are plain classes because they currently own behaviour
but no instance data; ``Animal`` uses a dataclass because it stores domain data.

The objects collaborate to produce the same useful result, but each component
has a clearer reason to change. ``KeeperReport`` asks the other objects for the
information it needs rather than reimplementing their rules.

This does not mean every responsibility should always become a separate class.
The split is justified here because the concerns already have distinct rules
and distinct reasons to change. In a smaller application, some of these jobs
could reasonably remain together until requirements create enough design
pressure to separate them.

Only one animal is used here because the animal type is not the design question in
this example. Repeating all four zoo animals would add code without helping to
show how responsibilities are divided between collaborating objects.

A similar design appears in business software when an ``Order`` or
``InsuranceClaim`` collaborates with focused components for validation,
scheduling, notifications, or reporting. The domain object does not need to
perform every operation merely because those operations involve it.
"""

from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(slots=True, frozen=True)
class Animal:
    """
    Represent animal-owned identity and domain data.

    Unlike the overloaded example, this class does not decide feeding policy,
    calculate care schedules, or format keeper reports. Those responsibilities
    belong to collaborating objects with their own reasons to change.
    """

    name: str
    species: str
    diet: str
    last_care_date: date


class FeedingGuide:
    """Provide feeding guidance based on an animal's diet."""

    def instructions_for(self, animal: Animal) -> str:
        """Return feeding guidance appropriate to the supplied animal."""
        if animal.diet == "Carnivore":
            return "Provide a carnivore diet appropriate to the species."

        return "Provide plant-based food appropriate to the species."


class CareSchedule:
    """Calculate routine care dates for animals."""

    def next_date_for(self, animal: Animal) -> date:
        """Return the next routine care date for the supplied animal."""
        return animal.last_care_date + timedelta(days=30)


class KeeperReport:
    """
    Format keeper-facing information using collaborating objects.

    KeeperReport owns presentation, but delegates feeding and scheduling
    decisions to the objects that own those responsibilities.
    """

    def format_for(
        self,
        animal: Animal,
        feeding_guide: FeedingGuide,
        care_schedule: CareSchedule,
    ) -> str:
        """Return a keeper-facing summary for the supplied animal."""
        return (
            f"{animal.name} ({animal.species})\n"
            f"  Diet: {animal.diet}\n"
            f"  Feeding: {feeding_guide.instructions_for(animal)}\n"
            f"  Next care date: {care_schedule.next_date_for(animal).isoformat()}"
        )


def main() -> None:
    """Run the collaborating-objects example."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )
    feeding_guide = FeedingGuide()
    care_schedule = CareSchedule()
    keeper_report = KeeperReport()

    print("Collaborating Objects")
    print()
    print(
        keeper_report.format_for(
            animal=animal,
            feeding_guide=feeding_guide,
            care_schedule=care_schedule,
        )
    )


if __name__ == "__main__":
    main()
