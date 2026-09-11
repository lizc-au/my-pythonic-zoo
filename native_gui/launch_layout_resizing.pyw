"""
launch_layout_resizing.pyw

Provide a Windows no-console entry point for the Layout & Resizing exhibit.

The application logic remains in `layout_resizing.py`, while this small launcher
delegates startup to its reusable `main()` function.
"""

from layout_resizing import main

if __name__ == "__main__":
    main()
