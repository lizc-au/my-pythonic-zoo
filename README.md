# 🐍 my-pythonic-zoo

**Minimum Runtime Requirement:** Python 3.10+ (Utilises modern type-hinting features).

Housing a variety of self-contained Python scripts built with clean formatting and clear logic. - improvements welcome 🧐

---

## 🗺️ Zoo Map (Curated Progression)

This repository is organized as an exhibition cookbook. Every script is entirely self-contained, using built-in standard libraries to remain immediately runnable and easily forkable.

### 🧹 [1. Data Cleaning](./data_cleaning/)
Foundational text and data preprocessing utilities.
* **`string_cleaner.py`**: Optimised text standardisation using Pythonic list comprehensions to fix whitespace and capitalization on raw datasets.

### 🔐 [2. User Management](./user_management/)
Authentication mechanisms and secure input architecture.
* **`password_hasher.py`**: Cryptographic credential handling implementing `hashlib.pbkdf2_hmac` with unique byte salts to defend against rainbow table and brute-force attacks.
* **`email_validator.py`**: Lightweight, regex-free input validation module using fast Pythonic string parsing boundaries to catch and sanitize malformed data before database staging.


### 💾 [3. Database Basics](./database_basics/)
System durability, context safety, and resource management.
* **`connection_tester.py`**: Safe SQLite execution environments wrapping queries in strict `try-except-finally` blocks to guarantee resource closure and prevent server memory leaks.

---

## 🛠️ Work in Progress & Upcoming Exhibits

This zoo is an active, evolving cookbook. I am continuously curating and deploying new standalone use cases. 

### 🚀 On the Way / Teasers:
* **Database Operations (CRUD)**: Implementing complete Create, Read, Update, and Delete transactional structures using safe parameterized queries.
* **Core Communication & API Routing**: Setting up lightweight endpoints, request parsing, and custom status code returns.
* **System Automation & DevOps**: Writing robust Python scripts for automated file system archiving, backup routines, and local directory cleanup operations.
* **Data Science & AI Foundations**: Deploying mathematical array manipulations and lightweight data synthesis modules.

*Have an idea for a clean utility? Feature requests and optimizations are welcome via Pull Requests!*

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

## Code Quality
This repository enforces strict code hygiene, style guidelines, and bug prevention rules using the **Ruff** linter. Configuration maps are located in `pyproject.toml`.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _README.md_ | _4 August 2026_ | _lizc-au_ |
