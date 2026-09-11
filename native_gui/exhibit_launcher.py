"""
exhibit_launcher.py

Provide a single graphical launcher for the Native GUI exhibits.

Each exhibit runs in its own Python process so its Tkinter root window and event
loop remain independent from the launcher.

The launcher deliberately hides while an exhibit is open and returns when that
exhibit closes. This one-at-a-time navigation keeps the separate exhibit windows
from competing for attention; a persistent launcher or in-window navigation
would be an equally valid design for a different application.

In a larger application, a similar launcher might provide access to separate
utilities, administration tools, reports, or other independently running
desktop applications.
"""

import subprocess
import sys
import tkinter as tk
from functools import partial
from pathlib import Path

EXHIBIT_DIRECTORY = Path(__file__).parent

EXHIBITS = (
    ("Basic Window Viewer", "basic_window_viewer.py"),
    ("Button & Event Handling", "button_event_handling.py"),
    ("User Input & Validation", "user_input_validation.py"),
    ("Layout & Resizing", "layout_resizing.py"),
    ("Dialogs & Multi-step Interaction", "dialogs_multistep.py"),
)

running_exhibits: dict[str, subprocess.Popen[bytes]] = {}


def launch_exhibit(root: tk.Tk, filename: str) -> None:
    """Close any open exhibit, then launch the selected exhibit."""
    # The launcher could keep multiple exhibits open, but using one active
    # exhibit at a time keeps navigation predictable and avoids window clutter.
    for process in running_exhibits.values():
        if process.poll() is None:
            process.terminate()
            process.wait()

    running_exhibits.clear()

    exhibit_path = EXHIBIT_DIRECTORY / filename
    process = subprocess.Popen([sys.executable, str(exhibit_path)])
    running_exhibits[filename] = process

    root.withdraw()
    wait_for_exhibit(root, process)


def close_launcher(root: tk.Tk) -> None:
    """Close any running exhibits, then close the launcher."""
    for process in running_exhibits.values():
        if process.poll() is None:
            process.terminate()

    root.destroy()


def wait_for_exhibit(root: tk.Tk, process: subprocess.Popen[bytes]) -> None:
    """Restore the launcher after the active exhibit closes."""

    # Check periodically with Tkinter's event scheduler rather than calling
    # process.wait(), which would block the event loop and freeze the launcher.
    if process.poll() is None:
        root.after(200, lambda: wait_for_exhibit(root, process))
        return

    root.deiconify()


def main() -> None:
    """Create and run the Native GUI Exhibit Launcher."""
    root = tk.Tk()
    root.title("Native GUI Exhibits")

    heading = tk.Label(root, text="Choose a Native GUI exhibit")
    heading.pack(padx=24, pady=(24, 12))

    # partial() creates each button callback with its arguments already bound.
    # A default-argument lambda can also capture the current loop value, but
    # partial() expresses that intention directly and is easier to type-check.
    for exhibit_name, filename in EXHIBITS:
        button = tk.Button(
            root,
            text=exhibit_name,
            width=30,
            command=partial(launch_exhibit, root, filename),
        )
        button.pack(padx=24, pady=4)

    close_button = tk.Button(
        root, text="Close Launcher", command=lambda: close_launcher(root)
    )
    close_button.pack(padx=24, pady=(12, 24))

    root.mainloop()


if __name__ == "__main__":
    main()
