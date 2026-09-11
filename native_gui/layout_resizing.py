"""
layout_resizing.py

Demonstrate layout management and responsive resizing with Tkinter.

The interface uses Frame widgets to separate controls from content, while
Tkinter's grid geometry manager arranges those regions into rows and columns.
Row and column weights determine which parts of the interface receive extra
space when the window is resized.

In a business application, the same layout pattern appears in interfaces with a
navigation or action panel beside a larger work area, such as a document viewer,
claims dashboard, email client, or approval screen.
"""

import tkinter as tk


def main() -> None:
    """Create and run the Layout & Resizing demonstration."""
    root = tk.Tk()
    root.title("Zoo Layout & Resizing")
    root.geometry("640x360")

    # Give the content row and details column a share of any extra window space.
    # Other rows and columns keep the default weight of 0, so they do not expand.
    # Relative weights divide extra space: weight=2 would receive twice the share
    # of a comparable row or column configured with weight=1.
    root.rowconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    # Group the animal controls into a narrow panel on the left.
    animal_frame = tk.Frame(root, padx=16, pady=16)
    animal_frame.grid(row=0, column=0, sticky="ns")

    # Give the larger details area the remaining available space.
    details_frame = tk.Frame(root, padx=16, pady=16)

    # Stretch this frame to every edge of its grid cell: north, south, east,
    # and west. Without `sticky`, the widget keeps only its requested size.
    details_frame.grid(row=0, column=1, sticky="nsew")

    # A Frame manages its own grid independently, so configure its content row
    # and column to pass the extra space on to the Text widget inside it.
    details_frame.rowconfigure(1, weight=1)
    details_frame.columnconfigure(0, weight=1)

    animal_heading = tk.Label(animal_frame, text="Animals")
    animal_heading.grid(row=0, column=0, sticky="w", pady=(0, 12))

    for row, animal_name in enumerate(
        ("Python", "Panda", "Lion", "Elephant"),
        start=1,
    ):
        animal_label = tk.Label(animal_frame, text=animal_name)
        animal_label.grid(row=row, column=0, sticky="w", pady=4)

    details_heading = tk.Label(details_frame, text="Animal Details")
    details_heading.grid(row=0, column=0, sticky="w", pady=(0, 12))

    details_text = tk.Text(details_frame, wrap="word")
    details_text.insert(
        "1.0",
        "Resize this window.\n\n"
        "The animal list remains narrow while this details area expands "
        "to use the additional space.",
    )
    details_text.config(state="disabled")
    details_text.grid(row=1, column=0, sticky="nsew")

    root.mainloop()


if __name__ == "__main__":
    main()
