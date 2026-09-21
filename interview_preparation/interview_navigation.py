"""
interview_navigation.py

Navigation controls for the interview-preparation interface.
"""

import tkinter as tk
from collections.abc import Callable
from tkinter import ttk

from interview_preparation.interview_model import Question

LEVELS = ("Junior", "Mid-level", "Advanced")


class FilterBar(ttk.Frame):
    """Topic and interview-level selection controls."""

    def __init__(
        self,
        parent: tk.Misc,
        topics: list[str],
        on_change: Callable[[], None],
    ) -> None:
        super().__init__(parent, padding=10)
        self.topic_var = tk.StringVar(value="All topics")
        self.level_var = tk.StringVar(value="Junior")
        self.on_change = on_change

        ttk.Label(self, text="Topic:").pack(side=tk.LEFT)
        topic_box = ttk.Combobox(
            self,
            textvariable=self.topic_var,
            values=["All topics", *topics],
            state="readonly",
            width=25,
        )
        topic_box.pack(side=tk.LEFT, padx=(5, 20))
        topic_box.bind("<<ComboboxSelected>>", self._notify_change)

        ttk.Label(self, text="Interview level:").pack(side=tk.LEFT)
        level_box = ttk.Combobox(
            self,
            textvariable=self.level_var,
            values=LEVELS,
            state="readonly",
            width=12,
        )
        level_box.pack(side=tk.LEFT, padx=5)
        level_box.bind("<<ComboboxSelected>>", self._notify_change)

    @property
    def selected_topic(self) -> str:
        """Return the selected topic filter."""
        return self.topic_var.get()

    @property
    def selected_level(self) -> str:
        """Return the selected interview level."""
        return self.level_var.get()

    def select_topic(self, topic: str) -> None:
        """Change the topic without triggering the callback."""
        self.topic_var.set(topic)

    def select_level(self, level: str) -> None:
        """Change the level without triggering the callback."""
        self.level_var.set(level)

    def _notify_change(self, _event: tk.Event) -> None:
        """Notify the controller that a filter changed."""
        self.on_change()


class QuestionPanel(ttk.LabelFrame):
    """Selectable list of filtered interview questions."""

    def __init__(
        self,
        parent: tk.Misc,
        on_select: Callable[[str], None],
    ) -> None:
        super().__init__(
            parent,
            text="Questions",
            padding=8,
            relief=tk.GROOVE,
            borderwidth=2,
        )
        self.on_select = on_select
        self.question_ids: list[str] = []

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.question_list = tk.Listbox(
            self,
            exportselection=False,
            activestyle="dotbox",
            width=88,
        )
        scrollbar = ttk.Scrollbar(
            self,
            orient=tk.VERTICAL,
            command=self.question_list.yview,
        )
        self.question_list.configure(yscrollcommand=scrollbar.set)
        self.question_list.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.question_list.bind("<<ListboxSelect>>", self._notify_selection)

    def show_questions(self, questions: list[Question]) -> None:
        """Replace the list and select its first question."""
        self.question_ids = [question.question_id for question in questions]
        self.question_list.delete(0, tk.END)

        for question in questions:
            self.question_list.insert(tk.END, question.question)

        if questions:
            self._select_index(0)
            self.on_select(questions[0].question_id)

    def select_question(self, question_id: str) -> None:
        """Select a visible question by its stable ID."""
        index = self.question_ids.index(question_id)
        self._select_index(index)
        self.on_select(question_id)

    def question_after(self, question_id: str) -> str | None:
        """Return the next visible question ID, if one exists."""
        current_index = self.question_ids.index(question_id)
        next_index = current_index + 1

        if next_index < len(self.question_ids):
            return self.question_ids[next_index]
        return None

    def _select_index(self, index: int) -> None:
        """Update the visible Listbox selection."""
        self.question_list.selection_clear(0, tk.END)
        self.question_list.selection_set(index)
        self.question_list.activate(index)
        self.question_list.see(index)

    def _notify_selection(self, _event: tk.Event) -> None:
        """Notify the controller when the user selects a question."""
        selection = self.question_list.curselection()
        if selection:
            self.on_select(self.question_ids[selection[0]])
