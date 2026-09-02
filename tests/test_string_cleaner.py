"""
test_string_cleaner.py

Tests for the string cleaning example.
"""

import unittest

from data_cleaning.string_cleaner import clean_office_data


class TestStringCleaner(unittest.TestCase):
    def test_whitespace_and_capitalization(self):
        """Test that messy text is stripped of spaces and properly capitalized."""
        raw_inputs = ["  subiaco ", "fremantle   ", "  SCARBOROUGH"]
        expected = ["Subiaco", "Fremantle", "Scarborough"]

        self.assertEqual(clean_office_data(raw_inputs), expected)

    def test_empty_strings_filtered(self):
        """Test that empty string elements are silently removed from the list."""
        raw_inputs = ["joondalup", "", " ", "alkimos"]
        expected = ["Joondalup", "Alkimos"]

        self.assertEqual(clean_office_data(raw_inputs), expected)


if __name__ == "__main__":
    unittest.main()
