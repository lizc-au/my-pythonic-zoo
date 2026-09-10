"""
launch_button_event_handling.pyw

Provide a Windows no-console entry point for the Button & Event Handling exhibit.

The application logic remains in `button_event_handling.py`, while this small
launcher delegates startup to its reusable `main()` function.
"""

from button_event_handling import main

if __name__ == "__main__":
    main()
