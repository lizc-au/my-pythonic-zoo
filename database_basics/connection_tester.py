"""
connection_tester.py

SQLite Connection and Error Handling Example
--------------------------------------------

Demonstrates how to:

1. Open an SQLite database connection safely.
2. Execute a simple query to verify the connection.
3. Handle SQLite-specific connection errors.
4. Close the database connection reliably.
5. Use an in-memory database when a persistent file is not required.
"""

import sqlite3
from contextlib import closing
from pathlib import Path


def check_database_connection(db_name: str | Path) -> bool:
    """Attempt an SQLite connection and report whether it succeeds."""
    print(f"[PROCESS] Attempting connection to: '{db_name}'...")

    try:
        with closing(sqlite3.connect(db_name)) as connection:
            cursor = connection.execute("SELECT sqlite_version();")
            version = cursor.fetchone()

            print(f"[SUCCESS] Connection established. SQLite version: {version}")

    except sqlite3.Error as error:
        print(f"[DATABASE ERROR] Encountered: {error}")
        return False

    print("[INFO] Safe exit: Database connection closed.")
    return True


# --- Standalone Verification Exhibit ---
if __name__ == "__main__":
    print("=== Pythonic Database Basics Zoo Exhibit ===\n")

    print("--- Test Case 1: Standard Connection ---")
    check_database_connection(":memory:")

    print("\n" + "=" * 40 + "\n")

    print("--- Test Case 2: Simulating a Connection Failure ---")
    invalid_database = Path("missing_directory") / "broken_db.db"
    check_database_connection(invalid_database)
