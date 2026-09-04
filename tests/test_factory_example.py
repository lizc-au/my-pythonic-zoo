"""
test_factory_example.py

Tests for the runnable Factory Pattern example.

These tests verify the client-side orchestration in ``factory_example.py``.
The factory's own selection and error behaviour is tested separately in
``test_animal_factory.py``.
"""

import pytest

from object_oriented.factory.factory_example import main


def test_main_runs_all_registered_animals(capsys: pytest.CaptureFixture[str]) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == ("Hiss!\nBleat!\nRoar!\nTrumpet!\n")
