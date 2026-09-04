"""
test_inappropriate_inheritance_example.py

Tests for the inappropriate inheritance example.

These tests deliberately verify the mechanics of the design. They don't claim the
hierarchy is good - that distinction will be important in the inheritance README.
"""

from object_oriented.inheritance.inappropriate_inheritance_example import (
    Panda,
    Python,
    SlitheringAnimal,
    WalkingAnimal,
    describe_movement,
)


def test_panda_inherits_walking_behaviour() -> None:
    animal = Panda()

    assert isinstance(animal, WalkingAnimal)
    assert animal.move() == "Walk"


def test_python_inherits_slithering_behaviour() -> None:
    animal = Python()

    assert isinstance(animal, SlitheringAnimal)
    assert animal.move() == "Slither"


def test_describe_movement_uses_inherited_behaviour() -> None:
    assert describe_movement(Panda()) == "Panda: Walk"
    assert describe_movement(Python()) == "Python: Slither"
