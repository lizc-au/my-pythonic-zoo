"""
launch_tkinter_showcase.pyw

Provide a Windows no-console entry point for the Tkinter showcase exhibit.

The application logic remains in `tkinter_showcase.py`, while this small launcher
delegates startup to its reusable `main()` function.
"""

from tkinter_showcase import main

if __name__ == "__main__":
    main()
