"""
Animal types available to the Factory Pattern example.

This package exposes the ``Animal`` protocol and the concrete animal classes
through one stable import location. Code outside this package does not need to
know which module contains each concrete implementation.
"""

from .animal import Animal
from .elephant import Elephant
from .lion import Lion
from .panda import Panda
from .python import Python

__all__ = ["Animal", "Elephant", "Lion", "Panda", "Python"]
