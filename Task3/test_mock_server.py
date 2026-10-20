"""
Task 3 - Tests for the mock policy server.

These tests verify that the local test double produces
the expected responses, including an invalid PDF download.
"""

import threading
from http.server import ThreadingHTTPServer
from urllib.request import urlopen

import pytest

from Task3.mock_server import MockPolicyHandler


@pytest.fixture(name="mock_server")
def start_mock_server():
    """Start a local mock server for each test."""

    server = ThreadingHTTPServer(
        ("127.0.0.1", 0),
        MockPolicyHandler
    )

    # Port 0 automatically selects an available port.
    port = server.server_port

    thread = threading.Thread(
        target=server.serve_forever,
        daemon=True
    )

    thread.start()

    yield f"http://127.0.0.1:{port}"

    # Stop the server after the test.
    server.shutdown()
    server.server_close()
    thread.join(timeout=2)


def test_policy_index(mock_server):
    """Check that the index page contains a PDF link."""

    url = f"{mock_server}/policy/"

    with urlopen(url, timeout=5) as response:
        html = response.read().decode("utf-8")

        assert response.status == 200
        assert response.headers.get_content_type() == "text/html"
        assert "/policy/invalid-policy.pdf" in html


def test_invalid_pdf_response(mock_server):
    """Check that the PDF URL returns HTML instead of a PDF."""

    url = f"{mock_server}/policy/invalid-policy.pdf"

    with urlopen(url, timeout=5) as response:
        content = response.read()

        # The HTTP request succeeds.
        assert response.status == 200

        # The returned content type is HTML.
        assert response.headers.get_content_type() == "text/html"

        # The response does not have the PDF file signature.
        assert not content.startswith(b"%PDF")

        # Verify that our simulated error message is present.
        assert b"Document Unavailable" in content
def naive_pdf_check(url):
    """
    Simulate a scraper that only checks the URL extension
    and HTTP status when downloading a PDF.
    """

    with urlopen(url, timeout=5) as response:
        response.read()

        return (
            response.status == 200
            and url.lower().endswith(".pdf")
        )


def test_naive_scraper_false_positive(mock_server):
    """
    Demonstrate that checking only HTTP status and file
    extension can incorrectly accept HTML as a PDF.
    """

    url = f"{mock_server}/policy/invalid-policy.pdf"

    # The naive scraper incorrectly accepts this download.
    accepted = naive_pdf_check(url)

    assert accepted is True

    # Examine the actual response to demonstrate the problem.
    with urlopen(url, timeout=5) as response:
        content = response.read()
        content_type = response.headers.get_content_type()

    # The response is HTML, not a PDF.
    assert content_type == "text/html"
    assert not content.startswith(b"%PDF")
