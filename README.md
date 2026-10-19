# CITS5501-Group-16

Group project for CITS5501/CITS3501 (Group 16, "404 Brain Not Found"). The project builds a command-line program that scrapes the UWA Policy Library and retrieves policy documents in a range of formats, including PDF and Word. Phase 2 delivers a minimal scraper prototype and a test design for a production version of it.

## Contents

| Folder | What it contains | Instructions |
|---|---|---|
| `Task1/` | Task 1 minimal prototype: `scraper.py` finds policy-document links on the index page, downloads five distinct documents and prints their metadata. | [`Task1/README.md`](Task1/README.md) |
| `Task3/` | Task 3 test double: a local mock server that returns HTML for a `.pdf` link, with pytest tests. | [`Task3/README.md`](Task3/README.md) |
| `phase2-report/` | Phase 2 report (Tasks 1–4) in Markdown and PDF, plus the Makefile used to build the PDF. | — |
| `phase1-sample-code/` | Phase 1 report and the sample Makefile it was built with. | — |

## Quick start

Requires Python 3.10 or later; [uv](https://docs.astral.sh/uv/) is recommended.

Run the prototype against the live policy site (from the `Task1/` directory):

```bash
cd Task1
uv run --with-requirements requirements.txt scraper.py
```

Run the Task 3 tests (from the repository root):

```bash
uv run --with-requirements Task3/requirements.txt python -m pytest -v Task3/test_mock_server.py
```

See the README in each folder for other ways to run the code, what the output means, and how to run the prototype against the Task 3 mock server.
