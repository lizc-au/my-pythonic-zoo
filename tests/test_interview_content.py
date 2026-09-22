"""
test_interview_content.py

Validate answer points and teaching-exhibit relationships.
"""

import csv
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[1]
CATALOGUE_DIR = PROJECT_ROOT / "interview_preparation"

MAX_CODE_EXAMPLE_LINES = 10

QUESTION_COLUMNS = [
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
ANSWER_COLUMNS = [
    "answer_point_id",
    "question_id",
    "minimum_level",
    "display_order",
    "explanation",
    "code_example",
]
EXHIBIT_COLUMNS = [
    "exhibit_link_id",
    "question_id",
    "display_order",
    "exhibit_name",
    "exhibit_path",
    "relationship",
]

LEVEL_ORDER = {"Junior": 0, "Mid-level": 1, "Advanced": 2}


def load_rows(
    filename: str,
    expected_columns: list[str],
) -> list[dict[str, str]]:
    """Load complete CSV rows and verify their columns."""
    path = CATALOGUE_DIR / filename

    with path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        assert reader.fieldnames == expected_columns

        rows = []
        for row in reader:
            assert None not in row
            assert all(value is not None for value in row.values())
            rows.append(
                {
                    key: value
                    for key, value in row.items()
                    if key is not None and value is not None
                }
            )

    return rows


def test_answer_points_are_valid() -> None:
    """Ensure answers are ordered and linked to known questions."""
    questions = load_rows("interview_questions.csv", QUESTION_COLUMNS)
    answers = load_rows("answer_points.csv", ANSWER_COLUMNS)
    questions_by_id = {question["question_id"]: question for question in questions}

    answer_ids = [answer["answer_point_id"] for answer in answers]
    assert answers
    assert len(answer_ids) == len(set(answer_ids))

    orders_by_question: defaultdict[str, list[int]] = defaultdict(list)
    answered_question_ids: set[str] = set()

    for answer in answers:
        question_id = answer["question_id"]
        display_order = int(answer["display_order"])
        code_lines = answer["code_example"].replace("\\n", "\n").splitlines()

        assert answer["answer_point_id"]
        assert question_id in questions_by_id
        assert answer["minimum_level"] in LEVEL_ORDER
        assert (
            LEVEL_ORDER[answer["minimum_level"]]
            >= LEVEL_ORDER[questions_by_id[question_id]["minimum_level"]]
        )
        assert display_order > 0
        assert answer["explanation"]
        assert len(code_lines) <= MAX_CODE_EXAMPLE_LINES

        orders_by_question[question_id].append(display_order)
        answered_question_ids.add(question_id)

    assert answered_question_ids == set(questions_by_id)

    for display_orders in orders_by_question.values():
        assert sorted(display_orders) == list(range(1, len(display_orders) + 1))


def test_exhibit_links_are_valid() -> None:
    """Ensure exhibit links reference questions and existing files."""
    questions = load_rows("interview_questions.csv", QUESTION_COLUMNS)
    exhibits = load_rows("question_exhibits.csv", EXHIBIT_COLUMNS)
    question_ids = {question["question_id"] for question in questions}

    exhibit_link_ids = [exhibit["exhibit_link_id"] for exhibit in exhibits]
    assert exhibits
    assert len(exhibit_link_ids) == len(set(exhibit_link_ids))

    orders_by_question: defaultdict[str, list[int]] = defaultdict(list)
    linked_question_ids: set[str] = set()

    for exhibit in exhibits:
        question_id = exhibit["question_id"]
        display_order = int(exhibit["display_order"])
        exhibit_path = (PROJECT_ROOT / exhibit["exhibit_path"]).resolve()

        assert exhibit["exhibit_link_id"]
        assert question_id in question_ids
        assert display_order > 0
        assert exhibit["exhibit_name"]
        assert exhibit["relationship"]
        assert exhibit_path.is_relative_to(PROJECT_ROOT)
        assert exhibit_path.is_file()

        orders_by_question[question_id].append(display_order)
        linked_question_ids.add(question_id)

    assert linked_question_ids == question_ids

    for display_orders in orders_by_question.values():
        assert sorted(display_orders) == list(range(1, len(display_orders) + 1))
