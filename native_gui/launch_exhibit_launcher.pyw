"""
launch_exhibit_launcher.pyw

Provide a Windows no-console entry point for the Native GUI Exhibit Launcher.

The application logic remains in `exhibit_launcher.py`, while this small launcher
delegates startup to its reusable `main()` function.
"""

from exhibit_launcher import main

if __name__ == "__main__":
    main()
