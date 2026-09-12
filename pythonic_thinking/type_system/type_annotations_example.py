"""
type_annotations_example.py

A type annotation describes what kind of value Python code is expected to use
in a particular place, for example `str`, `int`, or `bool`. Annotations can
describe variables, function parameters, return values, class attributes, and
other parts of a program.

Python generally does not enforce these annotations at runtime; static type
checkers such as mypy and Pyright analyse them to find inconsistencies before
the program runs.

This example shows how type annotations describe expected contracts in the code,
rather than serving only as documentation for the reader.

Annotations such as `ClassVar`, forward references, and optional types affect how
static type checkers interpret code. A stricter annotation is not automatically
a better annotation: it must accurately describe how the attribute or value is
intended to behave.

Type-checker warnings should be investigated rather than satisfied at any cost.
Adding `None`, `ClassVar`, casts, ignores, or other typing constructs merely to
remove a warning can make an annotation less accurate. The goal is not simply
to produce zero diagnostics, but to describe the program's real contract as
accurately as possible.

Frameworks often use declarative class attributes and other runtime patterns
that do not map perfectly onto a type checker's model. When that happens, the
right response is to understand the annotation's meaning rather than changing
working code simply to silence a diagnostic.

Real-world analogue:
An application framework might inspect class attributes to configure database
tables, validation rules, routes, or serializers. Those attributes participate
in the framework's runtime protocol, while a static type checker separately
reasons about the contracts expressed by their annotations.
"""

from typing import ClassVar, Optional

# ========= Class attributes and ClassVar =========


class AnimalRecord:
    """Demonstrate an ordinary class attribute."""

    category = "animal"


class ZooConfiguration:
    """Demonstrate a value intended to exist only at class level."""

    organisation_name: ClassVar[str] = "Pythonic Zoo"


class FrameworkRecord:
    """Represent a framework base class that already defines an attribute contract."""

    table_name: str = "records"


class UserRecord(FrameworkRecord):
    """Follow the framework contract without unnecessarily narrowing the annotation."""

    table_name = "users"


# ========= Forward references =========


class Keeper:
    """Represent a keeper who may be assigned an animal."""

    def __init__(self, animal: "ZooAnimal | None" = None) -> None:
        self.animal = animal


class ZooAnimal:
    """Represent an animal that may have an assigned keeper."""

    def __init__(self, keeper: Keeper | None = None) -> None:
        self.keeper = keeper


def describe_assignment(animal: Optional["ZooAnimal"]) -> str:
    """Describe whether an optional animal assignment exists."""
    if animal is None:
        return "No animal assigned."

    return "Animal assigned."


# ========= Demonstrations =========


def demonstrate_class_attributes() -> None:
    """Show that ClassVar communicates a stronger typing contract."""

    print("\n=== DEMONSTRATION 1: Class attributes and ClassVar ===")

    print(f"\n    AnimalRecord.category: {AnimalRecord.category}")
    print(
        f"    ZooConfiguration.organisation_name: {ZooConfiguration.organisation_name}"
    )

    print(
        "\n    `ClassVar[str]` does more than document where a value happens to live."
    )
    print("    It tells a type checker that the attribute is intended for class-level")
    print("    use rather than ordinary per-instance assignment.")

    print("\n    Therefore, adding ClassVar simply to make an annotation look stricter")
    print("    can create an incorrect type contract for framework-managed attributes.")


def demonstrate_framework_attribute_contract() -> None:
    """Show why a subclass should preserve a framework attribute contract."""

    print("\n=== DEMONSTRATION 2: Framework attribute contracts ===")

    print(f"\n    FrameworkRecord.table_name: {FrameworkRecord.table_name!r}")
    print(f"    UserRecord.table_name: {UserRecord.table_name!r}")

    print(
        "\n    The base class already defines `table_name` "
        "as an ordinary `str` attribute."
    )
    print("    The subclass supplies a value without changing that typing contract.")
    print("    Redeclaring it as `ClassVar[str]` would describe a different contract")
    print("    and can trigger an incompatible-override diagnostic.")


def demonstrate_forward_references() -> None:
    """Show how quoted annotations can refer to types defined later."""

    print("\n=== DEMONSTRATION 3: Forward references ===")

    keeper = Keeper()
    animal = ZooAnimal(keeper=keeper)
    keeper.animal = animal

    print(f"\n    keeper.animal is animal: {keeper.animal is animal}")
    print(f"    animal.keeper is keeper: {animal.keeper is keeper}")

    print(f"\n    describe_assignment(animal): {describe_assignment(animal)}")
    print(f"    describe_assignment(None): {describe_assignment(None)}")

    print("\n    `Keeper` is defined before `ZooAnimal`, so its annotation uses")
    print('    the quoted forward reference `"ZooAnimal | None"`.')
    print('    The older `Optional["ZooAnimal"]` spelling expresses the same')
    print("    optional type: the value may be a ZooAnimal or None.")
    print("    The quote delays evaluation of that type name until it can be resolved.")


def demonstrate_type_checker_judgement() -> None:
    """Explain why satisfying a type checker is not the only design goal."""

    print("\n=== DEMONSTRATION 4: Type checkers describe a model ===")

    print("\n    A type checker analyses the contracts expressed by annotations.")
    print("    A framework may separately interpret class attributes at runtime.")
    print("    Those two models can occasionally disagree.")

    print("\n    When that happens:")
    print("    1. Check what the framework's supported API expects.")
    print("    2. Check what the annotation actually promises.")
    print(
        "    3. Prefer the most accurate contract, "
        "not merely the strictest-looking one."
    )
    print("    4. Suppress a checker diagnostic only when the mismatch is understood.")


# ========= Main =========


def main() -> None:
    """Run the type-annotation demonstrations."""
    demonstrate_class_attributes()
    demonstrate_framework_attribute_contract()
    demonstrate_forward_references()
    demonstrate_type_checker_judgement()
    print()


# ========= Module Entry Point =========

if __name__ == "__main__":
    main()
