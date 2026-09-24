# Contributing to my-pythonic-zoo

Thank you for visiting! This repository is designed to be a reliable, highly readable collection of Python learning exhibits.

We actively welcome contributions, optimization pull requests, and use-case feature requests.

## Pull Request & Assignment Policy

Before starting a substantial change, create an [issue](https://github.com/lizc-au/my-pythonic-zoo/issues) or comment on a relevant existing one. This helps us agree on scope and avoid duplicate work.

Pull Requests without an assigned issue are welcome. If a PR relates to an existing issue, link it in the description.

## Contribution Workflow

1. **Choose a contribution:** Browse the [open issues](https://github.com/lizc-au/my-pythonic-zoo/issues) or propose your own improvement. For substantial work, coordinate on an issue first.
2. **Fork and branch:** Create a branch on your fork for that issue or focused change (`git checkout -b feat/my-new-script`). Use a separate branch for a separate issue so each Pull Request stays easy to review.
3. **Check your work:** Run the local quality checks below and resolve failures before submitting a Pull Request.
4. **Submit a Pull Request:** Describe the change and link any related issue. Use a closing keyword such as `Fixes #123` only when the PR fully resolves that issue; follow the agent disclosure guidance below when applicable.

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

### Documentation and Docstring Style

Examples in this repository are intended to teach through both their code and their documentation. Public modules, classes, and methods should therefore include useful docstrings that explain intent, responsibilities, or design decisions where these are not obvious from the code alone.

Docstrings use reStructuredText (reST) conventions. Enclose Python identifiers and short code expressions in double backticks, for example ``Animal``, ``speak()``, and ``AnimalFactory.create()``.

Prefer docstrings that explain **why** an abstraction or design choice exists, its important benefits or trade-offs, and when an alternative may be more appropriate. Avoid docstrings that merely repeat information already clear from the identifier or signature.

README files use Markdown rather than reStructuredText. Keep each prose paragraph to at most two sentences; put longer explanations in a Markdown table or a `<details>` section.

Use real folder and script links and commands in README examples. Update the relevant category guide when adding or changing an exhibit.

---

### Testing Requirements
* **Tests for Code Changes:** Python code contributions should include appropriate automated test coverage. Add or update tests in the `tests/` folder when the change introduces new behaviour or modifies existing behaviour. Documentation, configuration, and other non-code changes do not require new tests. The test suite is run with `pytest`, which also discovers and runs the repository's existing `unittest`-based tests. Pull Requests with failing tests cannot be merged.

* **Test Organisation:** Keep tests focused and easy to locate. When adding or changing a repository example, place its tests in a correspondingly named test module under `tests/`.

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

[Return to the zoo map](README.md)

---

_Last updated: 24 September 2026 · Maintained by [@lizc-au](https://github.com/lizc-au)_
