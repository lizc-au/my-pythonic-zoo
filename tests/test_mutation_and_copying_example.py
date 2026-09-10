"""
test_mutation_and_copying_example.py
"""

from pythonic_thinking.mental_model.mutation_and_copying_example import main


def test_mutation_and_copying_output(capsys) -> None:
    """Verify the exhibit demonstrates rebinding, mutation, and copying."""
    main()

    output = capsys.readouterr().out

    assert "animals is first_name: True" in output
    assert "animals is first_name: False" in output
    assert "animals = ['lion', 'panda', 'elephant']" in output
    assert "animals[0] == shallow_copy[0] = True" in output
    assert "animals[0] is shallow_copy[0] = True" in output
    assert "animals[0] == deep_copy[0] = False" in output
    assert "animals[0] is deep_copy[0] = False" in output
