"""
launch_window.pyw

Autonomous launcher for the Basic Window Viewer desktop application.
"""

from basic_window_viewer import (
    ZEN_OF_PYTHON,
    create_terminal_box,
    display_in_window,
)

if __name__ == "__main__":
    # Generate the layout matrix
    boxed_output = create_terminal_box(ZEN_OF_PYTHON)

    # Initialize the desktop window autonomously without opening a terminal console
    display_in_window(title="The Zen of Python", content=boxed_output)
