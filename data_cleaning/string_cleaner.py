"""
string_cleaner.py

A self-contained utility script to clean and standardise messy text data strings.
Optimised for processing raw spreadsheet exports or user inputs.
"""

def clean_office_data(messy_list: list) -> list:
    """
    Removes accidental white spaces and applies proper title capitalization 
    using a Pythonic list comprehension.
    """
    # Pythonic list comprehension: fast, clean, and idiomatic
    return [item.strip().title() for item in messy_list if item]


# --- Self-Contained Execution Block ---
# This allows the script to run standalone when executed directly.
if __name__ == "__main__":
    # Mock data representing typical messy entry formatting from a Perth office
    raw_perth_suburbs = ["  subiaco ", "fremantle   ", "  SCARBOROUGH", "", "joondalup"]
    
    cleaned_output = clean_office_data(raw_perth_suburbs)
    
    print("--- Pythonic Data Cleaner ---")
    print(f"Original Raw Input: {raw_perth_suburbs}")
    print(f"Cleaned Safe Output: {cleaned_output}")
