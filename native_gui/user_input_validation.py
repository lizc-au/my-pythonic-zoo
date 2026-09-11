"""
user_input_validation.py

Demonstrate user input and validation with Tkinter.

The user enters an animal name into an Entry widget and submits it for checking.
The application reads the current widget value, validates it, normalises it, and
updates the interface with an appropriate response.

In a business application, the same pattern appears when a user enters data such
as a customer reference, claim number, email address, or approval code. The
interface collects the value, checks whether it is usable, and gives feedback
before later application logic acts on it.
"""

import tkinter as tk

ANIMAL_SOUNDS = {
    "python": "Hiss!",
    "panda": "Bleat!",
    "lion": "Roar!",
    "elephant": "Trumpet!",
}


def normalise_animal_name(raw_name: str) -> str:
    """Return an animal name with surrounding whitespace removed and case normalised."""
    return raw_name.strip().casefold()


def validate_animal_name(raw_name: str) -> str:
    """Return feedback for an entered animal name."""

    # Remember to normalise inputs
    animal_name = normalise_animal_name(raw_name)

    if not animal_name:
        return "Please enter an animal name."

    sound = ANIMAL_SOUNDS.get(animal_name)
    if sound is None:
        return "That animal is not in this zoo."

    return f"{animal_name.title()} says: {sound}"


def check_animal(animal_entry: tk.Entry, result_label: tk.Label) -> None:
    """Read and validate the current animal Entry value, then show the result."""
    raw_name = animal_entry.get()
    result_label.config(text=validate_animal_name(raw_name))

    if normalise_animal_name(raw_name) in ANIMAL_SOUNDS:
        animal_entry.delete(0, tk.END)


def main() -> None:
    """Create and run the User Input & Validation demonstration."""
    root = tk.Tk()
    root.title("Zoo Animal Checker")

    instruction_label = tk.Label(
        root,
        text="Enter Python, Panda, Lion, or Elephant:",
    )
    instruction_label.pack(padx=20, pady=(20, 8))

    animal_entry = tk.Entry(root)
    animal_entry.pack(padx=20, pady=(0, 12))

    result_label = tk.Label(root, text="")
    result_label.pack(padx=20, pady=(0, 12))

    check_button = tk.Button(
        root,
        text="Check Animal",
        command=lambda: check_animal(animal_entry, result_label),
    )
    check_button.pack(padx=20, pady=(0, 20))

    # Bind the Enter key to the same action as the button. Tkinter passes an
    # event object to bound callbacks; `_event` shows that we intentionally ignore it.
    animal_entry.bind(
        "<Return>",
        lambda _event: check_animal(animal_entry, result_label),
    )

    # Give the Entry keyboard focus when the window opens so the user can
    # start typing immediately without first clicking inside the field.
    animal_entry.focus_set()

    root.mainloop()


if __name__ == "__main__":
    main()
