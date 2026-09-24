# Interview Preparation

Explore Python interview questions through the knowledge each one tests, concise answer points, and links to trusted references and Zoo exhibits. Use the Tkinter viewer for self-review rather than memorising a fixed script.

The catalogue is growing and is not an exhaustive question bank. The viewer reveals expected answer points but does not assess or score answers entered by a learner.

## Use the Viewer

| Action | What it does |
| :--- | :--- |
| Filter | Choose a topic and minimum interview level. |
| Search | Match question text, topics, tags, and the knowledge being assessed. |
| Reveal | Show answer points and short code examples when ready. |
| Follow up | Move from an introductory question to related deeper questions. |
| Explore | Open official Python references and related runnable Zoo exhibits. |
| Return | Go back to the selected level after visiting a harder follow-up. |

Search ignores letter case and matches literal text. Follow-up navigation stays within the active search results.

On Windows, double-click [`launch_interview_preparation.pyw`](./launch_interview_preparation.pyw) to open the viewer without a console. From the repository root, the equivalent command in the terminal is:-

`pythonw interview_preparation\launch_interview_preparation.pyw`.

<details>
<summary>How the application is organised</summary>

The viewer separates catalogue data, interface presentation, and user actions with a Model-View-Controller structure.

| File | Responsibility |
| :--- | :--- |
| [`interview_model.py`](./interview_model.py) | Load questions, answer points, and exhibit links. |
| [`interview_view.py`](./interview_view.py) | Assemble the Tkinter interface. |
| [`interview_navigation.py`](./interview_navigation.py) | Provide topic, level, and question controls. |
| [`interview_details.py`](./interview_details.py) | Show answers, examples, exhibits, and navigation actions. |
| [`interview_controller.py`](./interview_controller.py) | Coordinate data, filtering, selection, and navigation. |
| [`launch_interview_preparation.pyw`](./launch_interview_preparation.pyw) | Start the Windows application without a console. |

</details>

<details>
<summary>Question catalogue fields</summary>

[`interview_questions.csv`](./interview_questions.csv) stores one question per row.

| Column | Purpose |
| :--- | :--- |
| `question_id` | Stable unique identifier. |
| `topic` | Main subject. |
| `minimum_level` | Earliest level where this knowledge is reasonably expected. |
| `question` | Interview question text. |
| `tests_knowledge_of` | Underlying knowledge or skill being assessed. |
| `follow_up_question_id` | Optional next question in a related sequence. |
| `tags` | Search and filter terms. |
| `reference_url` | Trusted supporting resource. |
| `active` | Whether the viewer includes the question. |

A question remains relevant above its minimum level, though the expected answer may go deeper. A blank `follow_up_question_id` ends a sequence.

</details>

<details>
<summary>Answer points and exhibit link fields</summary>

[`answer_points.csv`](./answer_points.csv) stores ordered ideas a sound answer should cover. A question may have several points at different minimum levels.

| Answer column | Purpose |
| :--- | :--- |
| `answer_point_id` | Stable unique identifier. |
| `question_id` | Question receiving the point. |
| `minimum_level` | Earliest level where this depth is expected. |
| `display_order` | Order shown in the viewer. |
| `explanation` | Concise expected knowledge. |
| `code_example` | Optional snippet of at most ten displayed lines. |

Stored `\n` markers become line breaks before display. Fuller runnable demonstrations belong in Zoo exhibits.

[`question_exhibits.csv`](./question_exhibits.csv) connects a question to one or more relevant teaching examples.

| Exhibit column | Purpose |
| :--- | :--- |
| `exhibit_link_id` | Stable unique identifier. |
| `question_id` | Question receiving the link. |
| `display_order` | Order shown in the viewer. |
| `exhibit_name` | Learner-facing name. |
| `exhibit_path` | Repository-relative exhibit path. |
| `relationship` | How the exhibit supports the question. |

Automated tests check catalogue fields, unique IDs, relationships, terminating follow-up sequences, ordering, snippet length, and local exhibit paths.

</details>

Suggestions and corrections are welcome through the [Issues page](https://github.com/lizc-au/my-pythonic-zoo/issues).

---

[Return to the Zoo map](../README.md) to explore another area.

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
