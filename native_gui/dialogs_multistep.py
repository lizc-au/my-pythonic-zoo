"""
dialogs_multistep.py

Demonstrate dialogs and simple multi-step interaction with Tkinter.

The main window starts an action, then a modal confirmation dialog asks the user
whether to continue. The result of that dialog determines whether the interface
advances to a completed state or remains unchanged.

In a business application, the same pattern appears when a user confirms a
submission, approves a transaction, deletes a record, or cancels an operation
before the application commits the change.
"""

import tkinter as tk
from tkinter import messagebox


def ask_visit_decision(root: tk.Tk) -> bool | None:
    """Ask whether to request a zoo visit and return the user's decision."""

    # Tkinter provides fixed dialog APIs such as askyesno(), askokcancel(),
    # askretrycancel(), etc. and this three-choice askyesnocancel(). Here
    # Yes returns True, No returns False, and Cancel returns None.
    return messagebox.askyesnocancel(
        title="Confirm Zoo Visit",
        message="Would you like to request a zoo visit?",
        parent=root,
    )


def request_zoo_visit(root: tk.Tk, status_label: tk.Label) -> None:
    """
    Ask for confirmation and update the interface only when confirmed.

    The root window is passed explicitly so it can own the modal dialog,
    keeping the dialog associated with the application window.
    """

    confirmed = ask_visit_decision(root)

    if confirmed is None:
        return

    if confirmed:
        status_label.config(text="Zoo visit requested.")
    else:
        status_label.config(text="Zoo visit declined.")


def main() -> None:
    """Create and run the Dialogs & Multi-step Interaction demonstration."""
    root = tk.Tk()
    root.title("Zoo Visit Request")

    instruction_label = tk.Label(
        root,
        text="Request a zoo visit and confirm your choice.",
    )
    instruction_label.pack(padx=20, pady=(20, 12))

    status_label = tk.Label(root, text="")
    status_label.pack(padx=20, pady=(0, 12))

    request_button = tk.Button(
        root,
        text="Request Zoo Visit",
        command=lambda: request_zoo_visit(root, status_label),
    )
    request_button.pack(padx=20, pady=(0, 20))

    root.mainloop()


if __name__ == "__main__":
    main()
