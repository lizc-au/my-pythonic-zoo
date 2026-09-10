"""
test_button_event_handling.py
"""

from unittest.mock import Mock

from native_gui.button_event_handling import (
    INITIAL_MESSAGE,
    reset_message,
    show_lion_sound,
)


def test_show_lion_sound_updates_message_and_buttons() -> None:
    """Verify the lion callback updates the message and swaps the buttons."""
    message_label = Mock()
    lion_button = Mock()
    done_button = Mock()

    show_lion_sound(message_label, lion_button, done_button)

    message_label.config.assert_called_once_with(text="Lion says: Roar!")
    lion_button.pack_forget.assert_called_once()
    done_button.pack.assert_called_once_with(padx=20, pady=(0, 20))


def test_reset_message_restores_initial_state() -> None:
    """Verify the Done callback restores the initial message and button state."""
    message_label = Mock()
    lion_button = Mock()
    done_button = Mock()

    reset_message(message_label, lion_button, done_button)

    message_label.config.assert_called_once_with(text=INITIAL_MESSAGE)
    done_button.pack_forget.assert_called_once()
    lion_button.pack.assert_called_once_with(padx=20, pady=(0, 20))
