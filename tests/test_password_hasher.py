"""
test_password_hasher.py

Tests for the password hashing example.
"""

import unittest

from user_management.password_hasher import generate_secure_hash, verify_password


class TestPasswordHasher(unittest.TestCase):
    def test_successful_password_verification(self):
        """Test that a correctly matched login password verifies successfully."""
        password = "SecurePerthVolunteer2026!"
        stored_hash, stored_salt = generate_secure_hash(password)

        self.assertTrue(verify_password(stored_hash, stored_salt, password))

    def test_failed_password_verification(self):
        """Test that an incorrect password attempt is securely rejected."""
        password = "SecurePerthVolunteer2026!"
        stored_hash, stored_salt = generate_secure_hash(password)
        wrong_attempt = "wrong_password_123"

        self.assertFalse(verify_password(stored_hash, stored_salt, wrong_attempt))

    def test_unique_salts_generate_unique_hashes(self):
        """Test that identical passwords produce different salts and hashes."""
        password = "SamePassword123!"
        hash_one, salt_one = generate_secure_hash(password)
        hash_two, salt_two = generate_secure_hash(password)

        self.assertNotEqual(salt_one, salt_two)
        self.assertNotEqual(hash_one, hash_two)


if __name__ == "__main__":
    unittest.main()
