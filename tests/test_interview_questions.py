"""
test_interview_questions.py

Validate the structure and relationships in the interview catalogue.
"""

import csv
from pathlib import Path

CATALOGUE_PATH = (
    Path(__file__).parents[1] / "interview_preparation" / "interview_questions.csv"
)
EXPECTED_COLUMNS = [
    "question_id",
    "topic",
    "minimum_level",
    "question",
    "tests_knowledge_of",
    "follow_up_question_id",
    "tags",
    "reference_url",
    "active",
]
VALID_LEVELS = {"Junior", "Mid-level", "Advanced"}
VALID_ACTIVE_VALUES = {"TRUE", "FALSE"}


def load_questions() -> list[dict[str, str]]:
    """Load complete catalogue rows and verify the expected columns."""
    with CATALOGUE_PATH.open(encoding="utf-8", newline="") as catalogue_file:
        reader = csv.DictReader(catalogue_file)
        assert reader.fieldnames == EXPECTED_COLUMNS

        questions = []
        for row in reader:
            assert None not in row
            assert all(value is not None for value in row.values())
            questions.append(
                {
                    key: value
                    for key, value in row.items()
                    if key is not None and value is not None
                }
            )

    return questions


def test_catalogue_rows_are_valid() -> None:
    """Ensure IDs, levels, references, and follow-up links are valid."""
    questions = load_questions()
    assert questions

    question_ids = [question["question_id"] for question in questions]
    assert len(question_ids) == len(set(question_ids))

    known_ids = set(question_ids)
    for question in questions:
        assert question["question_id"]
        assert question["topic"]
        assert question["question"]
        assert question["tests_knowledge_of"]
        assert question["minimum_level"] in VALID_LEVELS
        assert question["active"] in VALID_ACTIVE_VALUES
        assert question["reference_url"].startswith("https://")

        follow_up_id = question["follow_up_question_id"]
        assert not follow_up_id or follow_up_id in known_ids


def test_follow_up_sequences_do_not_loop() -> None:
    """Ensure every follow-up sequence eventually terminates."""
    questions = load_questions()
    questions_by_id = {question["question_id"]: question for question in questions}

    for starting_id in questions_by_id:
        visited_ids: set[str] = set()
        current_id = starting_id

        while current_id:
            assert current_id not in visited_ids
            visited_ids.add(current_id)
            current_id = questions_by_id[current_id]["follow_up_question_id"]
