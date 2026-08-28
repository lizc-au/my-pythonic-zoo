# 🐍 my-pythonic-zoo

**Minimum Runtime Requirement:** Python 3.10+ (Utilises modern type-hinting features).

Housing a variety of self-contained Python scripts built with clean formatting and clear logic. - improvements welcome 🧐

*Have an idea or optimization? We welcome contributions! Check out our CONTRIBUTING.md guide to get started. To avoid duplicate work on larger features, drop a quick comment on an Issue to let us know you're working on it.*

---

## 🤖 AI & Automated Contributions
We welcome contributions assisted by AI tools and autonomous workflows, provided that:
1. **Full Disclosure:** All AI-generated or agent-assisted code and documentation must be explicitly disclosed in the Pull Request description, detailing the tools or frameworks used.
2. **Human Oversight:** The submitting contributor takes full responsibility for reviewing, testing, and understanding every line of submitted code. Undisclosed or unreviewed automated submissions may be closed without review.

---

## 🗺️ Zoo Map (Curated Progression)

This repository is organized as an exhibition cookbook. Every script is entirely self-contained, using built-in standard libraries to remain immediately runnable and easily forkable.

### 🧹 [1. Data Cleaning](./data_cleaning/)
Foundational text and data preprocessing utilities.
* **`string_cleaner.py`**: Optimised text standardisation using Pythonic list comprehensions to fix whitespace and capitalization on raw datasets.
* **`phone_sanitiser.py`**: Standalone Australian phone number sanitisation and structural block formatting with support for mobile, landlines (Perth/WA area codes), 13/1300/1800 numbers, and international prefixes.

### 🔐 [2. User Management](./user_management/)
Authentication mechanisms and secure input architecture.
* **`password_hasher.py`**: Cryptographic credential handling implementing `hashlib.pbkdf2_hmac` with unique byte salts to defend against rainbow table and brute-force attacks.
* **`email_validator.py`**: Lightweight, regex-free input validation module using fast Pythonic string parsing boundaries to catch and sanitize malformed data before database staging.

### 💾 [3. Database Basics](./database_basics/)
System durability, context safety, and resource management.
* **`connection_tester.py`**: Safe SQLite execution environments wrapping queries in strict `try-except-finally` blocks to guarantee resource closure and prevent server memory leaks.

### 💾 [4. Native GUI](./native_gui/)
Cross-platform Graphical User Interface examples using Python's standard built-in library Tkinter.
* **`basic_window_viewer.py`**: Simple window display (runs autonomously from Terminal via **`launch_window.pyw`**)

---

## Code Quality
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

## 🚀 On the Way / Open for Contribution:

### 📡 Core Communication & API Routing
- [ ] **Australian Postcode API Lookup**: Terminal utility fetching suburb/postcode data via public API. *(See [Issue #3](https://github.com/lizc-au/my-pythonic-zoo/issues/3) — Open for Contribution)*
- [ ] **HTTP Status Checker**: Lightweight URL health monitor and status code logger.

### 💾 Database Operations (CRUD)
- [ ] **SQLite CRUD Execution Script**: Transactional Create, Read, Update, and Delete module using parameterized queries.

### ⚙️ System Automation & DevOps
- [ ] **File System Cleanup & Archiver**: Directory cleanup utility that compresses old files and organizes logs by date.
- [ ] **Environment Checker**: Simple diagnostic script verifying Python version, active virtualenv, and installed system packages.

### 🧩 Algorithms & Data Structures
- [ ] **Knuth DLX Exact Cover Solver**: Production-ready implementation of Knuth's Dancing Links (Algorithm X) for matrix cover problems.
- [ ] **Graph Network & Traversal Visualizer**: Terminal or lightweight visualizer showing graph structures, shortest path (Dijkstra/A*), and node connections.

### 📈 Math & Data Visualization
- [ ] **Mathematical Formula Plotter**: Render mathematical equations and trigonometric functions (e.g., sine waves, parabolas, fractals) into visual plots using pure Python or Matplotlib.
- [ ] **Statistical Charting Utility**: Lightweight generator for statistical distributions, histograms, and data trendlines.

### 📊 Data Science & AI Foundations
- [ ] **Lightweight CSV Matrix Math**: Pure-Python numeric summarizer calculating basic statistical metrics on CSV columns without heavy dependencies.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _README.md_ | _28 August 2026_ | _lizc-au_ |
