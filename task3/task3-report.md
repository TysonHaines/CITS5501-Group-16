## 3. Task 3 – Fixtures and Test Doubles

### 3.1 Fixtures as a Source of Truth

Testing a web scraper against a live website can be difficult because the website's content and behaviour may change over time. To make our tests more reliable, we can use fixtures containing predefined inputs and expected outputs.

For HTML parsing, we could maintain sample policy index pages with a known set of document links. These would allow us to check whether the scraper identifies the correct documents. We could also create modified versions of these pages, such as ones with missing HTML elements or changes to the page structure, to test how the scraper handles unexpected content.

Similarly, sample policy documents in PDF and Word formats could be used to verify downloaded files. Having both valid and deliberately corrupted documents would help us check whether the scraper correctly identifies unsuccessful downloads rather than accepting every response as a valid document.

A locally hosted HTTP server is another useful fixture. It allows us to control the responses returned to the scraper, including HTTP status codes, content types and response bodies. Since the inputs are predefined, we can compare the scraper's behaviour against known expectations without relying on the live website.

### 3.2 Rate Limiting Observations

We used `curl` to investigate whether the target policy website applies request limits. We first accessed the policy index page, which returned HTTP 200, confirming that the website was accessible.

We then made six download requests for the same PDF document, with a one-second delay between requests. Each request returned HTTP 200 with a content type of `application/pdf`. All six responses contained 301,201 bytes, and the response times ranged from approximately 0.50 to 0.60 seconds.

We did not encounter any HTTP 429 (Too Many Requests) or HTTP 503 (Service Unavailable) responses during these attempts. Based on these observations, there was no evidence of rate limiting under the conditions we tested. However, this does not necessarily mean the website has no request limits, as restrictions might only apply when requests are made more frequently or in larger numbers.

For a larger test suite, we would avoid repeatedly sending requests to the live website. Instead, we could use locally stored HTML and document fixtures alongside a mock server to reproduce different responses. This would allow us to test error handling and retry behaviour without depending on the website's availability or risking unnecessary requests to the server.

### 3.3 Using Test Doubles to Simulate Failures

Test doubles are useful for reproducing network-related failures that may not occur consistently when testing against the actual website.

In Python, we can use `unittest.mock` or pytest's `monkeypatch` fixture to replace network operations with controlled behaviour. For example, a mocked request could raise a timeout or connection exception to check whether the scraper handles the error appropriately.

A local HTTP server can also be used to simulate these situations more realistically. Introducing a delay before sending a response would allow us to test slow connections and timeouts. An interrupted download could be simulated by closing the connection before the complete response has been sent. Similarly, returning HTTP 404, 429 or 503 would allow us to examine how the scraper responds to unsuccessful requests.

These approaches are useful because the same failure can be reproduced whenever required. This makes it easier to investigate problems and confirm whether changes to the scraper have improved its behaviour.

### 3.4 Implemented Failure Scenario

For our implementation, we created a local HTTP server using Python's `http.server` module. The server simulates a policy website containing a link to a PDF document.

The failure scenario occurs when the client requests `/policy/invalid-policy.pdf`. Although the URL ends in `.pdf`, the server deliberately returns HTTP 200 with a content type of `text/html`. The response contains an HTML message indicating that the document is unavailable, rather than an actual PDF.

This scenario corresponds to **T008 (S5 – HTML returned for a PDF URL)** from Task 2. According to the test's acceptance criteria, a fully functional scraper should reject the response and report a content or format mismatch instead of accepting it as a valid PDF.

Our implementation consists of two Python files: `mock_server.py`, which provides the simulated website, and `test_mock_server.py`, which contains three automated tests using pytest. These tests verify the index page, confirm that the PDF URL returns HTML, and demonstrate how a simplified scraper can incorrectly accept the response. All three tests passed locally.

We also tested the group's Task 1 prototype against the mock server. The scraper identified the PDF link and downloaded the response. However, despite receiving 234 bytes of HTML with the content type `text/html`, it reported `Outcome: SUCCESS`. This demonstrated that the prototype currently relies on the HTTP status to determine download success without validating the document format.

Under the acceptance criteria defined in T008, this behaviour would be considered a failure. However, it is a limitation of the current prototype rather than necessarily a violation of Task 1 requirements, since Task 1 focuses on basic document discovery, downloading and metadata reporting.

Reproducing this scenario against the live website would be difficult because we cannot control the server's responses. Using a local test double allowed us to reproduce the issue consistently without interfering with the actual website.

Overall, the demonstration highlights why a successful HTTP response does not necessarily mean that the downloaded document is valid.
