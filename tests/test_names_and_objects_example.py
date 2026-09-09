"""
test_names_and_objects_example.py
"""

from pythonic_thinking.mental_model.names_and_objects_example import main


def test_names_and_objects_output(capsys) -> None:
    """
    Verify the exhibit demonstrates shared identity and equal-but-distinct objects.
    """
    main()

    output = capsys.readouterr().out

    assert "animal is first_name:  True" in output
    assert "animal is second_name: True" in output
    assert "first_name is second_name: True" in output
    assert "animal == other_animal: True" in output
    assert "animal is other_animal: False" in output
