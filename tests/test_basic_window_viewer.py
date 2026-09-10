"""
test_basic_window_viewer.py

Unit tests for the Basic Window Viewer text processing engine.
Use `# type: ignore[arg-type]` as signal to mypy to allow deliberate invalid tests,
  i.e. ignore type checking specific lines for argument type mismatches.
"""

import unittest
from unittest.mock import patch

from native_gui.basic_window_viewer import create_terminal_box, main


class TestBasicWindowViewer(unittest.TestCase):
    """Test suite ensuring dynamic text padding boxes render flawlessly."""

    def test_basic_text_box(self):
        """Test wrapping a single line of text into a box structure."""
        text = "Hello You!"
        result = create_terminal_box(text, padding=1)  # type: ignore[arg-type]

        # Split lines to inspect the output layout rows cleanly
        lines = result.splitlines()

        # Check boundaries and width (11 chars + 2 padding + 2 borders = 15)
        self.assertEqual(lines[0], "+------------+")
        self.assertEqual(lines[1], "|            |")
        self.assertEqual(lines[2], "| Hello You! |")
        self.assertEqual(lines[3], "|            |")
        self.assertEqual(lines[4], "+------------+")

    def test_empty_input_handling(self):
        """Test graceful error message feedback for empty or layout strings."""
        result = create_terminal_box("   \n  \n ")  # type: ignore[arg-type]
        self.assertEqual(result, "Error: Text payload cannot be empty.")

    def test_invalid_type_defensiveness(self):
        """Test intercepting bad structural data types cleanly."""
        result = create_terminal_box(42)  # type: ignore[arg-type]
        self.assertIn("Error: Input must be a string", result)

    @patch("native_gui.basic_window_viewer.display_in_window")
    def test_main_prepares_and_displays_viewer(self, mock_display):
        """Test that main prepares the content and delegates to the GUI display."""
        main()

        mock_display.assert_called_once()
        self.assertEqual(mock_display.call_args.kwargs["title"], "The Zen of Python")
        self.assertIn(
            "Beautiful is better than ugly.", mock_display.call_args.kwargs["content"]
        )


if __name__ == "__main__":
    unittest.main()
