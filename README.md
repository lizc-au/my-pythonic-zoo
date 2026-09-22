# 🐍 my-pythonic-zoo

[![CI & Policy Checks](https://github.com/lizc-au/my-pythonic-zoo/actions/workflows/ci.yml/badge.svg)](https://github.com/lizc-au/my-pythonic-zoo/actions/workflows/ci.yml) [![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

_**"All creatures great and small, wise and wonderful."**_

💡 Philosophy: Clean, educational Python code supported by standard data science libraries (pandas, xarray).

**Minimum Runtime Requirement:** Python 3.12+ (Utilises modern type-hinting features).

Housing a variety of self-contained Python scripts built with clean formatting and clear logic - improvements welcome 🧐

*Have an idea or optimization? We welcome contributions! Check out our `CONTRIBUTING.md` guide to get started. To avoid duplicate work on larger features, drop a quick comment on an Issue to let us know you're working on it.*

---

## 🚀 Open Issues

The following issues are currently open for contributions. Check each issue for its scope, learning goals, and contribution guidance:

* **[#3] [Australian Postcode API Lookup](https://github.com/lizc-au/my-pythonic-zoo/issues/3)** - CLI utility for querying location data via public APIs.
* **[#52] [Binary Search Trees - Module 2: Traversal, Insertion and Searching](https://github.com/lizc-au/my-pythonic-zoo/issues/52)** - The next stage in the progressive BST learning path established in parent Issue #7.

---
*Want to tackle one? Drop a comment on the issue to claim it!*

---

## 🤖 AI Tools & Automated Workflows
We welcome contributors who use AI coding assistants (like Copilot, ChatGPT, or Claude) to help write and refine code! To keep the repository high-quality and safe for everyone, we just ask for two simple things:

1. Human Oversight & Ownership: Every submission must be fully reviewed, tested, and understood by a human contributor. Please ensure your code runs smoothly, passes all tests, and introduces no malicious or broken logic before opening a PR.

2. Bot & Autonomous Agent Disclosure: If a Pull Request is generated or submitted by an automated agent/bot workflow, please clearly disclose it in the PR description so maintainers know how the code was produced.

---

## 🗺 Zoo Map - Exhibits & Learning Paths

This repository is organized as a collection of practical Python exhibits and learning paths. Use the Zoo Map below to browse categories and exhibits; larger categories may link to their own README for more detailed navigation and teaching notes.

### 🧩 [Algorithms & Data Structures](./algorithms/)

Explore algorithms by building the mental models, data structures, and operations
behind them before combining those pieces into complete implementations.

* **[Binary Search Trees](./algorithms/binary_search_tree/)**: A progressive
  learning path beginning with linked nodes and the full BST ordering invariant,
  then continuing through traversal, insertion, searching, deletion, rendering,
  and an interactive terminal visualizer.

* **[Dancing Links](./algorithms/dancing_links/)**: A structured study sequence
  progressing from Exact Cover and Algorithm X through linked nodes, circular
  structures, toroidal matrices, and reversible cover/uncover operations before
  combining them into a complete Dancing Links implementation.

See the **[Algorithms Guide](./algorithms/README.md)** for the full study sequence
and detailed teaching progression.

### 🧹 [Data Cleaning](./data_cleaning/)
Foundational text and data preprocessing utilities.
* **`string_cleaner.py`**: Optimised text standardisation using Pythonic list comprehensions to fix whitespace and capitalization on raw datasets.
* **`phone_sanitiser.py`**: Standalone Australian phone number sanitisation and structural block formatting with support for mobile, landlines (Perth/WA area codes), 13/1300/1800 numbers, and international prefixes. *(Contributed by [@HeaTTap](https://github.com/HeaTTap) via [#2](https://github.com/lizc-au/my-pythonic-zoo/pull/2))*

### 💾 [Database Basics](./database_basics/)
System durability, context safety, and resource management.
* **`connection_tester.py`**: Safe SQLite execution environments wrapping queries in strict `try-except-finally` blocks to guarantee resource closure and prevent server memory leaks.
* **`sqlite_crud.py`**: Transaction-safe SQLite Create, Read, Update, and Delete operations using context managers, parameterized queries, and dictionary-like query results.

### 🖥️ [Native GUI](./native_gui/)
Cross-platform graphical user interface examples using Python's built-in Tkinter toolkit.
* **[Exhibit Launcher](./native_gui/exhibit_launcher.py)**: Provides a single graphical menu for opening the Native GUI exhibits one at a time.
* **[Comprehensive Tkinter Showcase](./native_gui/tkinter_showcase.py)**: Combines persistent navigation, responsive layout, validation, keyboard events, and dialogs in one clean application-style example.
* **[Basic Window Viewer](./native_gui/basic_window_viewer.py)**: Displays formatted text in a native desktop window.
* **[Button & Event Handling](./native_gui/button_event_handling.py)**: Introduces callbacks, button events, widget updates, and simple GUI state changes.
* **[User Input & Validation](./native_gui/user_input_validation.py)**: Collects, normalises, and validates text input with keyboard and button submission.
* **[Layout & Resizing](./native_gui/layout_resizing.py)**: Uses `Frame`, `grid`, relative weights, and `sticky` to build a responsive resizable interface.
* **[Dialogs & Multi-step Interaction](./native_gui/dialogs_multistep.py)**: Uses modal dialogs and Yes, No, or Cancel decisions to control a simple multi-step workflow.

See the **[Native GUI Guide](./native_gui/README.md)** for the learning path, launcher notes, and related documentation.

### 🧩 [Object-Oriented Python](./object_oriented/)

Practical object-oriented design examples exploring patterns, composition, responsibilities, and the trade-offs involved in building collaborating Python objects.

* **[Composition](./object_oriented/composition/)**: Builds objects from collaborating behaviours and explores who should own composition decisions.
* **[Domain Modelling](./object_oriented/domain_modelling/)**: Explores when domain differences should remain data and when type-specific behaviour justifies distinct domain types.
* **[Encapsulation & Invariants](./object_oriented/encapsulation/)** determines how an object controls access to its state and preserves the rules that must remain true as that state changes. 
* **[Factory](./object_oriented/factory/)**: Centralises object creation behind a stable interface.
* **[Inheritance](./object_oriented/inheritance/)** determines when one type genuinely specialises another and can honour the same contract, rather than using a superclass merely to reuse implementation.
* **[Responsibilities & Collaboration](./object_oriented/responsibilities/)** determines which object should own each responsibility and how objects should collaborate to complete larger tasks.

See the **[Object-Oriented Python Guide](./object_oriented/README.md)** for the full introduction, topic navigation, glossary links, and detailed documentation for each exhibit.

### 🐍 [Pythonic Thinking](./pythonic_thinking/)

Explore the mental models, characteristic idioms, common surprises, and language behaviours that help explain not just how to write Python, but why Python works the way it does.

* **[Mental Model](./pythonic_thinking/mental_model/)**: Builds foundations for reasoning about names and objects, mutation and copying, iteration, and functions as first-class objects.
* **[Type System](./pythonic_thinking/type_system/)**: Explores Python's dynamic type system, type annotations, type relationships, and how static analysis tools reason about Python code.
* **[Context Managers](./pythonic_thinking/context_managers/)**: Explores Python's `with` statement and context manager protocol for reliable lifecycle, resource, and exception handling.

See the **[Pythonic Thinking Guide](./pythonic_thinking/README.md)** for the full conceptual roadmap and planned exhibits.

### 🔐 [User Management](./user_management/)
Authentication mechanisms and secure input architecture.
* **`password_hasher.py`**: Cryptographic credential handling implementing `hashlib.pbkdf2_hmac` with unique byte salts to defend against rainbow table and brute-force attacks.
* **`email_validator.py`**: Lightweight, regex-free input validation module using fast Pythonic string parsing boundaries to catch and sanitize malformed data before database staging.

---

## 🎓 [Interview Preparation](./interview_preparation/)

Explore a growing catalogue of Python interview questions designed to identify the underlying knowledge being assessed. Questions include minimum expected levels, related follow-ups, concise answer points, small code examples, trusted Python references, and links to relevant teaching exhibits throughout the Zoo.

Use the Tkinter viewer to search questions and filter them by topic and level, reveal answers, follow related question sequences, and open supporting references and runnable exhibits. This remains a work in progress, with further questions and supporting material planned.

---

## 🧪 Code Quality
This repository enforces strict code hygiene, style guidelines, and bug prevention rules using the **Ruff** linter. Configuration maps are located in `pyproject.toml`.

---

## 🚀 How to Run an Exhibit

Every script in this zoo includes its own mock data block and execution wrapper. You do not need to install complex dependencies or configure global environments.

1. Clone or fork this repository.
2. Navigate to the desired folder.
3. Run the script directly from your terminal:
   ```bash
   python string_cleaner.py
   ```
4. If using VS Code or similar, right-click on python file to choose `Run Python File in Terminal`.

---

## 🛠️ Work in Progress & Upcoming Exhibits

This zoo is an active, evolving learning resource. Upcoming ideas may become focused standalone exhibits or progressive series, depending on the concepts and prerequisites involved.

Some ideas are deliberately weird and wonderful. Learning often begins by wondering how something marvellous works and asking, “Could I build that myself?”

### 📡 Core Communication & API Routing
* **[#3] [Australian Postcode API Lookup](https://github.com/lizc-au/my-pythonic-zoo/issues/3)** - Terminal utility fetching suburb/postcode data via public API.
* **HTTP Status Checker** - Lightweight URL health monitor and status code logger.

### ⚙️ System Automation & DevOps
* **Safe File Management & Archiving** - Progressive exhibits exploring directory inspection, file selection rules, dated organization, and recoverable archiving.
* **Environment Checker** - Simple diagnostic script verifying Python version, active virtualenv, and installed system packages.

### 💻 Visualizations & Interactive Displays
* **Maze Generation & Pathfinding** - Progressive exhibits exploring grid representation, maze generation, pathfinding algorithms, and terminal visualization.
* **Mathematical Functions & Plotting** - Progressive exhibits exploring coordinates, function evaluation, scaling, and terminal graph rendering.
* **Statistics & Data Visualization** - Progressive exhibits exploring distributions, summary statistics, histograms, and data trends.

### 🧩 Algorithms & Data Structures
* **[#7] [Binary Search Trees: From Linked Nodes to an Interactive Visualizer](https://github.com/lizc-au/my-pythonic-zoo/issues/7)** - Module 1 is complete; Modules 2 to 4 will continue through traversal, insertion, searching, deletion, rendering, and an interactive terminal visualizer.
* **Graphs, Traversal & Pathfinding** - Progressive exhibits exploring graph representation, traversal, shortest-path algorithms, and terminal visualization.

### ⚛️ Physics & Dimensional Simulations
* **3D Rotation & Projection** - Progressive exhibits exploring coordinates, rotation mathematics, 3D-to-2D projection, and terminal wireframe rendering.
* **Vectors & 2D Physics** - Progressive exhibits exploring vector movement, gravity, velocity, and collision behaviour through visual simulations.
* **Advanced Dimensional Projection** - Later exhibits building on the 3D progression to explore four-dimensional coordinates and projection through a rotating tesseract.
* **Motion & Dynamic Systems** - Progressive exhibits exploring time-step simulation, pendulum motion, orbital paths, and eventually chaotic systems.

### 📊 Data Science & AI Foundations
* **Lightweight CSV Matrix Math** - Pure-Python numeric summarizer calculating basic statistical metrics on CSV columns without heavy dependencies.

---

![my-pythonic-zoo social preview](assets/my-pythonic-zoo.png)

---

## AI Assistance Disclosure

This project is developed with interactive assistance from ChatGPT for pair programming, code review, documentation, testing, and exploring Python concepts. This repository is not autonomously developed or maintained by AI agents. AI is used collaboratively, with human review, decision-making, and a fair amount of blood, sweat and tears throughout. All design decisions, code changes, and contributions are reviewed, tested, and ultimately maintained by @lizc-au.

---

## 🤝 Contributors

Special thanks to everyone who has contributed to the Pythonic Zoo. Contributions, ideas, reviews, and improvements that help make the Zoo a better learning resource are greatly appreciated.

* [@HeaTTap](https://github.com/HeaTTap) - Australian Phone Number Sanitiser ([#2](https://github.com/lizc-au/my-pythonic-zoo/pull/2))
* [@aletgdev](https://github.com/aletgdev) - Transactional SQLite CRUD Execution Script ([#48](https://github.com/lizc-au/my-pythonic-zoo/pull/48))
* [@Reh1t](https://github.com/Reh1t) - Binary Search Trees Module 1: Structure and Ordering ([#55](https://github.com/lizc-au/my-pythonic-zoo/pull/55))

---

## 🤝 Community

Thanks also to members of the wider [Reddit](https://www.reddit.com/) Python community who have offered helpful critiques, suggestions and encouragement, especially where their feedback has led to improvements in the project.

* u/Diapolo10
* u/ectomancer
* u/0xGollumDev

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _README.md_ | _22 September 2026_ | _lizc-au_ |

---
