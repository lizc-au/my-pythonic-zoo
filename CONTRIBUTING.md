# Contributing to my-pythonic-zoo

Thank you for visiting! This repository is designed to be a reliable, highly readable cookbook of clean Python logic. 

We actively welcome contributions, optimization pull requests, and use-case feature requests.

## Pull Request & Assignment Policy

To prevent duplicate effort and protect maintainer review time, **we do not accept unsolicited or unassigned Pull Requests.** Any PR submitted without an assigned issue will be automatically closed by our GitHub Action automation.

### How to Contribute

1. **Find an area to improve:** Spot a bug, an optimization opportunity, or a documentation typo.
2. **Open or find an Issue:** 
   * *For existing issues:* Open the issue and check if it is free.
   * *For new bugs:* Open a **Bug Report Issue** describing the problem and how to reproduce it.
   * *For new features:* Open a **Feature Request Issue** to discuss your idea first.
3. **Request assignment:** Leave a comment on the issue explicitly asking to be assigned to the task.
4. **Wait for approval:** Do not write code until a maintainer officially assigns the issue to you.
5. **Lint your code**: Before pushing your branch, run `pip install ruff` and execute `ruff check .` in your terminal to ensure your code passes our strict Pythonic guidelines.
6. **Submit your PR:** Once assigned, submit your Pull Request for review following our AI and attribution rules if applicable.

### 🧪 Testing Requirements
* **Comprehensive `unittest` Coverage Required**: You must always include an accompanying test module inside the `tests/` folder that covers your submitted code, unless explicitly instructed otherwise. Pull Requests with failing tests cannot be merged.
* **Core File Restrictions**: Do **not** edit or add tests to `test_zoo_core.py`. Any unauthorized changes to this core file will cause your Pull Request to be rejected unless explicitly discussed and approved in your issue beforehand.

### AI & Automated Agent Submissions
We welcome AI-assisted contributions, provided they maintain transparency and human oversight:

* **Full Disclosure:** State clearly in your PR description if code or documentation was generated using an LLM or autonomous agent, and specify the tool or framework used (e.g., as outlined in [GitHub's guidelines on reviewing AI-generated code](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code)).
* **Human Ownership:** You are responsible for reviewing, testing, and understanding all submitted code. Undisclosed or automated PRs submitted without human verification will be closed.
* **Copyright & Provenance:** Ensure all submitted AI code complies with applicable open-source licenses and does not infringe on third-party intellectual property or proprietary datasets.

#### Recommended Git Commit Trailers
When committing AI-assisted code, append standard footers to the end of your commit message as shown in the examples below:

**Option A: GitHub Co-author (Appears visually on GitHub UI)**
```text
feat: add regex-free email validator

Co-authored-by: AI Agent <agent@users.noreply.github.com>
```
*(See [GitHub's multi-author commit docs](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors) for details).*

**Option B: Explicit Metadata (Open-source standard)**
```text
refactor: optimize string cleaning function

Generated-by: Claude 3.5 Sonnet
Assisted-by: SWE-agent v1.0
```

> **Note:** Leave a blank line between the commit message body and the trailer lines so Git parses them correctly.

*All reviews and interactions are conducted asynchronously through standard GitHub Pull Requests.*

---

| File | Last Updated | Maintainer |
| :--- | :---: | ---: |
| _CONTRIBUTING.md_ | _5 August 2026_ | _lizc-au_ |