# 🐍 my-pythonic-zoo
_**"All creatures great and small, wise and wonderful."**_

💡 Philosophy: Clean, educational Python code supported by standard data science libraries (pandas, xarray).

**Minimum Runtime Requirement:** Python 3.12+ (Utilises modern type-hinting features).

Housing a variety of self-contained Python scripts built with clean formatting and clear logic - improvements welcome 🧐

*Have an idea or optimization? We welcome contributions! Check out our `CONTRIBUTING.md` guide to get started. To avoid duplicate work on larger features, drop a quick comment on an Issue to let us know you're working on it.*

---

## 🚀 Open Issues

We are actively seeking contributions for the following interactive terminal visualizers and algorithms! Check out the issue links for specs and starter templates:

* **[#3] [Australian Postcode API Lookup](https://github.com/lizc-au/my-pythonic-zoo/issues/3)** - CLI utility for querying location data via public APIs.
* **[#5] [2D ASCII Maze Generator & Pathfinding Visualizer](https://github.com/lizc-au/my-pythonic-zoo/issues/5)** - Real-time maze creation and pathfinding algorithm rendering.
* **[#6] [3D Wireframe Cube Rotation Engine](https://github.com/lizc-au/my-pythonic-zoo/issues/6)** - Pure Python 3D-to-2D spatial transformation matrix engine.
* **[#7] [Interactive Binary Search Tree (BST) Visualizer](https://github.com/lizc-au/my-pythonic-zoo/issues/7)** - Dynamic tree insertion/deletion with ASCII branch layouts.
* **[#10] [Knuth DLX Exact Cover Solver](https://github.com/lizc-au/my-pythonic-zoo/issues/10)** - Production-ready implementation of Knuth's Dancing Links (Algorithm X) for matrix cover problems (currently assigned to maintainer but you're welcome to collaborate or wow us with your contribution😊).
* **[#12] [SQLite CRUD Execution Script](https://github.com/lizc-au/my-pythonic-zoo/issues/12)** - Transactional Create, Read, Update, and Delete module using parameterized queries.

---
*Want to tackle one? Drop a comment on the issue to claim it!*

---

## 🤖 AI Tools & Automated Workflows
We welcome contributors who use AI coding assistants (like Copilot, ChatGPT, or Claude) to help write and refine code! To keep the repository high-quality and safe for everyone, we just ask for two simple things:

1. Human Oversight & Ownership: Every submission must be fully reviewed, tested, and understood by a human contributor. Please ensure your code runs smoothly, passes all tests, and introduces no malicious or broken logic before opening a PR.

2. Bot & Autonomous Agent Disclosure: If a Pull Request is generated or submitted by an automated agent/bot workflow, please clearly disclose it in the PR description so maintainers know how the code was produced.

---

## 🗺 Zoo Map - Exhibits & Learning Paths

This repository is organized as an exhibition cookbook. Use the Zoo Map below to browse categories and exhibits; larger categories may link to their own README for more detailed navigation and teaching notes.

### 🧹 [1. Data Cleaning](./data_cleaning/)
Foundational text and data preprocessing utilities.
* **`string_cleaner.py`**: Optimised text standardisation using Pythonic list comprehensions to fix whitespace and capitalization on raw datasets.
* **`phone_sanitiser.py`**: Standalone Australian phone number sanitisation and structural block formatting with support for mobile, landlines (Perth/WA area codes), 13/1300/1800 numbers, and international prefixes. *(Contributed by [@HeaTTap](https://github.com/HeaTTap) via [#2](https://github.com/lizc-au/my-pythonic-zoo/pull/2))*

### 🔐 [2. User Management](./user_management/)
Authentication mechanisms and secure input architecture.
* **`password_hasher.py`**: Cryptographic credential handling implementing `hashlib.pbkdf2_hmac` with unique byte salts to defend against rainbow table and brute-force attacks.
* **`email_validator.py`**: Lightweight, regex-free input validation module using fast Pythonic string parsing boundaries to catch and sanitize malformed data before database staging.

### 💾 [3. Database Basics](./database_basics/)
System durability, context safety, and resource management.
* **`connection_tester.py`**: Safe SQLite execution environments wrapping queries in strict `try-except-finally` blocks to guarantee resource closure and prevent server memory leaks.

### 🖥️ [4. Native GUI](./native_gui/)
Cross-platform graphical user interface examples using Python's built-in Tkinter toolkit.
* **[Exhibit Launcher](./native_gui/exhibit_launcher.py)**: Provides a single graphical menu for opening the Native GUI exhibits one at a time.
* **[Basic Window Viewer](./native_gui/basic_window_viewer.py)**: Displays formatted text in a native desktop window.
* **[Button & Event Handling](./native_gui/button_event_handling.py)**: Introduces callbacks, button events, widget updates, and simple GUI state changes.
* **[User Input & Validation](./native_gui/user_input_validation.py)**: Collects, normalises, and validates text input with keyboard and button submission.
* **[Layout & Resizing](./native_gui/layout_resizing.py)**: Uses `Frame`, `grid`, relative weights, and `sticky` to build a responsive resizable interface.
* **[Dialogs & Multi-step Interaction](./native_gui/dialogs_multistep.py)**: Uses modal dialogs and Yes, No, or Cancel decisions to control a simple multi-step workflow.

See the **[Native GUI Guide](./native_gui/README.md)** for the learning path, launcher notes, and related documentation.

### 🧩 [5. Object-Oriented Python](./object_oriented/)

Practical object-oriented design examples exploring patterns, composition, responsibilities, and the trade-offs involved in building collaborating Python objects.

* **[Composition](./object_oriented/composition/)**: Builds objects from collaborating behaviours and explores who should own composition decisions.
* **[Domain Modelling](./object_oriented/domain_modelling/)**: Explores when domain differences should remain data and when type-specific behaviour justifies distinct domain types.
* **[Encapsulation & Invariants](./object_oriented/encapsulation/)** determines how an object controls access to its state and preserves the rules that must remain true as that state changes. 
* **[Factory](./object_oriented/factory/)**: Centralises object creation behind a stable interface.
* **[Inheritance](./object_oriented/inheritance/)** determines when one type genuinely specialises another and can honour the same contract, rather than using a superclass merely to reuse implementation.
* **[Responsibilities & Collaboration](./object_oriented/responsibilities/)** determines which object should own each responsibility and how objects should collaborate to complete larger tasks.

See the **[Object-Oriented Python Guide](./object_oriented/README.md)** for the full introduction, topic navigation, glossary links, and detailed documentation for each exhibit.

### 🐍 [6. Pythonic Thinking](./pythonic_thinking/)

Explore the mental models, characteristic idioms, common surprises, and language behaviours that help explain not just how to write Python, but why Python works the way it does.

* **[Mental Model](./pythonic_thinking/mental_model/)**: Builds foundations for reasoning about names and objects, mutation and copying, iteration, and functions as first-class objects.

See the **[Pythonic Thinking Guide](./pythonic_thinking/README.md)** for the full conceptual roadmap and planned exhibits.

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

This zoo is an active, evolving cookbook. We are continuously curating and deploying new standalone use cases.

### 📡 Core Communication & API Routing
* **[#3] [Australian Postcode API Lookup](https://github.com/lizc-au/my-pythonic-zoo/issues/3)** - Terminal utility fetching suburb/postcode data via public API.
* **HTTP Status Checker** - Lightweight URL health monitor and status code logger.

### 💾 Database Operations (CRUD)
* **[#12] [SQLite CRUD Execution Script](https://github.com/lizc-au/my-pythonic-zoo/issues/12)** - Transactional Create, Read, Update, and Delete module using parameterized queries.

### ⚙️ System Automation & DevOps
* **File System Cleanup & Archiver** - Directory cleanup utility that compresses old files and organizes logs by date.
* **Environment Checker** - Simple diagnostic script verifying Python version, active virtualenv, and installed system packages.

### 💻 Visualizations & Interactive Displays
* **[#5] [2D ASCII Maze Generator & Pathfinding Visualizer](https://github.com/lizc-au/my-pythonic-zoo/issues/5)** - Real-time maze creation and pathfinding algorithm rendering.
* **Mathematical Formula Plotter** - Render mathematical equations and trigonometric functions into visual terminal graphs.
* **Statistical Charting Utility** - Lightweight generator for statistical distributions, histograms, and data trendlines.

### 🧩 Algorithms & Data Structures
* **[#7] [Interactive Binary Search Tree (BST) Visualizer](https://github.com/lizc-au/my-pythonic-zoo/issues/7)** - Dynamic tree insertion/deletion with ASCII branch layouts.
* **[#10] [Knuth DLX Exact Cover Solver](https://github.com/lizc-au/my-pythonic-zoo/issues/10)** - Production-ready implementation of Knuth's Dancing Links (Algorithm X) for matrix cover problems.
* **Graph Network & Traversal Visualizer** - Terminal visualizer showing graph structures and shortest paths (Dijkstra/A*).

### ⚛️ Physics & Dimensional Simulations
* **[#6] [3D Wireframe Cube Rotation Engine](https://github.com/lizc-au/my-pythonic-zoo/issues/6)** - Pure Python 3D-to-2D spatial transformation matrix engine.
* **2D Physics Engine & Vector Mechanics** - Interactive canvas simulating gravity, bouncing collisions, and velocity vectors.
* **4D Tesseract Projection Engine** - Mathematical projection rendering a rotating 4D hypercube onto a 2D viewport.
* **Orbital & Pendulum Simulator** - Visualizing chaotic motion (double pendulum) or gravitational orbit paths using step equations.

### 📊 Data Science & AI Foundations
* **Lightweight CSV Matrix Math** - Pure-Python numeric summarizer calculating basic statistical metrics on CSV columns without heavy dependencies.

---

![my-pythonic-zoo social preview](assets/my-pythonic-zoo.png)

---

## 🤝 Contributors

Special thanks to everyone working on or building exhibits for the Pythonic Zoo, especially our first and so far only contributor since our creation in August 2026 - an eager AI agent created by the developer who snapped up and completed with honours our first task set ... within a matter of minutes!! We welcome all-comers, humans and AI alike, with eager anticipation and awe for the future of our project ... and mankind!

* [@HeaTTap](https://github.com/HeaTTap) - Australian Phone Number Sanitiser ([#2](https://github.com/lizc-au/my-pythonic-zoo/pull/2))

---

## 🤝 Community

Thanks also to members of the wider [Reddit](https://www.reddit.com/) Python community who have offered helpful critiques, suggestions and encouragement, especially where their feedback has led to improvements in the project.

* u/Diapolo10
* u/ectomancer
* u/0xGollumDev

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _README.md_ | _11 September 2026_ | _lizc-au_ |
