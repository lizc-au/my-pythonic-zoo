"""
password_hasher.py

Secure User Authentication Module
--------------------------------

CRITICAL SECURITY PRINCIPLE: Never store plain-text passwords in a database.

Why this matters:
1. Database Breaches: If a hacker steals a copy of the user database, plain-text
   passwords give them immediate access to every account. Hashing ensures they
   only see useless strings of random characters.
2. Credential Stuffing: Most people reuse passwords across multiple websites.
   If your database leaks plain-text passwords, hackers will use them to break
   into your users' bank accounts, personal emails, and social media.
3. Internal Security (The Insider Threat): System administrators, developers, or
   rogue employees with database access should never have the power to see a
   user's actual password.

How this script handles it safely:
- PBKDF2 (Password-Based Key Derivation Function 2) slashes computational speed
  for attackers, making 'brute-force' hacking attempts too slow and expensive.
- Cryptographic 'Salts' ensure that even if two users choose the exact same
  password, their final hashes stored in the database look completely different.
"""

import hashlib
import os


def generate_secure_hash(password: str) -> tuple:
    """
    Creates a secure SHA-256 hash using a unique random salt
    to protect against rainbow table attacks.
    """
    # Generate a random 16-byte salt
    salt = os.urandom(16)

    # Combine salt and password, then hash them together
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000  # Number of iterations
    )
    return hashed_password, salt


def verify_password(stored_hash: bytes, stored_salt: bytes, login_attempt: str) -> bool:
    """
    Verifies an incoming login password attempt against the stored hash and salt.
    """
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        login_attempt.encode('utf-8'),
        stored_salt,
        100000
    )
    return new_hash == stored_hash


# --- Standalone Verification Exhibit ---
if __name__ == "__main__":
    print("--- Pythonic User Authentication Zoo Exhibit ---")

    # Simulate a user signing up for a Perth volunteer portal
    user_password = "SecurePerthVolunteer2026!"
    print(f"1. User registers password: '{user_password}'")

    # Securely hash the password for database storage
    db_hash, db_salt = generate_secure_hash(user_password)
    print(f"2. Database stores unique salt: {db_salt.hex()[:10]}...")
    print(f"3. Database stores hashed string: {db_hash.hex()[:10]}...")

    print("\n--- Testing Login Attempts ---")
    # Test 1: Wrong password attempt
    wrong_attempt = "wrong_password_123"
    is_valid_1 = verify_password(db_hash, db_salt, wrong_attempt)
    print(f"Attempt '{wrong_attempt}' -> Access Granted: {is_valid_1}")

    # Test 2: Correct password attempt
    correct_attempt = "SecurePerthVolunteer2026!"
    is_valid_2 = verify_password(db_hash, db_salt, correct_attempt)
    print(f"Attempt '{correct_attempt}' -> Access Granted: {is_valid_2}")
