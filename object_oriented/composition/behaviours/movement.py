"""
Movement behaviours used by the Composition example.

This module demonstrates composition by modelling movement independently from
the animal that uses it.

An animal can *have* a ``Movement`` rather than inheriting its movement from a
base class. This becomes useful when behaviours can vary independently from the
main object or when different kinds of objects can share the same behaviour.

``Movement`` is a Protocol because the important relationship is behavioural:
a movement object must provide ``description()``, but implementations do not
need to share state or inherit from a common base class.

This terminal example exposes only a textual description of movement because
that is all the demonstration requires. In a larger application, a movement
behaviour might instead perform calculations, update state, issue commands, or
drive animation.

Benefits
--------
- Movement can vary independently from animal types.
- Different animals can reuse the same movement implementation.
- New movement behaviours can be added without modifying existing animals.
- Animal classes do not need an inheritance hierarchy for every combination of
  characteristics.

When not to use this approach
-----------------------------
Composition introduces another object and another relationship to understand.
If a behaviour is simple, fixed, and genuinely belongs entirely inside one
class, extracting it into a separate object may add unnecessary indirection.

See ``object_oriented/GLOSSARY.md`` for definitions of composition, behaviour,
Protocol, structural typing, and inheritance.
"""

from typing import Protocol


class Movement(Protocol):
    """Define the movement behaviour required by composing objects."""

    def description(self) -> str:
        """Return wording that describes this movement."""
        ...


class Slither:
    """Provide slithering movement."""

    def description(self) -> str:
        """Return wording describing slithering movement."""
        return "slithers"


class Walk:
    """Provide walking movement."""

    def description(self) -> str:
        """Return wording describing walking movement."""
        return "walks"
