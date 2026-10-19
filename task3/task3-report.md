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
