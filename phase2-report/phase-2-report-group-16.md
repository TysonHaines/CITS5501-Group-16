---
title: "CITS5501 Project Phase 2 -- Group 16"
author: "Tyson Haines (23779585), Akshay Raghuwanshi (24991278), Khushi Sesetti (23823678), Kevin Tan (23789621), Celine Xu (24714078)"
date: October 2026
mainfont: "New Computer Modern"
---

<!--
HOW TO USE THIS TEMPLATE

- Text inside HTML comments like this one is guidance. Pandoc drops it from
  the PDF, but delete it anyway before submitting.
- Lines starting with "TODO:" are placeholders. Replace every one of them;
  `grep -n TODO phase-2-report-group-16.md` should return nothing at submission.
- The section headings follow the four task drafts on our branches. Check every
  heading against the Phase 2 brief and add the brief's own requirement numbers
  (e.g. "brief 3.2.3") where a section answers a specific requirement.
- Numbering conventions, used everywhere in this report:
    A001, A002, ...  assumptions (required format, Phase 1 brief 2.4)
    L001, L002, ...  limitations of the Task 1 prototype
    T001, T002, ...  Task 2 test cases
    S1-S5            the five failure scenarios listed in the brief for Task 2
    X001, X002, ...  Task 4 adversarial tests
- Build the PDF with `make` in this directory (same pandoc + typst toolchain as Phase 1).
-->

# 1. Introduction

TODO: Two or three sentences on what Phase 2 asks for (a minimal scraper prototype, a test-suite design, fixtures and test doubles, and adversarial inputs) and how this report is organised.

Our group repository is hosted at: [github.com/TysonHaines/CITS5501-Group-16](https://github.com/TysonHaines/CITS5501-Group-16).

TODO: State the exact commit or tag the submission corresponds to (e.g. `main` at commit `abc1234`), so markers can reproduce what they read.

# 2. Team members

| Name                | Student number  | GitHub username   |
|---------------------|-----------------|-------------------|
| Tyson Haines        | 23779585        | TysonHaines       |
| Akshay Raghuwanshi  | 24991278        | AkshayRaghuwanshi |
| Khushi Sesetti      | 23823678        | khushisesetti     |
| Kevin Tan           | 23789621        | phattydumpling    |
| Celine Xu           | 24714078        | 1031Celinela      |

Group name: 404 Brain Not Found (Group 16).

## 2.1. Task allocation

<!-- Keep this honest and specific; it supports the Group Contribution Factor and
     shows the workflow promised in Phase 1 (feature branches + reviewed PRs). -->

| Task | Lead | Contributors / reviewers | Branch(es) / PR(s) |
|------|------|--------------------------|--------------------|
| Task 1 – Prototype | TODO | TODO | `task1/prototype` |
| Task 2 – Test suite design | TODO | TODO | `feature/task2-test-design` |
| Task 3 – Fixtures and test doubles | TODO | TODO | `feature/task3-fixtures-test-doubles` |
| Task 4 – Adversarial inputs | TODO | TODO | TODO |
| Report integration and editing | TODO | TODO | `make-report` |

# 3. Task 1 – Prototype

## 3.1. Purpose and implementation

<!-- Describe what the prototype does, in the order it does it: fetch index ->
     extract links -> filter -> select N distinct documents -> fetch each ->
     print metadata. Say explicitly what it does NOT do (e.g. no saving to disk,
     no crawling beyond the index), citing the brief requirement for each. -->

TODO: What the prototype does, step by step.

TODO: How links are identified as policy documents, and how the 3–5 "distinct" documents are chosen (what "distinct" means in our implementation).

TODO: The metadata printed for each download, as a list:

- URL of the policy document
- HTTP status and reason
- Declared `Content-Type`
- Downloaded size (actual bytes received, and the declared `Content-Length` if present)
- First bytes of the response body
- Outcome (`SUCCESS` / `FAILED`) and what each outcome means

## 3.2. Request controls

<!-- The fetch() wrapper: User-Agent, timeout, delay, request cap. Be precise
     about what each control does and does not guarantee (e.g. the timeout is
     per connect/read, not a total deadline; redirects are not counted). -->

TODO: The controls applied by `fetch()` and their values.

TODO: Requests made in a normal run (index + N documents) versus the cap.

## 3.3. Running the prototype

TODO: The exact command(s) to run it on the marking environment (Ubuntu 22.04, `uv`), and where the README with full instructions lives (`phase2/my-webscraper/README.md`).

```bash
# TODO: replace with the real command
uv run --with-requirements requirements.txt scraper.py
```

## 3.4. Sample output

<!-- One real, trimmed run against the live site, plus (ideally) one run that
     shows a failure being reported, e.g. against the Task 3 mock server.
     Show evidence; don't just describe it. -->

TODO: Paste a trimmed successful run.

```text
TODO
```

TODO: Paste a run that shows a failure being reported (e.g. HTTP 404 or wrong content type).

```text
TODO
```

## 3.5. Assumptions

<!-- Use the A001 format required by the Phase 1 brief (2.4): number, statement,
     why it is reasonable. Every assumption here must also appear in the
     register in Section 7. -->

**A001 – TODO: short name.**
TODO: The assumption, and why it is reasonable.

**A002 – TODO: short name.**
TODO: The assumption, and why it is reasonable.

## 3.6. Limitations

<!-- What the prototype knowingly does not handle. For each, say what the
     consequence is and, where relevant, which Task 2 or Task 4 test would
     expose it (e.g. "exposed by T008, X001"). -->

**L001 – TODO: short name.**
TODO: Limitation, consequence, and which test(s) would expose it.

**L002 – TODO: short name.**
TODO: Limitation, consequence, and which test(s) would expose it.

# 4. Task 2 – Test suite design

## 4.1. Scope and expected behaviour

<!-- State that the tests target a fully functional scraper, not the Task 1
     prototype, and define what "correct" means (e.g. reporting a failure can be
     correct; a 200 response alone is not a valid document). -->

TODO: What the test suite is designed for, and what counts as correct behaviour.

## 4.2. Test-design assumptions and acceptance policy

<!-- Explicit, numbered policy the tests assert against, e.g. retry counts,
     which statuses are retried, request cap. Record any of these as A00x in
     Section 7. -->

TODO: The acceptance policy (timeouts, retry limits, which HTTP errors are retried, request cap), each linked to an assumption number.

## 4.3. Expected behaviour per scenario

<!-- One short paragraph per scenario from the brief. Use the brief's own
     scenario names. -->

1. **S1 – TODO: scenario name:** TODO: reasonable response.
2. **S2 – TODO:** TODO.
3. **S3 – TODO:** TODO.
4. **S4 – TODO:** TODO.
5. **S5 – TODO:** TODO.

## 4.4. Test cases

<!-- Arrange-Act-Assert. Each Assert must state concrete pass AND fail evidence
     (an oracle), not "behaves correctly". -->

| Test ID / scenario | Arrange (fixture or environment) | Act | Assert (pass/fail evidence) |
|---|---|---|---|
| **T001 – S1: TODO** | TODO | TODO | **Pass:** TODO. **Fail:** TODO. |
| **T002 – S2: TODO** | TODO | TODO | **Pass:** TODO. **Fail:** TODO. |
| **T003 – S3: TODO** | TODO | TODO | **Pass:** TODO. **Fail:** TODO. |

## 4.5. Coverage summary

| Scenario | Test cases | Failure mechanisms distinguished |
|---|---|---|
| S1 | TODO | TODO |
| S2 | TODO | TODO |
| S3 | TODO | TODO |
| S4 | TODO | TODO |
| S5 | TODO | TODO |

## 4.6. Rationale and limitations

TODO: Why these cases were chosen, what the oracles are, and what the design does not cover. State clearly that these are proposed tests, not executed results.

# 5. Task 3 – Fixtures and test doubles

## 5.1. Fixtures as a source of truth

TODO: Which fixtures we would maintain (sample index pages, valid and corrupt documents, a local HTTP server) and what each one makes testable.

## 5.2. Rate-limiting observations

<!-- Report this like a small experiment: method, results, conclusion, caveats.
     Stay within the brief's politeness limits and say that you did. -->

**Method.** TODO: Tool used, number of requests, delay between them, date and time of the test.

**Results.**

| Request | HTTP status | Content-Type | Size (bytes) | Response time (s) |
|---|---|---|---|---|
| 1 | TODO | TODO | TODO | TODO |
| … | | | | |

**Conclusion.** TODO: What the evidence does and does not show about rate limiting.

## 5.3. Using test doubles to simulate failures

TODO: Which test doubles we would use (`unittest.mock`, pytest `monkeypatch`, local server) and which failure each one reproduces (timeouts, dropped connections, 404/429/503, slow responses).

## 5.4. Implemented failure scenario

<!-- Describe the scenario, why it was chosen, the files, how to run it, and
     the observed result, including Python and pytest versions. Link it to the
     Task 2 test it implements (e.g. "implements T008"). -->

**Scenario.** TODO: What the double does, and which Task 2 test case it corresponds to.

**Why this scenario.** TODO.

**Files.**

- `task3/mock_server.py` – TODO
- `task3/test_mock_server.py` – TODO

**How to run.**

```bash
# TODO: exact commands from the repository root
uv run --with pytest pytest task3/
```

**Result.** TODO: Tests run, pass/fail, environment (Python version, pytest version, OS).

## 5.5. Limitations

TODO: What this double does not exercise (e.g. it tests a simplified client, not our prototype), and what the next double would be.

# 6. Task 4 – Adversarial inputs

## 6.1. Approach

<!-- Tie each adversarial input back to an assumption we made in Phase 1
     (Q5, Q6, Q8) or in this report (A00x). State that inputs are served from
     controlled local fixtures, never by disrupting the live site, and that these
     are proposed tests, not observed results. -->

TODO: How the adversarial inputs were derived from our Phase 1 report and the assumptions in this report, and how they would be run safely.

## 6.2. Adversarial test cases

| ID | Assumption challenged (source) | Input artifact or environment | Failure, and how it would be detected |
|---|---|---|---|
| **X001** | TODO (Phase 1 Q8 / A00x) | TODO | **Failure:** TODO. **Detection:** TODO. |
| **X002** | TODO | TODO | **Failure:** TODO. **Detection:** TODO. |
| **X003** | TODO | TODO | **Failure:** TODO. **Detection:** TODO. |

## 6.3. Relationship to Tasks 1–3

TODO: Which X tests the current prototype would fail (link to L00x), and which overlap with or extend Task 2 tests (link to T00x).

# 7. Assumptions register

<!-- Every A00x used anywhere in this report, in one place. -->

| ID | Assumption | Why it is reasonable | Used in |
|---|---|---|---|
| A001 | TODO | TODO | Section 3.5 |
| A002 | TODO | TODO | TODO |

# 8. References

<!-- Optional. Phase 1 brief recommends AMS short alpha-numeric style. Include
     the brief, library docs, and any published source whose code we used (the
     brief requires crediting it). Delete this section if unused. -->

TODO: References, or delete this section.
