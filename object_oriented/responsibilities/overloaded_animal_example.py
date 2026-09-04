"""
overloaded_animal_example.py

Show the design pressure created when one object owns too many responsibilities.

This example deliberately gives ``Animal`` several jobs: storing animal data,
deciding feeding guidance, scheduling routine care, and formatting a keeper
report. The class can perform all of those tasks, but the responsibilities do
not all belong to the same reason for change.

That matters because a class with unrelated responsibilities tends to become
harder to change safely. A feeding-policy change, a scheduling change, or a
report-formatting change can all require editing the same class even though
those concerns are conceptually separate.

The companion ``collaborating_objects_example.py`` redistributes the work among
focused objects. ``Animal`` retains animal-owned information while other
objects take responsibility for feeding guidance, care scheduling, and report
formatting.

Good responsibility design does not mean creating a separate class for every
possible concern at the beginning of a project. Early modelling should identify
the responsibilities required by the current use cases and place the obvious
ones deliberately, while avoiding abstractions that have no real job yet.

As requirements grow, new responsibilities can expose pressure in the existing
design. That is the point to reassess ownership and split work where clearer
boundaries improve cohesion. The aim is neither one class that does everything
nor dozens of premature micro-classes, but responsibilities that are clear,
justified, and appropriate to the current requirements.

Only one animal is used here because the animal type is not the design question in
this example. Repeating all four zoo animals would add code without helping to
show the problems caused by placing unrelated responsibilities on one object.

A similar problem appears in business applications when one ``Document``,
``Order``, or ``InsuranceClaim`` class gradually accumulates validation,
persistence, notification, reporting, approval, and scheduling logic. The
important design question is not whether one class *can* do all of that work,
but whether it is the appropriate owner of each responsibility.
"""

from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(slots=True, frozen=True)
class Animal:
    """
    Represent an animal while deliberately owning several unrelated jobs.

    The animal's identity data belongs naturally here. Feeding guidance, care
    scheduling, and report formatting are also placed here for this first
    example so that the resulting responsibility pressure is easy to see.

    The class is intentionally plausible rather than absurdly overloaded:
    designs often become difficult gradually as reasonable-looking methods
    accumulate on an object that happens to be convenient to modify.
    """

    name: str
    species: str
    diet: str
    last_care_date: date

    def feeding_instructions(self) -> str:
        """
        Return feeding guidance based on this animal's recorded diet.

        This method is intentionally placed on Animal in the overloaded design.
        Feeding policy is a separate reason for change from the animal's
        identity data, which the companion example will make explicit.
        """
        if self.diet == "Carnivore":
            return "Provide a carnivore diet appropriate to the species."

        return "Provide plant-based food appropriate to the species."

    def next_care_date(self) -> date:
        """
        Calculate the next routine care date.

        Scheduling is deliberately owned by Animal in this first design even
        though scheduling policy may change for reasons unrelated to the
        animal's identity or feeding guidance.
        """
        return self.last_care_date + timedelta(days=30)

    def keeper_report(self) -> str:
        """
        Format a keeper-facing summary for this animal.

        Report formatting is another separate reason for change. A new layout,
        wording standard, or output format should not ideally require editing
        the same class that owns animal identity and care calculations.
        """
        return (
            f"{self.name} ({self.species})\n"
            f"  Diet: {self.diet}\n"
            f"  Feeding: {self.feeding_instructions()}\n"
            f"  Next care date: {self.next_care_date().isoformat()}"
        )


def main() -> None:
    """Run the overloaded Animal example."""
    animal = Animal(
        name="Leo",
        species="Lion",
        diet="Carnivore",
        last_care_date=date(2026, 9, 1),
    )

    print("Overloaded Animal")
    print()
    print(animal.keeper_report())


if __name__ == "__main__":
    main()
