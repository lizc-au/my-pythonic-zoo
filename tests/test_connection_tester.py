"""
test_connection_tester.py

Tests for the SQLite connection example.
"""

from pathlib import Path

from database_basics.connection_tester import check_database_connection


def test_successful_connection_returns_true(capsys) -> None:
    """A valid in-memory SQLite connection should succeed."""
    result = check_database_connection(":memory:")

    captured = capsys.readouterr()

    assert result is True
    assert "[SUCCESS] Connection established." in captured.out
    assert "[INFO] Safe exit: Database connection closed." in captured.out


def test_invalid_path_returns_false(tmp_path: Path, capsys) -> None:
    """A database path inside a missing directory should fail cleanly."""
    blocking_file = tmp_path / "not_a_directory"
    blocking_file.touch()
    invalid_database = blocking_file / "broken.db"

    result = check_database_connection(invalid_database)

    captured = capsys.readouterr()

    assert result is False
    assert "[DATABASE ERROR] Encountered:" in captured.out
