"""
tkinter_showcase.py

Combine the Native GUI concepts into one small, template-like Tkinter application.

The application keeps its navigation visible while switching between content
views, demonstrating a persistent-window alternative to the separate exhibit
launcher.
"""

import tkinter as tk
from tkinter import messagebox

ANIMAL_SOUNDS = {
    "python": "Hiss!",
    "panda": "Bleat!",
    "lion": "Roar!",
    "elephant": "Trumpet!",
}


def normalise_animal_name(raw_name: str) -> str:
    """Return an animal name normalised for comparison."""
    return raw_name.strip().casefold()


def clear_content(content_frame: tk.Frame) -> None:
    """Remove the widgets belonging to the current view."""
    for widget in content_frame.winfo_children():
        widget.destroy()


def add_view_heading(
    content_frame: tk.Frame,
    text: str,
    *,
    columnspan: int = 1,
) -> None:
    """Add the standard heading used by application content views."""
    heading = tk.Label(
        content_frame,
        text=text,
        font=("TkDefaultFont", 16, "bold"),
    )
    heading.grid(row=0, column=0, columnspan=columnspan, pady=(0, 20))


def show_home(content_frame: tk.Frame) -> None:
    """Display the application home view."""
    clear_content(content_frame)

    add_view_heading(content_frame, "Pythonic Zoo")

    message = tk.Label(
        content_frame,
        text=(
            "Choose an option from the navigation panel.\n\n"
            "This application combines events, input validation, responsive "
            "layout, dialogs, and persistent navigation in one Tkinter window."
        ),
        justify="left",
        wraplength=460,
    )
    message.grid(row=1, column=0, sticky="new")
    message.bind("<Configure>", lambda event: message.config(wraplength=event.width))


def show_animal_checker(content_frame: tk.Frame) -> None:
    """Display an animal-input and validation view."""
    clear_content(content_frame)

    add_view_heading(content_frame, "Animal Checker", columnspan=2)

    prompt = tk.Label(content_frame, text="Enter Python, Panda, Lion, or Elephant:")
    prompt.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 8))

    animal_entry = tk.Entry(content_frame)
    animal_entry.grid(row=2, column=0, sticky="ew", padx=(0, 8))

    result_label = tk.Label(content_frame, text="")
    result_label.grid(row=3, column=0, columnspan=2, sticky="w", pady=(12, 0))

    def check_animal() -> None:
        animal_name = normalise_animal_name(animal_entry.get())

        if not animal_name:
            result_label.config(text="Please enter an animal name.")
            return

        sound = ANIMAL_SOUNDS.get(animal_name)
        if sound is None:
            result_label.config(text="That animal is not in this zoo.")
            return

        result_label.config(text=f"{animal_name.title()} says: {sound}")
        animal_entry.delete(0, tk.END)

    check_button = tk.Button(content_frame, text="Check", command=check_animal)
    check_button.grid(row=5, column=0, columnspan=2)

    animal_entry.bind("<Return>", lambda _event: check_animal())
    animal_entry.focus_set()

    content_frame.columnconfigure(0, weight=1)


def show_visit_request(root: tk.Tk, content_frame: tk.Frame) -> None:
    """Display a simple multi-step visit-request workflow."""
    clear_content(content_frame)

    add_view_heading(content_frame, "Zoo Visit Request")

    status_label = tk.Label(content_frame, text="")
    status_label.grid(row=2, column=0, sticky="w", pady=(12, 0))

    def request_visit() -> None:
        status_label.config(text="")
        decision = messagebox.askyesnocancel(
            title="Confirm Zoo Visit",
            message="Would you like to request a zoo visit?",
            parent=root,
        )

        if decision is None:
            return

        if decision:
            status_label.config(text="Zoo visit requested.")
        else:
            status_label.config(text="Zoo visit declined.")

    request_button = tk.Button(
        content_frame,
        text="Request Zoo Visit",
        command=request_visit,
    )
    request_button.grid(row=5, column=0)


def main() -> None:
    """Create and run the comprehensive Tkinter showcase."""
    root = tk.Tk()
    root.title("Pythonic Zoo - Tkinter Showcase")
    root.geometry("760x440")
    root.minsize(520, 320)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    navigation_frame = tk.Frame(root, padx=16, pady=16, relief="groove", borderwidth=2)
    navigation_frame.grid(row=0, column=0, sticky="ns")

    content_frame = tk.Frame(root, padx=24, pady=24, relief="groove", borderwidth=2)
    content_frame.grid(row=0, column=1, sticky="nsew")
    content_frame.columnconfigure(0, weight=1)
    content_frame.rowconfigure(4, weight=1)

    title_label = tk.Label(
        navigation_frame,
        text="Native GUI",
        font=("TkDefaultFont", 13, "bold"),
    )
    title_label.grid(row=0, column=0, pady=(0, 16))

    home_button = tk.Button(
        navigation_frame,
        text="Home",
        width=20,
        command=lambda: show_home(content_frame),
    )
    home_button.grid(row=1, column=0, sticky="ew", pady=4)

    checker_button = tk.Button(
        navigation_frame,
        text="Animal Checker",
        width=20,
        command=lambda: show_animal_checker(content_frame),
    )
    checker_button.grid(row=2, column=0, sticky="ew", pady=4)

    visit_button = tk.Button(
        navigation_frame,
        text="Visit Request",
        width=20,
        command=lambda: show_visit_request(root, content_frame),
    )
    visit_button.grid(row=3, column=0, sticky="ew", pady=4)

    exit_button = tk.Button(
        navigation_frame,
        text="Exit",
        width=20,
        command=root.destroy,
    )
    exit_button.grid(row=4, column=0, sticky="ew", pady=(16, 4))

    show_home(content_frame)

    root.mainloop()


if __name__ == "__main__":
    main()
