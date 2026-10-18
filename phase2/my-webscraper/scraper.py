#!/usr/bin/env python3
"""
CITS5501 Project Phase 2 -- starter code for the Task 1 minimal prototype.

What this starter already does:

- reads an optional start URL from the command line (defaults to the
  policy index page),
- fetches that page via `fetch()`, which sets a timeout and a User-Agent,
  waits briefly between requests, and stops the program if it would exceed
  MAX_REQUESTS,
- extracts every <a href="..."> link on the page and makes it absolute,
- prints the links it found.

What you need to write (look for "TODO"):

- `is_policy_link()`: decide which links look like policy documents,
- `describe_download()`: download one document and print its metadata,
- the loop at the end of `main()` that picks 3-5 distinct documents
  and calls `describe_download()` on each.

Run with:

    uv run --with-requirements requirements.txt scraper.py
    uv run --with-requirements requirements.txt scraper.py http://localhost:3000/

(See README.md for other ways to run it.)
"""

import argparse
import sys
import time
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup


START_URL = "https://uwa-policy.cits5501.arranstewart.io/policy/"

# Politeness and safety limits. Please don't raise these when running
# against the live site.
MAX_REQUESTS = 20       # total requests per run (index page + downloads)
TIMEOUT_SECONDS = 10    # per request; `requests` has NO timeout by default
DELAY_SECONDS = 1.0     # pause between consecutive requests

USER_AGENT = "CITS5501-Group16-scraper/0.1 (university course project)"

FILE_EXTENSIONS = ('.pdf', '.doc', '.docx', '.pptx')
INITIAL_BYTES_SIZE = 16
CHUNK_SIZE = 8192
MAX_DOCS = 5

class RequestLimitExceeded(Exception):
    """Raised when a run tries to make more than MAX_REQUESTS requests."""

# keep track of how many request we have made.
_request_count = 0


def fetch(session, url, **kwargs):
    """
    Make a GET request, enforcing the request cap, a timeout and a delay.

    Use this for every request your prototype makes, rather than calling
    `session.get()` directly. Any extra keyword arguments (e.g. `stream=True`)
    are passed through to `session.get()`.

    Returns a `requests.Response`. Note that this does NOT raise an exception
    for 4xx/5xx status codes -- check `response.status_code` yourself.
    """

    global _request_count
    if _request_count >= MAX_REQUESTS:
        raise RequestLimitExceeded(
            f"request limit of {MAX_REQUESTS} reached; not fetching {url}"
        )
    if _request_count > 0:
        time.sleep(DELAY_SECONDS)
    _request_count += 1

    kwargs.setdefault("timeout", TIMEOUT_SECONDS)
    return session.get(url, **kwargs)


def extract_links(html, base_url):
    """
    Return a list of absolute URLs for every <a href="..."> in `html`,
    in the order they appear. Relative links are resolved against `base_url`.
    Duplicates are NOT removed.
    """
    soup = BeautifulSoup(html, "html.parser")
    return [urljoin(base_url, a["href"]) for a in soup.find_all("a", href=True)]


def is_policy_link(url):
    """
    Return True if `url` looks like it leads to a downloadable policy
    document (e.g. a PDF or office file), otherwise False.

    TODO: implement this. Filtering by file extension is acceptable for
    the prototype -- but note its limitations in your report.
    """
    # this does not account for other possible file extensions unmentioned
    # along with any other links related to the policy
    return urlparse(url).path.lower().endswith(FILE_EXTENSIONS)



def describe_download(session, url):
    """
    Download the document at `url` and print its metadata: for example the
    URL, HTTP status, declared content type, downloaded size, and
    (optionally) the first few bytes of the response body.

    The downloaded data does not need to be saved to disk.

    TODO: implement this, using `fetch()` to make the request.
    """
    print("==========METADATA==========")
    # url of policy
    print(f"URL: \n{url}\n")

    try:
        response = fetch(session, url, stream=True)
    except requests.RequestException as error:
        print(f"Outcome: FAILED (request error: {error})")
        print("============================")
        return False

    downloaded_size_bytes = 0
    initial_bytes = b""
    try:
        with response:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if len(initial_bytes) < INITIAL_BYTES_SIZE:
                    initial_bytes += chunk[:INITIAL_BYTES_SIZE - len(initial_bytes)]
                downloaded_size_bytes += len(chunk)
    except requests.RequestException as error:
        print(f"HTTP status: {response.status_code} {response.reason}")
        print(f"Outcome: FAILED (error while reading body: {error})")
        print("============================")
        return False


    # HTTP status
    successful = 200 <= response.status_code < 300
    if not successful:
        print(f"Outcome: FAILED (HTTP {response.status_code})")
        return False
    print(f"HTTP status and reason: \n{response.status_code}  {response.reason}\n")
    # declared content-type
    print(f"Content-Type: \n{response.headers.get('Content-Type')}\n")
    # downloaded size
    downloaded_size_mb = downloaded_size_bytes / (1024 * 1024)
    print(f"Downloaded Size: \n{downloaded_size_bytes} ({downloaded_size_mb:.2f} MB)\n")
    # initial bytes of the downloaded file
    print(f"Initial Bytes: \n{initial_bytes}\n")

    print(f"Outcome: SUCCESS")
    print("============================")
    return True



def main():
    """
    main routine
    """

    parser = argparse.ArgumentParser(
        description="Minimal policy-document scraper prototype (CITS5501)."
    )
    parser.add_argument(
        "start_url",
        nargs="?",
        default=START_URL,
        help=f"index page to start from (default: {START_URL})",
    )
    args = parser.parse_args()

    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT

    print(f"Fetching index page: {args.start_url}")
    response = fetch(session, args.start_url)
    print(f"  status: {response.status_code}, "
          f"content type: {response.headers.get('Content-Type')}")

    links = extract_links(response.text, response.url)
    print(f"Found {len(links)} links:")
    for link in links:
        print(f"  {link}")

    policy_links = [link for link in links if is_policy_link(link)]
    print(f"{len(policy_links)} of these look like policy documents.")

    # TODO: choose 3-5 *distinct* policy links and call describe_download()
    # on each. Keep within MAX_REQUESTS (the index page already used one).

    unique_policy_links = list(
        dict.fromkeys(urldefrag(link)[0] for link in policy_links)
    )
    selected_docs = unique_policy_links[:MAX_DOCS]
    print(f"Selected {len(selected_docs)} distinct documents:\n")
 
    succeeded = 0
    attempted = 0
    for doc in selected_docs:
        try:
            attempted += 1
            if describe_download(session, doc):
                succeeded += 1
        except RequestLimitExceeded as error:
            print(f"Stopping: {error}")
            break
 
    print(f"Downloads succeeded: {succeeded} of {attempted} attempted")
    print(f"Requests made: {_request_count} (limit {MAX_REQUESTS})")
    return 0 if succeeded > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
