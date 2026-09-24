# my-pythonic-zoo

[![CI & Policy Checks](https://github.com/lizc-au/my-pythonic-zoo/actions/workflows/ci.yml/badge.svg)](https://github.com/lizc-au/my-pythonic-zoo/actions/workflows/ci.yml) [![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

_**All creatures great and small, wise and wonderful.**_

A growing collection of small, runnable Python exhibits for learning how code works. Some topics form step-by-step paths from a simple mental model to a larger program; Python 3.12 or newer is required.

## Explore the Zoo

| Learning area | What you can explore | Start here |
| :--- | :--- | :--- |
| **Algorithms & Data Structures** | Binary search trees, exact cover, Algorithm X, and Dancing Links | [Algorithms guide](./algorithms/README.md) |
| **Pythonic Thinking** | Names and objects, types, iteration, and context managers | [Pythonic Thinking guide](./pythonic_thinking/README.md) |
| **Object-Oriented Python** | Composition, domain models, encapsulation, factories, inheritance, and responsibilities | [Object-Oriented guide](./object_oriented/README.md) |
| **Native GUI** | Tkinter windows, events, validation, layout, dialogs, and an integrated showcase | [Native GUI guide](./native_gui/README.md) |
| **Data Cleaning** | Text standardisation and Australian phone number formatting | [Data Cleaning folder](./data_cleaning/) |
| **Database Basics** | SQLite connection handling and transactional CRUD operations | [Database Basics folder](./database_basics/) |
| **User Management** | Password hashing and email input validation | [User Management folder](./user_management/) |
| **Interview Preparation** | Searchable questions with answer points, references, and related exhibits | [Interview Preparation guide](./interview_preparation/README.md) |

Each guide gives you the study order and links to its exhibits. You can also open a single script and follow its comments at your own pace.

## Try an Exhibit

From a terminal, run these commands one at a time:

| Step | Command | Note |
| :--- | :--- | :--- |
| Clone | `git clone https://github.com/lizc-au/my-pythonic-zoo.git` | Skip if you already have the repo. |
| Enter the folder | `cd my-pythonic-zoo` | Run the remaining commands here. |
| Check Python | `python --version` | Use Python 3.12 or newer. |
| Run a small example | `python data_cleaning/string_cleaner.py` | This exhibit needs no extra packages. |

On Windows, `py -3.12` can replace `python` if that is how your Python installation is registered. Many other exhibits also run directly; check their category guides for prerequisites or GUI launchers.

<details>
<summary>Development tools and quality checks</summary>

| Tool or file | Role | Where to look |
| :--- | :--- | :--- |
| Python virtual environment | Keep project packages separate from other projects | `python -m venv .venv` |
| VS Code or another editor | Read, run, and debug exhibits | Open the cloned repository folder. |
| Git and GitHub | Track changes and propose contributions | [Contributing guide](./CONTRIBUTING.md) |
| `pyproject.toml` | Python 3.12 target, dependency groups, Ruff, and mypy settings | [Project configuration](./pyproject.toml) |
| Quality script | Run formatting, linting, type checks, and tests after installing development dependencies | `python scripts/check_quality.py` |

</details>

## Contribute

Ideas, corrections, new exhibits, and reviews are welcome. Read [CONTRIBUTING.md](./CONTRIBUTING.md), and create or comment on an [issue](https://github.com/lizc-au/my-pythonic-zoo/issues) before starting a larger feature so work can be coordinated.

<details>
<summary>AI assistance and contributor expectations</summary>

AI coding assistants are welcome when a human contributor reviews, understands, and tests the submitted work. Disclose a pull request generated or submitted by an automated agent or bot in its description.

This project uses ChatGPT interactively for pair programming, review, documentation, testing, and exploring Python concepts. @lizc-au reviews and maintains the project and its contributions; the repository is not autonomously developed or maintained by AI agents.

</details>

<details>
<summary>Upcoming exhibits and longer learning paths</summary>

This is an evolving learning resource. An idea may become one focused exhibit or a series of small steps as its prerequisites become clear.

| Area | Ideas in progress or under consideration |
| :--- | :--- |
| Communication and APIs | [Australian Postcode API Lookup (Issue #3)](https://github.com/lizc-au/my-pythonic-zoo/issues/3); HTTP status checker |
| Automation | Safe file management and archiving; environment checker |
| Visualisation | Maze generation and pathfinding; mathematical plotting; statistics and data displays |
| Algorithms | [Binary search tree progression (Issue #7)](https://github.com/lizc-au/my-pythonic-zoo/issues/7); node relationships, traversal, and shortest paths |
| Physics and dimensions | 3D rotation and projection; vectors and 2D physics; later dimensional and motion simulations |
| Data science | Lightweight CSV matrix maths |

Some ideas are deliberately weird and wonderful. Curiosity about how something works is a good reason to build a small experiment.

</details>

## People Behind the Exhibits

| Contributor | Contribution |
| :--- | :--- |
| [@HeaTTap](https://github.com/HeaTTap) | [Australian Phone Number Sanitiser (#2)](https://github.com/lizc-au/my-pythonic-zoo/pull/2) |
| [@aletgdev](https://github.com/aletgdev) | [Transactional SQLite CRUD (#48)](https://github.com/lizc-au/my-pythonic-zoo/pull/48) |
| [@Reh1t](https://github.com/Reh1t) | [BST Module 1: Structure and Ordering (#55)](https://github.com/lizc-au/my-pythonic-zoo/pull/55) |

Thanks also to Reddit community members u/Diapolo10, u/ectomancer, and u/0xGollumDev for critiques, suggestions, and encouragement.

![my-pythonic-zoo social preview](assets/my-pythonic-zoo.png)

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
