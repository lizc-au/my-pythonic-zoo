# Interview Preparation

This section provides a structured catalogue and Tkinter viewer for common Python interview questions.

The questions guide learners toward the knowledge being assessed, concise answer points, trusted Python references, and relevant teaching exhibits throughout My Pythonic Zoo. The aim is understanding and explanation rather than memorising fixed answers.

> **Work in progress:** This is a growing learning resource, not an exhaustive list of Python interview questions. Further questions, answer points, code snippets, and exhibit links are planned as the Zoo develops. The catalogue may never be considered completely finished because interview subjects and expectations continue to evolve. Suggestions and corrections are welcome.

The current viewer supports self-review by revealing expected answer points; it does not yet assess or score answers entered by the learner.

## Interview Viewer

The Tkinter viewer allows learners to:

- Filter questions by topic and interview level.
- Search question text, topics, tags, and the knowledge being assessed.
- Reveal concise answer points and small code examples.
- Follow related questions from introductory concepts into deeper material.
- Open official Python references.
- Open related runnable exhibits from the Zoo.
- Return to the originally selected level after temporarily following a harder question.

Search is case-insensitive and uses literal substring matching. While search results are active, follow-up navigation remains within those results rather than opening an unrelated question outside the search scope.

On Windows, launch the application without a console window by double-clicking:

```text
launch_interview_preparation.pyw
```

Or run it from the repository root:

```powershell
pythonw interview_preparation\launch_interview_preparation.pyw
```

## Application Structure

The viewer uses a Model-View-Controller structure.

| File | Responsibility |
|---|---|
| `interview_model.py` | Loads and represents questions, answer points, and exhibit links |
| `interview_view.py` | Composes the complete Tkinter interface |
| `interview_navigation.py` | Provides topic, level, and question-selection controls |
| `interview_details.py` | Displays questions, answers, code examples, exhibits, and navigation actions |
| `interview_controller.py` | Coordinates catalogue data, user actions, filtering, and navigation |
| `launch_interview_preparation.pyw` | Starts the application without a console window on Windows |

## Question Catalogue

`interview_questions.csv` stores one interview question per row.

| Column | Purpose |
|---|---|
| `question_id` | Stable unique identifier |
| `topic` | Main subject area |
| `minimum_level` | Earliest level at which the knowledge would reasonably be expected |
| `question` | The interview question |
| `tests_knowledge_of` | The underlying knowledge or skill being assessed |
| `follow_up_question_id` | Optional ID of the next related question |
| `tags` | Terms used for searching and filtering |
| `reference_url` | Trusted supporting resource |
| `active` | Whether the question is currently included |

A question remains applicable above its `minimum_level`; the expected depth of the answer may increase.

`follow_up_question_id` refers to another row in the catalogue. A blank value ends that related-question sequence.

## Answer Points

`answer_points.csv` stores the ideas that a sound answer should cover. A question may have several ordered answer points.

| Column | Purpose |
|---|---|
| `answer_point_id` | Stable unique identifier |
| `question_id` | Question receiving this answer point |
| `minimum_level` | Earliest level at which this depth would reasonably be expected |
| `display_order` | Order in which the answer point is displayed |
| `explanation` | Concise prose explaining the expected knowledge |
| `code_example` | Optional code snippet of no more than ten displayed lines |

Stored `\n` markers in `code_example` are converted into line breaks by the Model before display. Code snippets support the concise answer; fuller runnable examples belong in teaching exhibits.

## Exhibit Links

`question_exhibits.csv` connects questions to relevant teaching examples. A question may link to several exhibits, including conceptual explanations and practical use cases.

| Column | Purpose |
|---|---|
| `exhibit_link_id` | Stable unique identifier |
| `question_id` | Question receiving this exhibit link |
| `display_order` | Order in which the exhibit is displayed |
| `exhibit_name` | Learner-facing exhibit name |
| `exhibit_path` | Repository-relative path to the exhibit |
| `relationship` | Explanation of how the exhibit supports the question |

Automated tests validate catalogue columns, unique IDs, question relationships, terminating follow-up sequences, answer ordering, code-example length, exhibit ordering, and local exhibit paths.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _interview_preparation/README.md_ | _22 September 2026_ | _lizc-au_ |

---
