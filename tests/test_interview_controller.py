"""
test_interview_controller.py

Test interview navigation without opening a Tkinter window.

Cast a replaced callable because mypy retains its production type and
cannot otherwise recognise MagicMock assertion methods.
"""

from typing import cast
from unittest.mock import MagicMock, patch

import pytest

from interview_preparation.interview_controller import (
    InterviewController,
)
from interview_preparation.interview_model import Catalogue, Question


def mock_method(method: object) -> MagicMock:
    """Treat a replaced callable as a MagicMock for assertions."""
    return cast(MagicMock, method)


def make_question(
    question_id: str,
    topic: str,
    *,
    minimum_level: str = "Junior",
    follow_up_question_id: str = "",
) -> Question:
    """Create a compact question fixture."""
    return Question(
        question_id=question_id,
        topic=topic,
        minimum_level=minimum_level,
        question=f"Question {question_id}",
        tests_knowledge_of="Test knowledge",
        follow_up_question_id=follow_up_question_id,
        tags="test",
        reference_url="https://docs.python.org/",
        active=True,
    )


def make_controller(
    *,
    current_level: str = "Junior",
    requested_level: str = "Junior",
) -> InterviewController:
    """Create a controller with mocked view dependencies."""
    questions = {
        "IQ001": make_question(
            "IQ001",
            "First topic",
            follow_up_question_id="IQ002",
        ),
        "IQ002": make_question("IQ002", "First topic"),
        "IQ003": make_question("IQ003", "First topic"),
        "IQ004": make_question("IQ004", "Second topic"),
        "IQ005": make_question(
            "IQ005",
            "Second topic",
            minimum_level="Advanced",
        ),
    }

    controller = InterviewController.__new__(InterviewController)
    controller.root = MagicMock()
    controller.catalogue = Catalogue(
        questions=questions,
        answers_by_question={},
        exhibits_by_question={},
    )
    controller.view = MagicMock()
    controller.view.filters.selected_level = current_level
    controller.current_question_id = None
    controller.requested_level = requested_level
    return controller


@pytest.mark.parametrize(
    (
        "question_id",
        "next_question_id",
        "current_level",
        "requested_level",
        "expected_label",
    ),
    [
        (
            "IQ001",
            None,
            "Junior",
            "Junior",
            "Next follow-up",
        ),
        (
            "IQ002",
            "IQ003",
            "Junior",
            "Junior",
            "Next question",
        ),
        (
            "IQ003",
            "IQ004",
            "Junior",
            "Junior",
            "Next topic",
        ),
        (
            "IQ004",
            None,
            "Junior",
            "Junior",
            "Restart Junior questions",
        ),
        (
            "IQ004",
            None,
            "Advanced",
            "Mid-level",
            "Return to Mid-level questions",
        ),
    ],
)
def test_select_question_sets_correct_navigation_label(
    question_id: str,
    next_question_id: str | None,
    current_level: str,
    requested_level: str,
    expected_label: str,
) -> None:
    """Choose a label that describes the next available action."""
    controller = make_controller(
        current_level=current_level,
        requested_level=requested_level,
    )

    mock_method(
        controller.view.questions.question_after
    ).return_value = next_question_id
    controller.select_question(question_id)

    question = controller.catalogue.questions[question_id]
    mock_method(controller.view.details).show_question.assert_called_once_with(
        question,
        [],
        expected_label,
    )


def test_follow_up_temporarily_raises_interview_level() -> None:
    """Display a harder follow-up without changing the requested level."""
    controller = make_controller(
        current_level="Mid-level",
        requested_level="Mid-level",
    )
    controller.current_question_id = "IQ001"
    controller.catalogue.questions["IQ002"] = make_question(
        "IQ002",
        "First topic",
        minimum_level="Advanced",
    )

    with patch.object(controller, "refresh_questions") as refresh:
        controller.open_follow_up()

    mock_method(controller.view.filters.select_level).assert_called_once_with(
        "Advanced"
    )
    refresh.assert_called_once_with()
    mock_method(controller.view.questions.select_question).assert_called_once_with(
        "IQ002"
    )
    assert controller.requested_level == "Mid-level"


def test_end_of_selection_returns_to_requested_level() -> None:
    """Restart the original level after its final visible question."""
    controller = make_controller(
        current_level="Advanced",
        requested_level="Mid-level",
    )
    controller.current_question_id = "IQ004"
    mock_method(controller.view.questions.question_after).return_value = None

    with patch.object(controller, "refresh_questions") as refresh:
        controller.open_follow_up()

    mock_method(controller.view.filters.select_level).assert_called_once_with(
        "Mid-level"
    )
    refresh.assert_called_once_with()
