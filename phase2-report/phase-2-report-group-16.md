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

# 5. Task 3 – Fixtures and Test Doubles

## 5.1. Fixtures as a Source of Truth

Testing a web scraper against a live website can be unreliable because the website's content and behaviour may change over time. To make our tests more repeatable, we can use fixtures containing predefined inputs and expected results.

For HTML parsing, we would maintain sample policy index pages containing a known set of document links. These would allow us to check whether the scraper identifies the correct documents. We could also create modified versions with missing elements, incomplete HTML or changes to the page structure to test how the scraper handles unexpected content.

Similarly, valid and deliberately corrupted PDF and Word documents could be used to check whether downloads are correctly validated. The expected file formats and results would be established beforehand, allowing us to determine whether the scraper is producing correct output rather than simply completing a request.

A locally hosted HTTP server is also useful because it allows us to control the status codes, content types and response bodies returned to the scraper. This makes it possible to reproduce failures consistently without relying on the live website.

## 5.2. Rate-Limiting Observations

We used `curl` to investigate whether the target policy website applies request limits.

**Method:** On 15 October 2026, we first accessed the policy index page, which returned HTTP 200. We then made six download requests for the same PDF document, with a one-second delay between requests. For each attempt, we recorded the HTTP status, content type, downloaded size and response time.

**Results:**

| Request | HTTP Status | Content-Type    | Size (bytes) | Response Time (s) |
| ------- | ----------- | --------------- | ------------ | ----------------- |
| 1       | 200         | application/pdf | 301,201      | 0.554             |
| 2       | 200         | application/pdf | 301,201      | 0.538             |
| 3       | 200         | application/pdf | 301,201      | 0.599             |
| 4       | 200         | application/pdf | 301,201      | 0.505             |
| 5       | 200         | application/pdf | 301,201      | 0.517             |
| 6       | 200         | application/pdf | 301,201      | 0.528             |

All six requests returned HTTP 200 with identical download sizes. Response times remained between approximately 0.50 and 0.60 seconds, and no redirects occurred.

**Conclusion:** We did not observe any evidence of rate limiting during these six attempts. However, this does not necessarily mean the website has no restrictions, as limits might only apply when requests are made more frequently or in larger numbers.

Another group member reported receiving HTTP 429 (Too Many Requests) after making more than six requests. This suggests that the website applies rate limits under certain conditions. However, the exact threshold and time window could not be established from our observations.

For a larger test suite, we would avoid repeatedly accessing the live website. Instead, we could use local fixtures and simulated server responses to test error handling, retry behaviour and rate limiting without generating unnecessary traffic.

## 5.3. Using Test Doubles to Simulate Failures

Test doubles allow us to reproduce network failures that may be difficult to trigger consistently against the actual policy website.

In Python, `unittest.mock` or pytest's `monkeypatch` fixture can replace HTTP operations with controlled behaviour. For example, a mocked request could raise a timeout or connection exception, allowing us to check whether the scraper reports the error and handles retries appropriately.

A local HTTP server could also simulate network problems more realistically. Adding a delay before responding would allow us to test slow responses and timeouts. An interrupted download could be reproduced by closing the connection before the complete response body has been sent. Similarly, returning HTTP 404, 429 or 503 would allow us to examine how the scraper handles unavailable documents, request limits and server errors.

These approaches make testing more predictable because the same conditions can be reproduced whenever needed. They also allow us to test different failure scenarios without depending on the availability or behaviour of the live website.

## 5.4. Implemented Failure Scenario

**Scenario:** Our implementation demonstrates **T008 (S5 – HTML returned for a PDF URL)** from Task 2.

We created a local HTTP server using Python's `http.server` module. The server simulates a policy website containing a link to `/policy/invalid-policy.pdf`.

Although the requested URL ends in `.pdf`, the server deliberately returns HTTP 200 with `Content-Type: text/html`. The response contains an HTML error message rather than a PDF document.

**Why this scenario:** We chose this scenario because a scraper that checks only the HTTP status and file extension may incorrectly accept an invalid document. According to T008, a fully functional scraper should reject the response and report a content or format mismatch.

**Files:**

* `task3/mock_server.py` – Implements the local HTTP server and invalid PDF response.
* `task3/test_mock_server.py` – Contains three automated tests using pytest.
* `task3/README.md` – Provides instructions for running the server and reproducing the demonstration.

**How to run:**

From the repository root, activate the Python environment and execute:

```bash
python -m pytest -v task3/test_mock_server.py
```

To run the mock server manually:

```bash
python task3/mock_server.py
```

The mock policy index is then available at `http://127.0.0.1:8000/policy/`.

**Test results:** All three automated tests passed locally using Python 3.10.12 and pytest 9.1.1 on WSL Ubuntu 22.04.

The tests verified that the index contained the expected PDF link, that requesting the document returned HTML instead of PDF content, and that a simplified scraper incorrectly accepted the response.

We also tested the group's actual Task 1 prototype against the mock server. The scraper discovered the document link and downloaded the response. However, despite receiving 234 bytes of HTML with the content type `text/html`, it reported:

```text
HTTP status and reason:
200 OK

Content-Type:
text/html

Downloaded Size:
234 (0.00 MB)

Outcome: SUCCESS

Downloads succeeded: 1 of 1 attempted
Requests made: 2 (limit 20)
```

This demonstrated that the prototype currently determines download success using the HTTP status without validating the actual document format.

Under T008's acceptance criteria, this behaviour would be considered a failure for a production scraper. However, it is a limitation of the current prototype rather than necessarily a violation of Task 1 requirements, which focus on basic document discovery, downloading and metadata reporting.

Reproducing this scenario against the live website would be difficult because we cannot control its server responses. Using a local test double allowed us to reproduce the issue consistently without interfering with the actual website.

## 5.5. Limitations

Our implementation focuses on one specific failure scenario: a PDF URL returning HTML content despite a successful HTTP response.

Although the three automated tests confirm that the test double produces the intended behaviour, they do not provide comprehensive testing of the scraper. The integration test demonstrates the prototype's response to this particular scenario, but does not establish how it would behave under other network failures.

The current test double does not simulate connection timeouts, interrupted downloads, or repeated HTTP 429 and 503 responses. These could be added in future tests to evaluate retry behaviour and error handling.

Another limitation is that our demonstration focuses on incorrect content types and file signatures rather than full document parsing. A more complete test suite would also include corrupted PDFs that have valid-looking headers but cannot be opened by a PDF reader, as described in T009.

Despite these limitations, the implemented fixture provides a repeatable demonstration of an important weakness in document validation and can be reused when improving the scraper.

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
