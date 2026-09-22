"""
interview_model.py

Load and represent the interview-preparation catalogue.
"""

import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
LEVEL_ORDER = {"Junior": 0, "Mid-level": 1, "Advanced": 2}


@dataclass(frozen=True)
class Question:
    """One interview question from the catalogue."""

    question_id: str
    topic: str
    minimum_level: str
    question: str
    tests_knowledge_of: str
    follow_up_question_id: str
    tags: str
    reference_url: str
    active: bool


@dataclass(frozen=True)
class AnswerPoint:
    """One expected point, with an optional compact code example."""

    answer_point_id: str
    question_id: str
    minimum_level: str
    display_order: int
    explanation: str
    code_example: str


@dataclass(frozen=True)
class ExhibitLink:
    """A link from an interview question to a teaching exhibit."""

    exhibit_link_id: str
    question_id: str
    display_order: int
    exhibit_name: str
    exhibit_path: str
    relationship: str


@dataclass(frozen=True)
class Catalogue:
    """All related interview-preparation data."""

    questions: dict[str, Question]
    answers_by_question: dict[str, list[AnswerPoint]]
    exhibits_by_question: dict[str, list[ExhibitLink]]


def load_rows(path: Path) -> list[dict[str, str]]:
    """Load CSV rows while preserving blank fields as empty strings."""
    with path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [
            {key: value or "" for key, value in row.items() if key is not None}
            for row in reader
        ]


def load_questions(base_dir: Path) -> dict[str, Question]:
    """Load interview questions indexed by their stable IDs."""
    return {
        row["question_id"]: Question(
            question_id=row["question_id"],
            topic=row["topic"],
            minimum_level=row["minimum_level"],
            question=row["question"],
            tests_knowledge_of=row["tests_knowledge_of"],
            follow_up_question_id=row["follow_up_question_id"],
            tags=row["tags"],
            reference_url=row["reference_url"],
            active=row["active"] == "TRUE",
        )
        for row in load_rows(base_dir / "interview_questions.csv")
    }


def load_answers(base_dir: Path) -> dict[str, list[AnswerPoint]]:
    """Load ordered answer points grouped by question ID."""
    grouped_answers: defaultdict[str, list[AnswerPoint]] = defaultdict(list)

    for row in load_rows(base_dir / "answer_points.csv"):
        answer = AnswerPoint(
            answer_point_id=row["answer_point_id"],
            question_id=row["question_id"],
            minimum_level=row["minimum_level"],
            display_order=int(row["display_order"]),
            explanation=row["explanation"],
            code_example=row["code_example"].replace("\\n", "\n"),
        )
        grouped_answers[answer.question_id].append(answer)

    for answers in grouped_answers.values():
        answers.sort(key=lambda answer: answer.display_order)

    return dict(grouped_answers)


def load_exhibits(base_dir: Path) -> dict[str, list[ExhibitLink]]:
    """Load ordered exhibit links grouped by question ID."""
    grouped_exhibits: defaultdict[str, list[ExhibitLink]] = defaultdict(list)

    for row in load_rows(base_dir / "question_exhibits.csv"):
        exhibit = ExhibitLink(
            exhibit_link_id=row["exhibit_link_id"],
            question_id=row["question_id"],
            display_order=int(row["display_order"]),
            exhibit_name=row["exhibit_name"],
            exhibit_path=row["exhibit_path"],
            relationship=row["relationship"],
        )
        grouped_exhibits[exhibit.question_id].append(exhibit)

    for exhibits in grouped_exhibits.values():
        exhibits.sort(key=lambda exhibit: exhibit.display_order)

    return dict(grouped_exhibits)


def load_catalogue(base_dir: Path = BASE_DIR) -> Catalogue:
    """Load and connect all interview-preparation data."""
    return Catalogue(
        questions=load_questions(base_dir),
        answers_by_question=load_answers(base_dir),
        exhibits_by_question=load_exhibits(base_dir),
    )
