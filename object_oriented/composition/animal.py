"""
Animal object used by the Composition example.

This example models an animal as an object that *has* a movement behaviour.
The animal does not inherit movement implementation from a specialised base
class. Instead, a compatible ``Movement`` object is supplied when the animal is
created.

This keeps the animal focused on representing the animal itself while allowing
movement behaviour to vary independently.

Benefits
--------
- Behaviour can be replaced without changing the animal class.
- Multiple animal types can reuse the same behaviour object type.
- The design avoids inheritance hierarchies created only to represent behaviour
  combinations.
- The animal depends on a small behavioural contract rather than a concrete
  movement implementation.

When not to use this approach
-----------------------------
If the behaviour is fixed, trivial, and inseparable from the object, a separate
composed object may add unnecessary complexity.

See ``object_oriented/GLOSSARY.md`` for composition, dependency, behaviour,
Protocol, coupling, and inheritance.
"""

from dataclasses import dataclass

from object_oriented.composition.behaviours.movement import Movement


@dataclass(slots=True, frozen=True)
class Animal:
    """Represent an animal composed with a movement behaviour."""

    species: str
    movement: Movement

    def describe_movement(self) -> str:
        """Return a sentence describing how this animal moves."""
        article = "An" if self.species[0].lower() in "aeiou" else "A"
        return f"{article} {self.species.lower()} {self.movement.description()}."
