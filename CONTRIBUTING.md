# Contributing to BPREI

> Thank you for your interest in contributing to the **BylickiLabs Python Reverse Engineering Inspector (BPREI)**.

<br>

---

<br>

### Principles

> Contributions should respect the existing BPREI architecture and preserve the application's focus as a static analysis tool.
  - In particular:

* Analyzed target code must not be imported or executed.
* New analysis functionality should use static inspection wherever possible.
* Changes must not cause the German and English localization sets to diverge.
* New dependencies should be technically justified and kept to the necessary minimum.
* Existing export formats and stored data structures should only receive incompatible changes with clear justification.
* Security relevant changes should be documented and tested with particular care.

### Development Environment

```yarn
Python 3.10 or newer is recommended.
```

```powershell
py -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

> The existing `start.bat` can alternatively be used for the normal application launch.

### Branches

> Use a dedicated branch for each change.
  - Examples:

```text
feature/dependency-graph
fix/export-encoding
docs/security-policy
test/project-analyzer
```

### Code Quality

> [!NOTE]
> Before opening a pull request, at minimum the following checks should pass:


```powershell
python -m compileall -q main.py src
ruff check .
python -m pytest
```

> [!NOTE]
> If no suitable tests exist for new functionality, tests should be added together with the change whenever possible.

### Localization

> The keys under `TRANSLATIONS["de"]` and `TRANSLATIONS["en"]` must remain identical.
  - New user visible interface text should not be hardcoded directly in UI code when it can be represented through the centralized localization system.

### Pull Requests

> A pull request should:

* have a clear title
* explain the purpose of the change
* list the most important technical changes
* document performed tests
* identify possible impact or compatibility changes
* include screenshots when the user interface changes visibly
* contain no credentials, tokens, secrets, or personal data

### Issues

> Before opening a new issue, check whether a similar report or request already exists.
  - Use the provided GitHub issue templates for bug reports and feature requests.