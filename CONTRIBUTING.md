# Contributing to my-pythonic-zoo

Thank you for visiting! This repository is designed to be a reliable, highly readable cookbook of clean Python logic. 

We actively welcome contributions, optimization pull requests, and use-case feature requests.

## Pull Request & Assignment Policy

To help prevent duplicate effort, contributors are encouraged to start with an open issue or discuss a proposed change before beginning substantial work. If an issue already exists, please comment on it so we can coordinate scope and avoid multiple contributors working on the same task.

Pull Requests submitted without an assigned issue are still welcome. If the PR relates to an existing roadmap item, we may ask that it be linked to the relevant issue before review.

## Contribution Workflow

1. **Choose Your Contribution:** Check the open issues labelled `good-first-issue` or `help wanted`, or propose your own improvement. For substantial changes, opening an issue first is encouraged so the scope can be discussed before you begin.
2. **Coordinate Existing Issues:** If you are working on an existing issue, leave a quick comment before starting so we can avoid duplicate effort.
3. **Fork & Branch:** Create a branch on your fork (`git checkout -b feat/my-new-script`).
4. **Clean & Test:** Run the local quality checks described below and resolve any failures before submitting your PR.
5. **Submit a PR:** Open a Pull Request describing the change and why it is useful. If it relates to an issue, reference it (e.g., `Fixes #3`). If an autonomous agent substantially contributed to the work or submitted the PR, follow the disclosure guidance below.

### Local Development Setup

From the repository root, create a virtual environment:

```text
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```text
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```text
source .venv/bin/activate
```

Then upgrade `pip` and install the development dependency group defined in `pyproject.toml`:

```text
python -m pip install --upgrade pip
python -m pip install --group dev
```

The `dev` group includes both the runtime dependencies and the tools needed for linting, type checking, and testing.

---

### Testing Requirements
* **Tests for Code Changes:** Python code contributions should include appropriate automated test coverage. Add or update tests in the `tests/` folder when the change introduces new behaviour or modifies existing behaviour. Documentation, configuration, and other non-code changes do not require new tests. The test suite is run with `pytest`, which also discovers and runs the repository's existing `unittest`-based tests. Pull Requests with failing tests cannot be merged.

* **Core Test File:** `tests/test_zoo_core.py` provides shared regression coverage for several core repository modules. Please do not modify it without first discussing the proposed change in an issue. Changes may be appropriate when core behaviour genuinely changes, but they should be reviewed deliberately so existing protections are not weakened accidentally.

#### Local Quality Checks

Before submitting a Pull Request, activate the project's virtual environment and run the repository quality helper from the repository root:

```text
python scripts/check_quality.py
```

The helper runs the same core checks used by CI:

* Ruff linting
* Ruff formatting
* mypy type checking
* pytest

All checks should pass before the Pull Request is submitted.

#### Optional Pre-Push Hook

The repository includes an optional Git pre-push hook that runs the same quality helper automatically before each push.

With the project's virtual environment activated, enable the hook for your local clone by running:

```text
git config core.hooksPath .githooks
```

Once enabled, Git will run `python scripts/check_quality.py` before allowing a push. If any quality check fails, the push is stopped so the issue can be fixed first.

The hook is optional. GitHub Actions remains the authoritative CI check for Pull Requests.

---

### Autonomous Agent Submissions

Developers are welcome to use AI tools as part of their normal development workflow. Routine AI assistance does not require disclosure.

If an autonomous agent performs substantial implementation work or submits a Pull Request, the following additional guidelines apply:

* **Agent Disclosure:** In the interests of transparency and good open-source practice, please identify the autonomous agent or framework used in the Pull Request description.
* **Human Ownership:** Agent-generated Pull Requests are welcome, but a human contributor should review and understand the completed work and remain responsible for the submission before it is considered for merge.
* **Copyright & Provenance:** Contributors are responsible for taking reasonable care that submitted content complies with applicable licenses, does not knowingly reproduce protected third-party material without permission, and does not include proprietary data without authorization.

---

### Response Times

This project is maintained by a single maintainer. Issues and Pull Requests are welcome, but responses may take several days depending on availability. Thank you for your patience.

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _CONTRIBUTING.md_ | _2 September 2026_ | _lizc-au_ |
