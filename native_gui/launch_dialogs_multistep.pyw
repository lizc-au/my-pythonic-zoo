"""
launch_dialogs_multistep.pyw

Provide a Windows no-console entry point for the Dialogs & Multi-step
Interaction exhibit.

The application logic remains in `dialogs_multistep.py`, while this small
launcher delegates startup to its reusable `main()` function.
"""

from dialogs_multistep import main

if __name__ == "__main__":
    main()
