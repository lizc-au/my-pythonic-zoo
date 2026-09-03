"""
Animal protocol used by the Factory Pattern example.

The factory needs a stable contract for the objects it creates, but the
concrete animal classes do not need to share implementation or inherit from
a common base class.

A Protocol is a good fit because it describes required behaviour rather than
an inheritance hierarchy. Any object that provides a compatible ``speak()``
method satisfies the Animal contract.

Benefits
--------
- Concrete classes remain independent and focused.
- Client code depends on behaviour rather than implementation.
- New animal classes can satisfy the contract without inheriting from Animal.
- Type checkers can verify that factory-created objects provide ``speak()``.

When not to use this approach
-----------------------------
Prefer an abstract base class when related classes genuinely need shared
implementation, enforced inherited behaviour, or common state. A Protocol is
most useful when the important relationship is "can do this" rather than
"is derived from this".
"""

from typing import Protocol


class Animal(Protocol):
    """
    Define the behaviour required of animals created by this factory.

    This Factory example intentionally models only the behaviour required by the
    factory's returned objects: an animal must provide ``speak()``.

    For objects with multiple or changeable behaviours, see the Composition
    examples, where behaviours are modelled separately and combined with objects
    that use them.

    For descriptive differences between objects, such as species or subspecies,
    see the Domain Modelling examples. They demonstrate when a difference should
    be represented as data and when it justifies a separate type.

    For deciding which object should own a responsibility, see the Responsibilities
    and Collaboration examples. They demonstrate how focused objects collaborate
    without allowing one class to accumulate unrelated concerns.

    The ``...`` in ``speak()`` is Python's Ellipsis literal. Here it indicates that
    the Protocol defines the method signature but provides no implementation.
    The concrete animal classes provide the actual ``speak()`` behaviour.
    """

    def speak(self) -> None:
        """Display one sound made by the animal."""
        ...
