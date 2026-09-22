"""
test_interview_model.py

Test loading and connecting the interview catalogue data.
"""

from interview_preparation.interview_model import load_catalogue


def test_load_catalogue_connects_related_data() -> None:
    """Load questions with their ordered answers and exhibits."""
    catalogue = load_catalogue()

    assert catalogue.questions
    assert set(catalogue.answers_by_question) == set(catalogue.questions)
    assert set(catalogue.exhibits_by_question) == set(catalogue.questions)

    first_question = catalogue.questions["IQ001"]
    assert first_question.topic == "Names and objects"
    assert first_question.minimum_level == "Junior"
    assert first_question.follow_up_question_id == "IQ002"
    assert first_question.active is True

    answer_ids = [
        answer.answer_point_id for answer in catalogue.answers_by_question["IQ001"]
    ]
    assert answer_ids == ["AP001", "AP002", "AP003"]

    exhibit_names = [
        exhibit.exhibit_name for exhibit in catalogue.exhibits_by_question["IQ005"]
    ]
    assert exhibit_names == [
        "Functions as Objects",
        "Button and Event Handling",
    ]


def test_load_catalogue_decodes_code_line_breaks() -> None:
    """Convert stored newline markers into displayable code."""
    catalogue = load_catalogue()
    answers = catalogue.answers_by_question["IQ008"]
    stop_iteration_answer = next(
        answer for answer in answers if answer.answer_point_id == "AP024"
    )

    assert "\\n" not in stop_iteration_answer.code_example
    assert stop_iteration_answer.code_example.splitlines() == [
        "try:",
        "    animal = next(iterator)",
        "except StopIteration:",
        "    pass",
    ]
