"""
inappropriate_inheritance_example.py

Show why inheritance is a poor fit when it is used only to share behaviour.

Inheritance is most useful when a subclass represents a meaningful specialised
form of its base class and can be used wherever that base type is expected.

A common mistake is to create inheritance hierarchies around capabilities simply
because several objects happen to share the same behaviour.

This example models movement that way:

``WalkingAnimal`` and ``SlitheringAnimal`` are treated as base classes, and
specific animals inherit from them.

The design works mechanically, but the hierarchy expresses the wrong idea.
Walking and slithering are capabilities, not the essential type of the animal.
Movement can also vary independently of other animal characteristics, which
makes composition a better fit.

This matters because inheritance creates a strong relationship between types.
Using it merely to reuse code can make later changes awkward. If an animal gains
another movement capability, changes movement during its lifetime, or requires
several independent behaviours, the hierarchy becomes increasingly difficult
to represent accurately.

The [Composition examples](../composition/README.md) show the richer design:
``Animal`` collaborates with a ``Movement`` object rather than inheriting from a
movement-based superclass.

Only two animals are needed here because the purpose is to expose the design
problem rather than demonstrate the complete zoo.

A similar mistake appears in business software when classes such as
``EmailDocument`` and ``PrintedDocument`` inherit from delivery mechanisms even
though delivery is only one capability of a document. The same concern often
belongs in a collaborator rather than in the object's inheritance hierarchy.
"""


class WalkingAnimal:
    """Provide movement behaviour through inheritance."""

    name: str

    def move(self) -> str:
        """Describe walking movement."""
        return "Walk"


class SlitheringAnimal:
    """Provide movement behaviour through inheritance."""

    name: str

    def move(self) -> str:
        """Describe slithering movement."""
        return "Slither"


class Panda(WalkingAnimal):
    """Represent a panda whose movement comes from its superclass."""

    name = "Panda"


class Python(SlitheringAnimal):
    """Represent a python whose movement comes from its superclass."""

    name = "Python"


def describe_movement(animal: WalkingAnimal | SlitheringAnimal) -> str:
    """Describe how an animal moves."""
    return f"{animal.name}: {animal.move()}"


def main() -> None:
    """Run the inappropriate inheritance example."""
    animals = (Panda(), Python())

    print("Movement Modelled Through Inheritance")
    print()

    for animal in animals:
        print(describe_movement(animal))


if __name__ == "__main__":
    main()
