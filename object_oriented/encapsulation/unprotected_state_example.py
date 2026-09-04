"""
unprotected_state_example.py

Show the problems caused when an object's state can be changed without control.

This example models a zoo animal whose recorded weight must remain positive.
The rule matters to the domain, but the first design exposes ``weight_kg`` as a
freely assignable public attribute. Client code can therefore bypass the rule
after construction and place the object into an invalid state.

Encapsulation is not simply about hiding attributes. The more important design
question is whether an object protects the invariants it is responsible for.
An invariant is a condition that should remain true for every valid instance
throughout its lifetime.

The point here is not "public attributes are bad"; it is that an object which
owns a rule should not allow callers to bypass that rule and leave it invalid.

Only one animal is used because animal type is not the design question in this
example. Repeating all four zoo animals would add code without helping to show
how uncontrolled state changes can violate an object's rules.

A similar problem appears in business software when an ``Order`` allows a
negative quantity to be assigned directly, or an ``InsuranceClaim`` allows its
status to be changed to an impossible value. If the object owns the rule, its
public operations should make invalid transitions difficult or impossible.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Animal:
    """
    Represent an animal whose weight rule can be bypassed after construction.

    ``__post_init__`` validates the initial value, but ``weight_kg`` remains
    freely assignable. This means the object cannot guarantee that its own
    invariant remains true after it has been created.
    """

    name: str
    species: str
    weight_kg: float

    def __post_init__(self) -> None:
        """Reject an invalid initial weight."""
        if self.weight_kg <= 0:
            raise ValueError("weight_kg must be greater than zero")


def main() -> None:
    """Run the unprotected-state example."""
    animal = Animal(
        name="Leo",
        species="Lion",
        weight_kg=190.0,
    )

    print("Initially valid:")
    print(f"{animal.name}: {animal.weight_kg} kg")

    animal.weight_kg = -25.0

    print()
    print("After uncontrolled assignment:")
    print(f"{animal.name}: {animal.weight_kg} kg")


if __name__ == "__main__":
    main()
