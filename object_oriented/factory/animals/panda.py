"""
Panda implementation used by the Factory Pattern example.

Panda is a concrete animal class. It provides the ``speak()`` behaviour
required by the Animal Protocol without explicitly inheriting from Animal.

This demonstrates structural typing: the class satisfies the protocol because
it provides the required behaviour, rather than inheriting from a particular
base class as it would with nominal typing.
"""


class Panda:
    """
    Represent a panda satisfying this example's ``Animal`` contract.

    See ``factory.animals.animal.Animal`` for scope and related use cases.
    """

    def speak(self) -> None:
        """Display one sound made by this panda."""
        print("Bleat!")
