"""
launch_user_input_validation.pyw

Provide a Windows no-console entry point for the User Input & Validation exhibit.

The application logic remains in `user_input_validation.py`, while this small
launcher delegates startup to its reusable `main()` function.
"""

from user_input_validation import main

if __name__ == "__main__":
    main()
