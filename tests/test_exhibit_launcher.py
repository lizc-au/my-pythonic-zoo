"""
test_exhibit_launcher.py
"""

from unittest.mock import Mock, patch

from native_gui.exhibit_launcher import (
    close_launcher,
    launch_exhibit,
    running_exhibits,
)


@patch("native_gui.exhibit_launcher.subprocess.Popen")
def test_launch_exhibit_restarts_selection_and_hides_launcher(mock_popen: Mock) -> None:
    """Verify selecting an exhibit starts it and hides the launcher window."""
    root = Mock()
    process = mock_popen.return_value
    running_exhibits.clear()

    launch_exhibit(root, "button_event_handling.py")

    mock_popen.assert_called_once()
    root.withdraw.assert_called_once()
    assert running_exhibits["button_event_handling.py"] is process


@patch("native_gui.exhibit_launcher.subprocess.Popen")
def test_launch_exhibit_closes_existing_exhibit(mock_popen: Mock) -> None:
    """Verify selecting another exhibit closes the currently running one."""
    root = Mock()
    existing_process = Mock()
    existing_process.poll.return_value = None
    running_exhibits.clear()
    running_exhibits["button_event_handling.py"] = existing_process

    launch_exhibit(root, "layout_resizing.py")

    existing_process.terminate.assert_called_once()
    existing_process.wait.assert_called_once()
    assert "button_event_handling.py" not in running_exhibits
    assert "layout_resizing.py" in running_exhibits


def test_close_launcher_terminates_running_exhibits() -> None:
    """Verify launcher shutdown closes active exhibits before destroying itself."""
    root = Mock()
    process = Mock()
    process.poll.return_value = None
    running_exhibits.clear()
    running_exhibits["layout_resizing.py"] = process

    close_launcher(root)

    process.terminate.assert_called_once()
    root.destroy.assert_called_once()
