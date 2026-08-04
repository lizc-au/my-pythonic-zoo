"""
test_zoo_core.py

Unit tests for core repository modules: string_cleaner and email_validator.
"""

import unittest

from data_cleaning.string_cleaner import clean_office_data
from user_management.email_validator import validate_user_email
from user_management.password_hasher import generate_secure_hash, verify_password


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


class TestEmailValidator(unittest.TestCase):
    def test_valid_emails(self):
        """Test that structurally sound emails pass and sanitize to lowercase."""
        valid_cases = ["  lizc.au@example.com.au ", "PERTH.coder@domain.com"]
        for email in valid_cases:
            is_valid, result = validate_user_email(email)
            self.assertTrue(is_valid)
            self.assertEqual(result, email.strip().lower())

    def test_invalid_email_structures(self):
        """Test rejection of malformed structures (missing @, multiples, empty fields)."""
        invalid_cases = [
            ("bad_email_no_at.com", "Error: Invalid email structure"),
            ("double@@email.com", "Error: Invalid email structure"),
            ("user@", "Error: Invalid email structure"),
            ("", "Error: Email field cannot be empty.")
        ]
        for email, expected_error in invalid_cases:
            is_valid, result = validate_user_email(email)
            self.assertFalse(is_valid)
            self.assertTrue(result.startswith(expected_error))


class TestPasswordHasher(unittest.TestCase):
    def test_successful_password_verification(self):
        """Test that a correctly matched login password verifies successfully."""
        password = "SecurePerthVolunteer2026!"
        stored_hash, stored_salt = generate_secure_hash(password)
        
        # Verify the correct password returns True
        self.assertTrue(verify_password(stored_hash, stored_salt, password))

    def test_failed_password_verification(self):
        """Test that an incorrect password attempt is securely rejected."""
        password = "SecurePerthVolunteer2026!"
        stored_hash, stored_salt = generate_secure_hash(password)
        
        # Verify a bad password attempt returns False
        wrong_attempt = "wrong_password_123"
        self.assertFalse(verify_password(stored_hash, stored_salt, wrong_attempt))

    def test_unique_salts_generate_unique_hashes(self):
        """
        Test that identical passwords generate completely different cryptographic
        hashes due to unique salts.
        """
        password = "SamePassword123!"
        hash_one, salt_one = generate_secure_hash(password)
        hash_two, salt_two = generate_secure_hash(password)
        
        # Even though the passwords are the same, the hashes and salts must be unique
        self.assertNotEqual(salt_one, salt_two)
        self.assertNotEqual(hash_one, hash_two)


if __name__ == "__main__":
    unittest.main()
