"""
phone_sanitiser.py

ENGINEERING PRINCIPLE: Raw string inputs from web forms or spreadsheet

exports can contain inconsistent delimiters, spaces, country codes, or
accidental characters. Sanitising phone inputs at the entry gate ensures
consistent formatting for database storage and downstream tools.

Note: AU cases only included as requested for this snippet.
"""

# Named constants to eliminate magic value errors (PLR2004)
AU_MOBILE_LEN = 10
AU_LANDLINE_LEN = 10
AU_TOLLFREE_LEN = 10
AU_SHORT_LEN = 6


def _format_mobile(digits: str, is_intl: bool) -> str:
    """Format mobile numbers starting with 04."""
    if is_intl:
        return f"+61 4{digits[2:4]} {digits[4:7]} {digits[7:]}"
    return f"04{digits[2:4]} {digits[4:7]} {digits[7:]}"


def _format_landline(digits: str, is_intl: bool) -> str:
    """Format landline numbers based on standard state area codes."""
    area_code = digits[:2]
    if is_intl:
        # Drop the leading zero for international landline formatting
        return f"+61 {area_code[1]} {digits[2:6]} {digits[6:]}"
    return f"({area_code}) {digits[2:6]} {digits[6:]}"


def sanitize_australian_phone_number(
    phone: str, format_type: str = "national"
) -> tuple[bool, str]:
    """Validates and structuralises Australian phone string values."""
    if not isinstance(phone, str):
        err_type = type(phone).__name__
        return (
            False,
            f"Error: Input must be a string value (received: {err_type}).",
        )

    # Reject if any alphanumeric letters or illegal symbols are explicitly present
    # Allowed symbols: spaces, dashes, dots, brackets, plus sign
    allowed_chars = set("0123456789 -().+")
    if not set(phone).issubset(allowed_chars):
        return False, "Error: Phone number contains invalid characters."

    is_intl = format_type == "international"
    normalized = "".join(filter(str.isalnum, phone))

    # Normalise country prefixes safely
    if normalized.startswith("61") and len(normalized) in (11, 12):
        normalized = "0" + normalized[2:]

    digits = "".join(filter(str.isdigit, normalized))
    result = None

    if len(digits) == AU_MOBILE_LEN and digits.startswith("04"):
        result = True, _format_mobile(digits, is_intl)

    elif len(digits) == AU_LANDLINE_LEN and digits[:2] in (
        "02",
        "03",
        "07",
        "08",
    ):
        result = True, _format_landline(digits, is_intl)

    elif len(digits) == AU_TOLLFREE_LEN and digits.startswith(("1300", "1800")):
        result = True, f"{digits[:4]} {digits[4:7]} {digits[7:]}"

    elif len(digits) == AU_SHORT_LEN and digits.startswith("13"):
        result = True, f"{digits[:2]} {digits[2:4]} {digits[4:]}"

    else:
        err_msg = (
            f"Error: Invalid Australian phone number structure "
            f"(digit length: {len(digits)})."
        )
        result = False, err_msg

    return result
