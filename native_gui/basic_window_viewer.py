"""
basic_window_viewer.py

Text Output Formatting and Graphical UI Module
---------------------------------------------
ENGINEERING PRINCIPLE: Standard Label widgets enforce uniform layouts. Utilizing
Text widgets with Tag mappings allows in-situ rich text modifications, such as
line highlighting and selective font styling, using native GUI frameworks.

See end of this file for autonomous `launch_window.pyw` requirement explanation.
"""

import tkinter as tk
from tkinter import font

ZEN_OF_PYTHON = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


def create_terminal_box(text: str, padding: int = 2) -> str:
    """Wraps a multi-line string payload into a dynamically sized terminal box."""
    if not isinstance(text, str):
        err_type = type(text).__name__
        return (
            f"Error: Input must be a string value (received: {err_type})."
        )

    lines = [line.rstrip() for line in text.strip().splitlines()]
    if not lines:
        return "Error: Text payload cannot be empty."

    max_line_len = len(max(lines, key=len))
    box_width = max_line_len + (padding * 2)
    horizontal_border = f"+{'-' * box_width}+"
    empty_padding = f"|{' ' * box_width}|"

    output_blocks = [horizontal_border, empty_padding]
    for line in lines:
        padded_text = line.ljust(max_line_len)
        spaces = " " * padding
        output_blocks.append(f"|{spaces}{padded_text}{spaces}|")

    output_blocks.extend([empty_padding, horizontal_border])
    return "\n".join(output_blocks)


def display_in_window(title: str, content: str) -> None:
    """Launches a native Tkinter window to display styled text."""
    root = tk.Tk()
    root.title(title)
    root.configure(bg="#1e1e1e")

    # Force the window dimensions
    root.geometry("740x500")

    # Define standard and bold monospaced variants
    base_font = font.Font(family="Courier", size=11, weight="normal")
    bold_font = font.Font(family="Courier", size=11, weight="bold")

    # Use a Text widget instead of a Label to allow multi-style content
    text_area = tk.Text(
        root,
        font=base_font,
        fg="#d4d4d4",      # Default light grey text
        bg="#1e1e1e",      # Dark mode background
        padx=20,
        pady=20,
        bd=0,              # Remove default border lines
        highlightthickness=0, # Clear window focal focus boxes
    )

    # Insert the raw boxed text payload
    text_area.insert(tk.INSERT, content)

    # Use expand and fill, and add external vertical padding to give it room
    text_area.pack(expand=True, fill=tk.BOTH, pady=(0, 25))

    # =================================================================
    # IN-SITU FORMATTING RULES (Defining "CSS-like" Tags)
    # =================================================================
    text_area.tag_config("title_style", foreground="#4fc1ff", font=bold_font)
    text_area.tag_config("border_style", foreground="#569cd6")
    text_area.tag_config("highlight_line", background="#2d2d2d", foreground="#ce9178")

    # =================================================================
    # APPLYING THE TAGS (Tkinter uses string indices: "line.character")
    # =================================================================
    # 1. Format the Box Borders (Line 1, Line 2, and the final 2 lines)
    # Tkinter text coordinates start at 1.0 (Line 1, Column 0)
    text_area.tag_add("border_style", "1.0", "3.0") # Lines 1 & 2

    # Target the last two border rows dynamically
    total_lines = int(text_area.index(tk.END).split(".")[0])
    text_area.tag_add("border_style", f"{total_lines - 3}.0", f"{total_lines}.0")

    # 2. Format the Header Line ("The Zen of Python, by Tim Peters")
    # It sits on line 3 (index 3.0), right after the top empty padding line
    text_area.tag_add("title_style", "3.0", "4.0")

    # 3. Highlight specific individual golden principles cleanly in-situ
    # Let's highlight "Readability counts." (Line 10)
    text_area.tag_add("highlight_line", "10.0", "11.0")

    # Let's highlight "Errors should never pass silently." (Line 13)
    text_area.tag_add("highlight_line", "13.0", "14.0")

    # Disable editing so users cannot modify the text block inside the UI
    text_area.config(state=tk.DISABLED)
    root.mainloop()

# =============================================================================
# ARCHITECTURAL NOTE: Why an execution block (`if __name__ == "__main__":`)
# belongs in an autonomous launcher (`launch_window.pyw`) rather than here:
#
# 1. Terminal Decoupling: Executing `.py` files forces the host operating
#    system to open and hold a captive terminal console window. Separating the
#    runtime hook into a `.pyw` extension tells Windows to run via pythonw.exe,
#    suppressing the console and allowing the UI window to run autonomously.
# 2. Test Suite Compatibility: Python cannot cleanly resolve standard module
#    namespace imports from `.pyw` target extensions during automated test runs.
#    Keeping core showcase logic in a standard `.py` module ensures it remains
#    fully visible, importable, and testable by our GitHub Actions gatekeepers.
# =============================================================================
