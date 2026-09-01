"""
connection_tester.py

Robust Database Connection and Error Handling Module
----------------------------------------------------

CRITICAL ENGINEERING PRINCIPLE: Never assume a database connection will succeed.
Always wrap database interactions in try-except-finally blocks to prevent memory
leaks, unclosed connections, and catastrophic application crashes.

Why this matters:
1. Graceful Failures: If a network drops or a database server goes offline, your
   app should log the error cleanly and alert the system, not crash for the user.
2. Resource Management: Open database connections consume server memory. If code
   crashes midway without a 'finally' block, that connection stays open, slowly
   bleeding server resources until the system collapses.
"""

import sqlite3
from sqlite3 import Error


def test_database_connection(db_name: str):
    """
    Attempts to connect to a database, execute a simple query,
    and handles connection errors gracefully.
    """
    connection = None

    try:
        print(f"[PROCESS] Attempting connection to: '{db_name}'...")
        connection = sqlite3.connect(db_name)

        cursor = connection.cursor()
        cursor.execute("SELECT SQLite_Version();")
        version = cursor.fetchone()

        print(f"[SUCCESS] Connection Established. SQLite Version: {version}")

    except Error as error_message:
        print(f"[DATABASE ERROR] Encontered: {error_message}")
        print("[ALERT] Triggering automatic alert system... (Simulated)")

    except OSError as system_error:
        print(f"[OS ERROR] Filesystem failure: {system_error}")
        print("[ALERT] Verify path string formatting or disk write permissions.")

    finally:
        if connection:
            connection.close()
            print("[INFO] Safe Exit: Database connection closed securely.")


# --- Standalone Verification Exhibit ---
if __name__ == "__main__":
    print("=== Pythonic Database Basics Zoo Exhibit ===\n")

    print("--- Test Case 1: Standard Connection ---")
    test_database_connection("perth_volunteer_mock.db")

    print("\n" + "=" * 40 + "\n")

    print("--- Test Case 2: Simulating a Connection Failure ---")
    test_database_connection("C:/InvalidFolder/NonExistentDisk/broken_db.db")
