"""
interview_controller.py

Coordinate the interview catalogue and its Tkinter interface.
"""

import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import messagebox

from interview_preparation.interview_model import (
    LEVEL_ORDER,
    PROJECT_ROOT,
    Catalogue,
    ExhibitLink,
    Question,
    load_catalogue,
)
from interview_preparation.interview_view import InterviewView, ViewCallbacks


class InterviewController:
    """Coordinate user actions, catalogue data, and view updates."""

    def __init__(self, root: tk.Tk, catalogue: Catalogue) -> None:
        self.root = root
        self.catalogue = catalogue
        self.current_question_id: str | None = None
        self.requested_level = "Junior"

        topics = sorted(
            {
                question.topic
                for question in catalogue.questions.values()
                if question.active
            }
        )
        callbacks = ViewCallbacks(
            filter_changed=self.filters_changed,
            question_selected=self.select_question,
            reveal_answer=self.reveal_answer,
            open_reference=self.open_reference,
            open_follow_up=self.open_follow_up,
            open_exhibit=self.open_exhibit,
        )
        self.view = InterviewView(root, topics, callbacks)
        self.refresh_questions()

    def filters_changed(self) -> None:
        """Remember the user's chosen level before applying filters."""
        self.requested_level = self.view.filters.selected_level
        self.refresh_questions()

    def refresh_questions(self) -> None:
        """Display active questions allowed by the current filters."""
        selected_topic = self.view.filters.selected_topic
        selected_level = LEVEL_ORDER[self.view.filters.selected_level]

        questions = sorted(
            (
                question
                for question in self.catalogue.questions.values()
                if question.active
                and LEVEL_ORDER[question.minimum_level] <= selected_level
                and selected_topic in ("All topics", question.topic)
                and self._matches_search(question)
            ),
            key=lambda question: (
                question.topic,
                question.question_id,
            ),
        )

        if questions:
            self.view.questions.show_questions(questions)
        else:
            self.current_question_id = None
            self.view.details.show_empty()
            self.view.set_status("No questions match these filters.")

    def _matches_search(self, question: Question) -> bool:
        """Match search text against learner-facing question fields."""
        search_text = self.view.filters.search_text
        searchable_fields = (
            question.question,
            question.topic,
            question.tags,
            question.tests_knowledge_of,
        )

        return not search_text or any(
            search_text in field.casefold() for field in searchable_fields
        )

    def select_question(self, question_id: str) -> None:
        """Display one question while keeping its answer hidden."""
        question = self.catalogue.questions[question_id]
        exhibits = self.catalogue.exhibits_by_question.get(question_id, [])

        self.current_question_id = question_id
        self.view.details.show_question(
            question,
            exhibits,
            self._next_action_text(question),
        )
        self.view.set_status(f"{question.question_id} - {question.topic}")

    def reveal_answer(self) -> None:
        """Show answer points appropriate to the selected level."""
        if self.current_question_id is None:
            return

        selected_level = LEVEL_ORDER[self.view.filters.selected_level]
        answers = [
            answer
            for answer in self.catalogue.answers_by_question.get(
                self.current_question_id, []
            )
            if LEVEL_ORDER[answer.minimum_level] <= selected_level
        ]

        self.view.details.answer_panel.show_answers(answers)
        self.view.set_status("Answer revealed.")

    def open_reference(self) -> None:
        """Open the current question's official Python reference."""
        question = self._current_question()
        if question is not None:
            webbrowser.open(question.reference_url)

    def open_follow_up(self) -> None:
        """Open an in-scope follow-up or the next visible question."""
        question = self._current_question()
        if question is None:
            return

        follow_up_id = self._available_follow_up_id(question)
        next_question_id = follow_up_id or self.view.questions.question_after(
            question.question_id
        )

        if next_question_id is None:
            self.view.filters.select_level(self.requested_level)
            self.refresh_questions()
            return

        next_question = self.catalogue.questions[next_question_id]

        if not follow_up_id:
            self.view.filters.select_level(self.requested_level)

        selected_level = self.view.filters.selected_level
        if LEVEL_ORDER[next_question.minimum_level] > LEVEL_ORDER[selected_level]:
            self.view.filters.select_level(next_question.minimum_level)

        self.refresh_questions()
        self.view.questions.select_question(next_question_id)

    def open_exhibit(self, exhibit: ExhibitLink) -> None:
        """Open a local teaching exhibit in its default application."""
        exhibit_path = PROJECT_ROOT / exhibit.exhibit_path

        if not exhibit_path.is_file():
            self._show_missing_exhibit(exhibit_path)
            return

        webbrowser.open(exhibit_path.resolve().as_uri())
        self.view.set_status(f"Opened {exhibit.exhibit_name}.")

    def _available_follow_up_id(self, question: Question) -> str:
        """Return a follow-up only when it satisfies the search."""
        follow_up_id = question.follow_up_question_id

        if follow_up_id and self.view.filters.search_text:
            follow_up = self.catalogue.questions[follow_up_id]
            if not self._matches_search(follow_up):
                follow_up_id = ""

        return follow_up_id

    def _next_action_text(self, question: Question) -> str | None:
        """Describe the next available navigation action."""
        next_action_text = None
        follow_up_id = self._available_follow_up_id(question)

        if follow_up_id:
            next_action_text = "Next follow-up"
        else:
            next_question_id = self.view.questions.question_after(question.question_id)
            if next_question_id is not None:
                next_question = self.catalogue.questions[next_question_id]
                next_action_text = (
                    "Next question"
                    if next_question.topic == question.topic
                    else "Next topic"
                )

        if next_action_text is None:
            if self.view.filters.selected_level == self.requested_level:
                next_action_text = f"Restart {self.requested_level} questions"
            else:
                next_action_text = f"Return to {self.requested_level} questions"

        return next_action_text

    def _current_question(self) -> Question | None:
        """Return the current question, if one is selected."""
        if self.current_question_id is None:
            return None
        return self.catalogue.questions[self.current_question_id]

    def _show_missing_exhibit(self, exhibit_path: Path) -> None:
        """Report a missing local exhibit."""
        messagebox.showerror(
            "Exhibit not found",
            f"The exhibit could not be found:\n{exhibit_path}",
            parent=self.root,
        )


def main() -> None:
    """Load the catalogue and start the Tkinter application."""
    root = tk.Tk()
    root.withdraw()

    try:
        catalogue = load_catalogue()
    except (KeyError, OSError, ValueError) as error:
        messagebox.showerror(
            "Unable to load catalogue",
            str(error),
            parent=root,
        )
        root.destroy()
        return

    InterviewController(root, catalogue)
    root.deiconify()
    root.mainloop()


if __name__ == "__main__":
    main()
