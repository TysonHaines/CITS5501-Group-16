# Task 3 – Fixtures and Test Doubles

## Overview

This directory contains a local HTTP test double developed for
CITS5501 Project Phase 2, Task 3.

The test double simulates a policy website that returns HTML content
when a client attempts to download a PDF document.

The purpose is to demonstrate how a scraper can incorrectly accept
an invalid document when it only checks the HTTP status code and
file extension.

## Files

- `mock_server.py` – Simulates the policy website using Python's
  built-in HTTP server.
- `test_mock_server.py` – Contains automated pytest tests.
- `README.md` – Instructions for running the demonstration.

## Requirements

- Python 3.10 or later
- pytest
- uv (recommended for dependency management)

## Setup

Run these commands from the repository root:

```bash
uv venv .venv
source .venv/bin/activate
uv pip install pytest
```

## Running the Mock Server

From the repository root, run:

```bash
python task3/mock_server.py
```

The server starts at:

http://localhost:8000

The simulated policy index is available at:

http://localhost:8000/policy/

The deliberately invalid PDF response is available at:

http://localhost:8000/policy/invalid-policy.pdf

To inspect the invalid response, open another terminal and run:

```bash
curl -i http://localhost:8000/policy/invalid-policy.pdf
```

The server returns HTTP 200 with `Content-Type: text/html`,
even though the requested URL ends in `.pdf`.

Press Ctrl+C to stop the server.

## Running Automated Tests

From the repository root, run:

```bash
python -m pytest -v task3/test_mock_server.py
```

The tests automatically start and stop their own local HTTP servers.

No external network connection is required for the tests.

## Test Cases

### Test 1: Policy Index

Verifies that the simulated policy index returns HTTP 200,
declares HTML content, and contains a PDF download link.

### Test 2: Invalid PDF Response

Verifies that requesting the PDF URL returns HTTP 200 but provides
HTML content rather than a valid PDF signature.

### Test 3: Naive Scraper False Positive

Demonstrates how a simplified scraper incorrectly accepts the
invalid response when it only checks the HTTP status code
and `.pdf` extension.

The test passes when this incorrect acceptance is reproduced.

## Expected Results

All three tests should pass.

This confirms that the test double consistently reproduces
the intended failure scenario.

These tests demonstrate a potential scraper vulnerability.
They do not independently verify the behaviour of the group's
Task 1 prototype.

## Why Use a Local Test Double?

The actual policy website cannot reliably be made to return
HTML instead of a valid PDF on demand.

Using a local test double provides a controlled, repeatable
environment without modifying the real website or depending
on external network conditions.
