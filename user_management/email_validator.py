"""
email_validator.py

User Input Validation Module
----------------------------

ENGINEERING PRINCIPLE: Always validate data at the gate. Never pass raw user inputs 
directly to systems or databases without confirming structural integrity first.

Why this matters:
1. System Reliability: Improperly formatted strings can break database queries 
   or cause downstream errors in email delivery APIs.
2. Defensive Programming: Checking bounds and structure locally prevents unexpected 
   application crashes without relying on external server error triggers.
"""

def validate_user_email(email: str) -> tuple[bool, str]:
    """
    Validates the structure of a user-submitted email string without 
    complex regular expressions, using basic Pythonic string boundaries.
    Returns a tuple: (is_valid, sanitized_email_or_error_message).
    """
    if not email:
        return False, "Error: Email field cannot be empty."

    # Standardize data by stripping spaces and converting to lowercase
    sanitized = email.strip().lower()

    # Rule 1: Must contain exactly one '@' symbol
    if sanitized.count('@') != 1:
        return False, "Error: Invalid email structure (must contain exactly one '@')."

    # Split into local part and domain part
    local_part, domain_part = sanitized.split('@')

    # Rule 2: Local and domain parts must not be empty
    if not local_part or not domain_part:
        return False, "Error: Invalid email structure (missing user or domain name)."

    # Rule 3: Domain part must contain at least one dot, and not at the very end
    if '.' not in domain_part or domain_part.endswith('.'):
        return False, "Error: Invalid domain naming structure."

    return True, sanitized


# --- Standalone Verification Exhibit ---
if __name__ == "__main__":
    print("=== Pythonic User Management Zoo Exhibit ===")
    print("--- Testing Email Gate Validation System ---\n")

    # List of test credentials simulating inputs on a Perth community registration form
    test_cases = [
        "  lizc.au@example.com.au ",  # Valid, needs trimming and lowering
        "perth.coder@domain.com",       # Valid standard format
        "bad_email_no_at.com",          # Invalid (no @)
        "double@@email.com",            # Invalid (multiple @)
        "user@",                        # Invalid (missing domain)
        "",                             # Invalid (empty)
    ]

    for test_email in test_cases:
        is_valid, result = validate_user_email(test_email)
        print(f"Raw Input: '{test_email}'")
        if is_valid:
            print(f"-> [PASS] Sanitized Data: '{result}'\n")
        else:
            print(f"-> [FAIL] Reject Reason:  '{result}'\n")
