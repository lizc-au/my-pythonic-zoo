"""
test_layout_resizing.py
"""

from unittest.mock import Mock, patch

from native_gui.layout_resizing import main


@patch("native_gui.layout_resizing.tk.Text")
@patch("native_gui.layout_resizing.tk.Label")
@patch("native_gui.layout_resizing.tk.Frame")
@patch("native_gui.layout_resizing.tk.Tk")
def test_main_configures_resizable_root_grid(
    mock_tk: Mock,
    _mock_frame: Mock,
    _mock_label: Mock,
    _mock_text: Mock,
) -> None:
    """
    Verify the main window gives extra space to the content row and details column.
    """
    root = mock_tk.return_value

    main()

    root.rowconfigure.assert_called_once_with(0, weight=1)
    root.columnconfigure.assert_called_once_with(1, weight=1)


@patch("native_gui.layout_resizing.tk.Text")
@patch("native_gui.layout_resizing.tk.Label")
@patch("native_gui.layout_resizing.tk.Frame")
@patch("native_gui.layout_resizing.tk.Tk")
def test_details_area_stretches_with_available_space(
    mock_tk: Mock,
    mock_frame: Mock,
    _mock_label: Mock,
    mock_text: Mock,
) -> None:
    """Verify the details frame and Text widget stretch within their grid cells."""
    details_frame = Mock()
    mock_frame.side_effect = [Mock(), details_frame]
    details_text = mock_text.return_value

    main()

    details_frame.grid.assert_called_once_with(row=0, column=1, sticky="nsew")
    details_frame.rowconfigure.assert_called_once_with(1, weight=1)
    details_frame.columnconfigure.assert_called_once_with(0, weight=1)
    details_text.grid.assert_called_once_with(row=1, column=0, sticky="nsew")
