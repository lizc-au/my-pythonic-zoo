"""
email_validator.py

User Input Validation Module
----------------------------
ENGINEERING PRINCIPLE: Always validate data at the gate. Never pass raw user
inputs directly to systems or databases without confirming structural integrity
first.
"""


def validate_user_email(email: str) -> tuple[bool, str]:
    """Validates the structure of a user-submitted email string."""
    # Single exit point tracker to satisfy strict PLR0911 configuration
    result = None

    if not isinstance(email, str):
        err_type = type(email).__name__
        result = (
            False,
            f"Error: Input must be a string value (received: {err_type}).",
        )

    else:
        # Standardise email strings by stripping and converting to lowercase
        stripped = email.strip().lower()

        # Check structural markers
        invalid_structure = (
            "@" not in stripped
            or stripped.count("@") > 1
            or stripped.startswith("@")
            or stripped.endswith("@")
        )

        if not stripped:
            result = False, "Error: Email field cannot be empty."
        elif invalid_structure:
            result = False, "Error: Invalid email structure"
        else:
            result = True, stripped

    return result
