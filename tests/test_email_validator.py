"""
test_email_validator.py

Tests for the email validation example.
"""

import unittest

from user_management.email_validator import validate_user_email


class TestEmailValidator(unittest.TestCase):
    def test_valid_emails(self):
        """Test that structurally sound emails pass and sanitize to lowercase."""
        valid_cases = ["  lizc.au@example.com.au ", "PERTH.coder@domain.com"]

        for email in valid_cases:
            is_valid, result = validate_user_email(email)

            self.assertTrue(is_valid)
            self.assertEqual(result, email.strip().lower())

    def test_invalid_email_structures(self):
        """Test rejection of malformed email structures."""
        invalid_cases = [
            ("bad_email_no_at.com", "Error: Invalid email structure"),
            ("double@@email.com", "Error: Invalid email structure"),
            ("user@", "Error: Invalid email structure"),
            ("", "Error: Email field cannot be empty."),
        ]

        for email, expected_error in invalid_cases:
            is_valid, result = validate_user_email(email)

            self.assertFalse(is_valid)
            self.assertTrue(result.startswith(expected_error))


if __name__ == "__main__":
    unittest.main()
