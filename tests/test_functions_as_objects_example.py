"""
test_functions_as_objects_example.py
"""

from pythonic_thinking.mental_model.functions_as_objects_example import main


def test_functions_as_objects_output(capsys) -> None:
    """Verify the exhibit demonstrates core function-object behaviour."""
    main()
    output = capsys.readouterr().out

    assert "lion_sound is same_function: True" in output
    assert "python_sound(): Hiss!" in output
    assert "panda_sound(): Bleat!" in output
    assert "lion_sound(): Roar!" in output
    assert "selected_sound is panda_sound: True" in output
    assert "selected_sound(): Bleat!" in output
