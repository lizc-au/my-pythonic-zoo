"""
test_iteration_example.py
"""

from pythonic_thinking.mental_model.iteration_example import main


def test_iteration_output(capsys) -> None:
    """Verify the exhibit demonstrates iteration, exhaustion, and for-loop use."""
    main()

    output = capsys.readouterr().out

    assert "animals iterable type: list" in output
    assert "animal_iterator type: list_iterator" in output
    assert "iterable is iterator: False" in output
    assert "next(animal_iterator) first value: python" in output
    assert "StopIteration: iterator exhausted" in output
    assert "first value from a fresh iterator: python" in output
    assert "For normal iteration, prefer a `for` loop." in output
