"""
button_event_handling.py

Demonstrate basic event-driven GUI programming with Tkinter.

A GUI does not usually run from top to bottom and then exit. Instead, it builds
the interface, enters Tkinter's event loop, and waits for user actions such as
button clicks. A button's `command` receives a function object to call later;
the function is passed without parentheses because it should not run while the
button is being created.

For a fuller explanation of why functions can be passed without calling them,
and how `lambda` creates a short function object for use as a callback adapter,
see `pythonic_thinking/mental_model/functions_as_objects_example.py`.

In a business application, the same pattern appears when a user clicks actions
such as Approve, Reject, Save, or Submit. The interface connects each event to
the function responsible for handling that action.
"""

import tkinter as tk

INITIAL_MESSAGE = "Click the button to hear from the lion."


def show_lion_sound(
    message_label: tk.Label,
    lion_button: tk.Button,
    done_button: tk.Button,
) -> None:
    """Show the lion message and replace the action button with Done."""
    message_label.config(text="Lion says: Roar!")
    lion_button.pack_forget()
    done_button.pack(padx=20, pady=(0, 20))


def reset_message(
    message_label: tk.Label,
    lion_button: tk.Button,
    done_button: tk.Button,
) -> None:
    """Restore the initial instruction and button state."""
    message_label.config(text=INITIAL_MESSAGE)
    done_button.pack_forget()
    lion_button.pack(padx=20, pady=(0, 20))


def main() -> None:
    """Create and run the Button & Event Handling demonstration."""

    # Create the application's main window, the root of its widget hierarchy.
    root = tk.Tk()
    root.title("Zoo Button Events")

    # Create a Label widget from Tkinter and make the root window its parent.
    message_label = tk.Label(root, text=INITIAL_MESSAGE)

    # Ask Tkinter's pack geometry manager to position the label in its parent.
    message_label.pack(padx=20, pady=20)

    # Create a Button whose command is a function object Tkinter can call later.
    # The lambda adapts our argument-taking handler to Tkinter's no-argument command.
    lion_button = tk.Button(
        root,
        text="Meet the Lion",
        command=lambda: show_lion_sound(message_label, lion_button, done_button),
    )

    # Position the button below the label with some surrounding space.
    lion_button.pack(padx=20, pady=(0, 20))

    # Create the Done button that will be shown after the lion event.
    done_button = tk.Button(
        root,
        text="Done",
        command=lambda: reset_message(message_label, lion_button, done_button),
    )
    done_button.pack(padx=20, pady=(0, 20))

    # Remove the Done button from the layout until the first event needs it.
    done_button.pack_forget()

    # Preserve the interface's initial natural size when its text later changes.
    root.update_idletasks()
    root.minsize(root.winfo_width(), root.winfo_height())

    # Hand control to Tkinter, which now waits for and dispatches GUI events.
    root.mainloop()


if __name__ == "__main__":
    main()
