"""
interview_view.py

Compose the Tkinter view for the interview-preparation application.
"""

import tkinter as tk
from collections.abc import Callable
from dataclasses import dataclass
from tkinter import ttk

from interview_preparation.interview_details import DetailActions, DetailPanel
from interview_preparation.interview_model import ExhibitLink
from interview_preparation.interview_navigation import FilterBar, QuestionPanel


@dataclass(frozen=True)
class ViewCallbacks:
    """Actions supplied to the view by the controller."""

    filter_changed: Callable[[], None]
    question_selected: Callable[[str], None]
    reveal_answer: Callable[[], None]
    open_reference: Callable[[], None]
    open_follow_up: Callable[[], None]
    open_exhibit: Callable[[ExhibitLink], None]


class InterviewView(ttk.Frame):
    """Compose the navigation and detail portions of the interface."""

    def __init__(
        self,
        root: tk.Tk,
        topics: list[str],
        callbacks: ViewCallbacks,
    ) -> None:
        super().__init__(root)
        self.pack(fill=tk.BOTH, expand=True)

        self.status_var = tk.StringVar(value="Select a question to begin.")
        self._configure_window(root)

        self.filters = FilterBar(self, topics, callbacks.filter_changed)
        self.filters.pack(fill=tk.X)

        main_pane = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        main_pane.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.questions = QuestionPanel(main_pane, callbacks.question_selected)
        detail_actions = DetailActions(
            reveal_answer=callbacks.reveal_answer,
            open_reference=callbacks.open_reference,
            open_follow_up=callbacks.open_follow_up,
            open_exhibit=callbacks.open_exhibit,
        )
        self.details = DetailPanel(main_pane, detail_actions)

        main_pane.add(self.questions, weight=2)
        main_pane.add(self.details, weight=3)

        ttk.Label(
            self,
            textvariable=self.status_var,
            anchor=tk.W,
            padding=(10, 5),
        ).pack(fill=tk.X)

    @staticmethod
    def _configure_window(root: tk.Tk) -> None:
        """Set the window title, size, and starting position."""
        window_width = 1050
        left_position = max((root.winfo_screenwidth() - window_width) // 2, 0)
        root.title("My Pythonic Zoo - Interview Preparation")
        root.geometry(f"{window_width}x600+{left_position}+20")
        root.minsize(800, 500)

    def set_status(self, message: str) -> None:
        """Update the status line."""
        self.status_var.set(message)
