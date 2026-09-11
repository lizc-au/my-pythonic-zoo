"""
test_dialogs_multistep.py
"""

from unittest.mock import Mock, patch

from native_gui.dialogs_multistep import request_zoo_visit


@patch("native_gui.dialogs_multistep.ask_visit_decision", return_value=True)
def test_request_zoo_visit_handles_yes(
    _mock_decision: Mock,
) -> None:
    """Verify Yes advances the workflow to a requested state."""
    root = Mock()
    status_label = Mock()

    request_zoo_visit(root, status_label)

    status_label.config.assert_called_once_with(text="Zoo visit requested.")


@patch("native_gui.dialogs_multistep.ask_visit_decision", return_value=False)
def test_request_zoo_visit_handles_no(
    _mock_decision: Mock,
) -> None:
    """Verify No records an explicit declined state."""
    root = Mock()
    status_label = Mock()

    request_zoo_visit(root, status_label)

    status_label.config.assert_called_once_with(text="Zoo visit declined.")


@patch("native_gui.dialogs_multistep.ask_visit_decision", return_value=None)
def test_request_zoo_visit_handles_cancel(
    _mock_decision: Mock,
) -> None:
    """Verify Cancel leaves the existing interface state unchanged."""
    root = Mock()
    status_label = Mock()

    request_zoo_visit(root, status_label)

    status_label.config.assert_not_called()
