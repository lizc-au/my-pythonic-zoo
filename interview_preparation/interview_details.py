"""
interview_details.py

Question-detail components for the interview interface.
"""

import tkinter as tk
from collections.abc import Callable
from dataclasses import dataclass
from tkinter import ttk

from interview_preparation.interview_model import AnswerPoint, ExhibitLink, Question


@dataclass(frozen=True)
class DetailActions:
    """Controller actions used by the question-detail panels."""

    reveal_answer: Callable[[], None]
    open_reference: Callable[[], None]
    open_follow_up: Callable[[], None]
    open_exhibit: Callable[[ExhibitLink], None]


class AnswerPanel(ttk.LabelFrame):
    """Scrollable display for answer points and code snippets."""

    def __init__(self, parent: tk.Misc) -> None:
        super().__init__(
            parent,
            text="Answer points",
            padding=8,
            relief=tk.GROOVE,
            borderwidth=2,
        )
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.answer_text = tk.Text(
            self,
            wrap=tk.WORD,
            state=tk.DISABLED,
            height=14,
            padx=8,
            pady=8,
        )
        scrollbar = ttk.Scrollbar(
            self,
            orient=tk.VERTICAL,
            command=self.answer_text.yview,
        )
        self.answer_text.configure(yscrollcommand=scrollbar.set)
        self.answer_text.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.answer_text.tag_configure(
            "code",
            font="TkFixedFont",
            background="#eeeeee",
            lmargin1=20,
            lmargin2=20,
            spacing1=4,
            spacing3=8,
        )

    def clear(self) -> None:
        """Clear and lock the answer display."""
        self.answer_text.configure(state=tk.NORMAL)
        self.answer_text.delete("1.0", tk.END)
        self.answer_text.configure(state=tk.DISABLED)

    def show_answers(self, answers: list[AnswerPoint]) -> None:
        """Display answer explanations and optional code snippets."""
        self.answer_text.configure(state=tk.NORMAL)
        self.answer_text.delete("1.0", tk.END)

        for answer in answers:
            self.answer_text.insert(tk.END, f"• {answer.explanation}\n")
            if answer.code_example:
                self.answer_text.insert(tk.END, f"{answer.code_example}\n", "code")

        if not answers:
            self.answer_text.insert(tk.END, "No answer points are available yet.")

        self.answer_text.configure(state=tk.DISABLED)


class ExhibitPanel(ttk.LabelFrame):
    """Related teaching exhibits for the selected question."""

    def __init__(
        self,
        parent: tk.Misc,
        on_open: Callable[[ExhibitLink], None],
    ) -> None:
        super().__init__(
            parent,
            text="Related exhibits",
            padding=8,
            relief=tk.GROOVE,
            borderwidth=2,
        )
        self.on_open = on_open
        self.exhibits: list[ExhibitLink] = []

        self.columnconfigure(0, weight=1)

        self.exhibit_list = tk.Listbox(
            self,
            exportselection=False,
            height=4,
        )
        self.exhibit_list.grid(row=0, column=0, sticky="ew")
        self.exhibit_list.bind("<Double-Button-1>", self._open_selection)

        self.open_button = ttk.Button(
            self,
            text="Open selected exhibit",
            command=self._open_selection,
        )
        self.open_button.grid(row=1, column=0, sticky="w", pady=(8, 0))

    def show_exhibits(self, exhibits: list[ExhibitLink]) -> None:
        """Display related exhibit names and relationship notes."""
        self.exhibits = exhibits
        self.exhibit_list.delete(0, tk.END)

        for exhibit in exhibits:
            self.exhibit_list.insert(
                tk.END,
                f"{exhibit.exhibit_name}: {exhibit.relationship}",
            )

        if exhibits:
            self.exhibit_list.selection_set(0)
            self.open_button.configure(state=tk.NORMAL)
        else:
            self.open_button.configure(state=tk.DISABLED)

    def _open_selection(self, _event: tk.Event | None = None) -> None:
        """Ask the controller to open the selected exhibit."""
        selection = self.exhibit_list.curselection()
        if selection:
            self.on_open(self.exhibits[selection[0]])


class DetailPanel(ttk.Frame):
    """Question details, answers, exhibits, and navigation actions."""

    def __init__(
        self,
        parent: tk.Misc,
        actions: DetailActions,
    ) -> None:
        super().__init__(parent, padding=(12, 5))
        self.question_var = tk.StringVar()
        self.knowledge_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        self._build_question_header(actions.reveal_answer)

        self.answer_panel = AnswerPanel(self)
        self.answer_panel.grid(row=3, column=0, sticky="nsew")

        self.exhibit_panel = ExhibitPanel(self, actions.open_exhibit)
        self.exhibit_panel.grid(row=4, column=0, sticky="ew", pady=(10, 0))

        self._build_navigation(actions)

    def _build_question_header(self, reveal_answer: Callable[[], None]) -> None:
        """Create the question heading and reveal control."""
        ttk.Label(
            self,
            textvariable=self.question_var,
            font=("TkDefaultFont", 14, "bold"),
            wraplength=600,
            justify=tk.LEFT,
        ).grid(row=0, column=0, sticky="ew", pady=(0, 8))

        ttk.Label(
            self,
            textvariable=self.knowledge_var,
            wraplength=600,
            justify=tk.LEFT,
        ).grid(row=1, column=0, sticky="ew", pady=(0, 10))

        self.reveal_button = ttk.Button(
            self,
            text="Reveal answer",
            command=reveal_answer,
        )
        self.reveal_button.grid(row=2, column=0, sticky="w", pady=(0, 8))

    def _build_navigation(self, actions: DetailActions) -> None:
        """Create centred reference and follow-up buttons."""
        navigation = ttk.Frame(self)
        navigation.grid(row=5, column=0, sticky="ew", pady=(10, 0))
        navigation.columnconfigure(0, weight=1)
        navigation.columnconfigure(3, weight=1)

        self.reference_button = ttk.Button(
            navigation,
            text="Open Python reference",
            command=actions.open_reference,
        )
        self.reference_button.grid(row=0, column=1, padx=(0, 10))

        self.follow_up_button = ttk.Button(
            navigation,
            text="Next follow-up",
            command=actions.open_follow_up,
        )
        self.follow_up_button.grid(row=0, column=2, padx=(10, 0))

    def show_question(
        self,
        question: Question,
        exhibits: list[ExhibitLink],
        next_action_text: str | None,
    ) -> None:
        """Display a question while keeping its answer hidden."""
        self.question_var.set(question.question)
        self.knowledge_var.set(
            f"Tests knowledge of: {question.tests_knowledge_of}\n"
            f"Minimum level: {question.minimum_level}"
        )
        self.answer_panel.clear()
        self.exhibit_panel.show_exhibits(exhibits)
        self.reveal_button.configure(state=tk.NORMAL)
        self.reference_button.configure(state=tk.NORMAL)
        if next_action_text is None:
            self.follow_up_button.configure(
                text="End of selection",
                state=tk.DISABLED,
            )
        else:
            self.follow_up_button.configure(
                text=next_action_text,
                state=tk.NORMAL,
            )

    def show_empty(self) -> None:
        """Display an empty-filter result and disable actions."""
        self.question_var.set("No questions match these filters.")
        self.knowledge_var.set("")
        self.answer_panel.clear()
        self.exhibit_panel.show_exhibits([])
        self.reveal_button.configure(state=tk.DISABLED)
        self.reference_button.configure(state=tk.DISABLED)
        self.follow_up_button.configure(state=tk.DISABLED)
