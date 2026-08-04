"""
phone_sanitiser.py

Australian Phone Number Sanitisation Module
-------------------------------------------

ENGINEERING PRINCIPLE: Raw string inputs from web forms or spreadsheet exports can contain
inconsistent delimiters, spaces, country codes, or accidental characters. Sanitising and
standardising phone inputs at the entry gate ensures consistent formatting for database storage
and downstream communication services.
"""


def sanitize_australian_phone_number(
    phone: str, format_type: str = "national"
) -> tuple[bool, str]:
    """
    Sanitises and formats Australian phone strings into standardised structural blocks.

    Supports Australian mobile (04xx), landlines (02, 03, 07, 08 area codes),
    and 13/1300/1800 numbers. Handles country codes (+61), trailing/leading spaces,
    and delimiters like hyphens or parentheses.

    Parameters:
        phone (str): Raw user-submitted phone number string.
        format_type (str): Output format preference ('national' or 'international').

    Returns:
        tuple[bool, str]: (is_valid, formatted_number_or_error_message)
    """
    if not phone or not isinstance(phone, str):
        return False, "Error: Phone number field cannot be empty."

    raw = phone.strip()
    if not raw:
        return False, "Error: Phone number field cannot be empty."

    # Reject accidental alphabetic or unallowed special characters upfront
    allowed_chars = set("0123456789 +-().")
    for char in raw:
        if char not in allowed_chars:
            return False, f"Error: Phone number contains invalid character: '{char}'"

    # Normalize international country code prefix (+61 or 61) to national '0' prefix
    normalized = raw
    if normalized.startswith("+61"):
        normalized = "0" + normalized[3:]
    elif normalized.startswith("61") and len("".join(filter(str.isdigit, normalized))) in (11, 12):
        normalized = "0" + normalized[2:]

    # Extract numeric digits only
    digits = "".join(filter(str.isdigit, normalized))

    if not digits:
        return False, "Error: No numeric digits found in input."

    is_international = format_type.lower() == "international"

    # Mobile numbers: 10 digits starting with 04
    if len(digits) == 10 and digits.startswith("04"):
        if is_international:
            formatted = f"+61 4{digits[2:4]} {digits[4:7]} {digits[7:]}"
        else:
            formatted = f"{digits[:4]} {digits[4:7]} {digits[7:]}"
        return True, formatted

    # Landline numbers: 10 digits starting with 02 (NSW/ACT), 03 (VIC/TAS), 07 (QLD), 08 (WA/SA/NT)
    if len(digits) == 10 and digits[:2] in ("02", "03", "07", "08"):
        area_code = digits[:2]
        if is_international:
            formatted = f"+61 {area_code[1]} {digits[2:6]} {digits[6:]}"
        else:
            formatted = f"({area_code}) {digits[2:6]} {digits[6:]}"
        return True, formatted

    # Local rate / Toll-free numbers: 10 digits starting with 1300 or 1800
    if len(digits) == 10 and (digits.startswith("1300") or digits.startswith("1800")):
        formatted = f"{digits[:4]} {digits[4:7]} {digits[7:]}"
        return True, formatted

    # Short local rate numbers: 6 digits starting with 13
    if len(digits) == 6 and digits.startswith("13"):
        formatted = f"{digits[:2]} {digits[2:4]} {digits[4:]}"
        return True, formatted

    return False, f"Error: Invalid Australian phone number structure (digit length: {len(digits)})."


# --- Standalone Verification Exhibit ---
if __name__ == "__main__":
    print("=== Pythonic Data Cleaning Zoo Exhibit ===")
    print("--- Testing Australian Phone Number Sanitiser ---\n")

    # Sample mock data representing typical entries from Perth / WA community forms
    mock_phone_inputs = [
        "  0412 345 678 ",       # Perth mobile (valid, whitespace)
        "(08) 9380 1234",        # Perth WA landline with area code
        "+61 8 9380 1234",       # Perth landline in international format
        "0893801234",            # Perth landline unformatted
        "  +61 412 345 678 ",    # Mobile international format with whitespace
        "1300 224 636",          # 1300 local rate number
        "13 11 14",              # 13 short service number
        "0412ABC678",            # Invalid: accidental letters
        "12345",                 # Invalid: too short
        "",                      # Invalid: empty string
    ]

    for raw_input in mock_phone_inputs:
        is_valid, result = sanitize_australian_phone_number(raw_input)
        print(f"Raw Input: '{raw_input}'")
        if is_valid:
            print(f"-> [PASS] Sanitised Output: '{result}'\n")
        else:
            print(f"-> [FAIL] Reject Reason:   '{result}'\n")
