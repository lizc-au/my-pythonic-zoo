"""
test_tkinter_showcase.py

Most of the remaining behaviour is Tkinter widget orchestration already
exercised manually, no need to create brittle tests that merely mock every
widget call. The useful pure logic is covered.
"""

from native_gui.tkinter_showcase import normalise_animal_name


def test_normalise_animal_name_prepares_user_input_for_comparison() -> None:
    """Verify animal input is trimmed and case-normalised."""
    assert normalise_animal_name("  PANDA  ") == "panda"
