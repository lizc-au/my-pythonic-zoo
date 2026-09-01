"""
test_phone_sanitiser.py

Unit tests for the Australian Phone Number Sanitiser module.
"""

import unittest

from data_cleaning.phone_sanitiser import sanitize_australian_phone_number


class TestPhoneSanitiser(unittest.TestCase):
    """Test suite targeting the Australian phone string normalization code."""

    def test_perth_landline_national_format(self):
        """Test Perth/WA landline numbers (08 area code) in national format."""
        raw_inputs = [
            "0893801234",
            " (08) 9380 1234 ",
            "08-9380-1234",
            "(08).9380.1234",
        ]
        for item in raw_inputs:
            is_valid, result = sanitize_australian_phone_number(
                item, format_type="national"
            )
            self.assertTrue(is_valid, f"Failed for valid Perth landline: {item}")
            self.assertEqual(result, "(08) 9380 1234")

    def test_perth_landline_international_format(self):
        """Test Perth/WA landline numbers converted to international format."""
        is_valid, result = sanitize_australian_phone_number(
            "+61 8 9380 1234", format_type="international"
        )
        self.assertTrue(is_valid)
        self.assertEqual(result, "+61 8 9380 1234")

        is_valid_nat, result_nat = sanitize_australian_phone_number(
            "+61 8 9380 1234", format_type="national"
        )
        self.assertTrue(is_valid_nat)
        self.assertEqual(result_nat, "(08) 9380 1234")

    def test_mobile_numbers(self):
        """Test Australian mobile numbers (04xx)."""
        is_valid, result = sanitize_australian_phone_number(" 0412 345 678 ")
        self.assertTrue(is_valid)
        self.assertEqual(result, "0412 345 678")

        is_valid_intl, result_intl = sanitize_australian_phone_number(
            "0412345678", format_type="international"
        )
        self.assertTrue(is_valid_intl)
        self.assertEqual(result_intl, "+61 412 345 678")

    def test_other_state_landlines(self):
        """Test landlines for NSW (02), VIC (03), QLD (07)."""
        for prefix, expected_code in [
            ("02", "(02)"),
            ("03", "(03)"),
            ("07", "(07)"),
        ]:
            raw = f"{prefix} 9123 4567"
            is_valid, result = sanitize_australian_phone_number(raw)
            self.assertTrue(is_valid)
            self.assertEqual(result, f"{expected_code} 9123 4567")

    def test_toll_free_and_special_numbers(self):
        """Test 1300, 1800, and 13 numbers."""
        is_valid_1300, res_1300 = sanitize_australian_phone_number("1300 224 636")
        self.assertTrue(is_valid_1300)
        self.assertEqual(res_1300, "1300 224 636")

        is_valid_1800, res_1800 = sanitize_australian_phone_number("1800123456")
        self.assertTrue(is_valid_1800)
        self.assertEqual(res_1800, "1800 123 456")

        is_valid_13, res_13 = sanitize_australian_phone_number("13 11 14")
        self.assertTrue(is_valid_13)
        self.assertEqual(res_13, "13 11 14")

    def test_invalid_characters(self):
        """Test rejection of alphabetic and illegal special characters."""
        invalid_inputs = [
            "0412ABC678",
            "08-9380-123x",
            "0412#345678",
            "PHONE: 0412345678",
        ]
        for item in invalid_inputs:
            is_valid, result = sanitize_australian_phone_number(item)
            self.assertFalse(is_valid)
            self.assertIn("Error:", result)

    def test_empty_or_invalid_type(self):
        """Test handling of empty, whitespace-only, or non-string inputs."""
        invalid_inputs = ["", " ", None, 12345678]
        for item in invalid_inputs:
            is_valid, result = sanitize_australian_phone_number(item)
            self.assertFalse(is_valid)
            self.assertIn("Error:", result)


if __name__ == "__main__":
    unittest.main()
