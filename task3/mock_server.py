"""
Task 3 - Fixtures and Test Doubles

A local HTTP server that simulates an invalid PDF download.

The server returns HTML content with HTTP status 200
when a client requests a file ending in .pdf.

This allows us to test how a policy scraper handles
unexpected document content.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer


class MockPolicyHandler(BaseHTTPRequestHandler):
    """Handle requests to the simulated policy website."""

    def do_GET(self):  # pylint: disable=invalid-name
        """Return a policy index or an invalid PDF response."""

        if self.path in ("/", "/policy/"):

            # Simulated policy index containing a PDF link.
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Policy Library</title>
            </head>
            <body>
                <h1>University Policy Library</h1>

                <a href="/policy/invalid-policy.pdf">
                    Download Policy Document
                </a>

            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            self.wfile.write(html.encode("utf-8"))

        elif self.path == "/policy/invalid-policy.pdf":

            # Deliberately return HTML instead of a valid PDF.
            html = """
            <!DOCTYPE html>
            <html>
            <body>
                <h1>Document Unavailable</h1>
                <p>The requested policy document is unavailable.</p>
            </body>
            </html>
            """

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            self.wfile.write(html.encode("utf-8"))

        else:

            self.send_response(404)
            self.end_headers()


def main():
    """Start the local mock policy server."""

    server_address = ("127.0.0.1", 8000)

    server = HTTPServer(server_address, MockPolicyHandler)

    print("Mock policy server running on http://localhost:8000")
    print("Press Ctrl+C to stop the server.")

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nStopping mock server.")

    finally:
        server.server_close()


if __name__ == "__main__":
    main()
