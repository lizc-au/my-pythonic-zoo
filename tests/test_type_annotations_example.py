"""
test_type_annotations_example.py
"""

from pythonic_thinking.type_system.type_annotations_example import (
    FrameworkRecord,
    UserRecord,
    ZooAnimal,
    describe_assignment,
    main,
)


def test_framework_subclass_preserves_attribute_contract() -> None:
    """
    Verify the subclass supplies a value without changing the base attribute shape.
    """
    assert FrameworkRecord.table_name == "records"
    assert UserRecord.table_name == "users"


def test_describe_assignment_accepts_animal_or_none() -> None:
    """Verify the optional annotation supports both valid value forms."""
    animal = ZooAnimal()

    assert describe_assignment(animal) == "Animal assigned."
    assert describe_assignment(None) == "No animal assigned."


def test_type_annotations_example_output(capsys) -> None:
    """Verify the exhibit explains the key typing lessons."""
    main()
    output = capsys.readouterr().out

    assert "ClassVar[str]" in output
    assert "incompatible-override diagnostic" in output
    assert 'Optional["ZooAnimal"]' in output
    assert "strictest-looking one" in output
