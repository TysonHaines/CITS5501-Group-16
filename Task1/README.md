# CITS5501 Project Phase 2 – Task 1 Prototype

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-prototype-orange)

A minimal prototype whose objective is to **identify and "download" policy documents** from the UWA Policy Library index page.

To demonstrate that the scraper works, it prints useful progress information to the console, including each policy document's:

- URL
- HTTP status and reason
- Declared `Content-Type`
- Downloaded size
- Initial bytes of the downloaded file

---

## Group Details

**Group Number:** 16
**Group Name:** 404 Brain Not Found

| Member             | Student ID |
|--------------------|------------|
| Tyson Haines       | 23779585   |
| Akshay Raghuwanshi | 24991278   |
| Celine Xu          | 24714078   |
| Kevin Tan          | 23789621   |
| Khushi Sesetti     | 23823678   |

---

## What Our Scraper Does

1. **Fetches the index page** at:
   `https://uwa-policy.cits5501.arranstewart.io/policy/`
2. **Extracts every `<a href>` link** and resolves it to an absolute URL.
3. **Filters for policy documents**, keeping any link recognised as a document by the file extension in its URL.
4. **Removes duplicates** and selects the first **5** distinct documents.
5. **Downloads each selected document via stream** (nothing is saved to disk) and prints the following to the console:

   - URL of the policy document
   - HTTP status and reason
   - Declared `Content-Type`
   - Downloaded size
   - First 16 bytes of the file
   - Outcome of the download: `SUCCESS` or `FAILED`

> [!NOTE]
> The number of documents is set by the `MAX_DOCS` variable (default `5`). We recommend not raising it when running against the live site: the site rate-limits requests (see Section 5.2 of our report), and in our tests requests beyond the first five or six within roughly ten seconds were refused with HTTP 429.

---

## Requirements

- **Python 3.10 or later** (required by the pinned version of `requests`; Ubuntu 22.04's `python3` is 3.10, and `uv` will download a suitable Python if needed)
- **Packages listed in `requirements.txt`**, which ensures the dependencies and their versions are configured correctly.
- **Network access to the policy site.** Access may be restricted depending on your network. You must either be able to reach the UWA Policy Library index page, or have a local copy of it.

---

## How to Run

Run all commands below from the directory containing `scraper.py` and `requirements.txt` – that is, the `Task1/` directory of the submitted zip file.

Alternatively, if you have access to our private GitHub repository, you can clone it and change into the same directory:

```bash
git clone https://github.com/TysonHaines/CITS5501-Group-16.git
cd CITS5501-Group-16/Task1
```

### Option 1: Using `uv`

Make sure `uv` is installed and that your CLI accepts bash commands, then run:

```bash
uv run --with-requirements requirements.txt scraper.py
```

### Option 2: Without `uv`

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python3 scraper.py
```

On Windows, use `python` instead of `python3`.

### Using a local copy of the site

If you are using a local copy (e.g. at `localhost:3000`), pass its URL as an argument:

```bash
uv run --with-requirements requirements.txt scraper.py http://localhost:3000/
```

### Example output

A run takes about 6–10 seconds because of the one-second pause between requests. The program first prints every link found on the index page (over 400 on the live site), then a metadata block for each selected document, and finally a summary. Trimmed output from a run against the live site:

```text
Fetching index page: https://uwa-policy.cits5501.arranstewart.io/policy/
  status: 200, content type: text/html; charset=utf-8
Found 413 links:
  ... (one line per link) ...
215 of these look like policy documents.
Selected 5 distinct documents:

==========METADATA==========
URL:
https://uwa-policy.cits5501.arranstewart.io/policy/-/media/project/uwa/uwa/policy-library/policy/code-of-conduct/integrity/policy-framework/policy-governance-framework.pdf

HTTP status and reason:
200  OK

Content-Type:
application/pdf

Downloaded Size:
301201 (0.29 MB)

Initial Bytes:
b'%PDF-1.6\r%\xe2\xe3\xcf\xd3\r\n'

Outcome: SUCCESS
============================
... (four more documents) ...
Downloads succeeded: 5 of 5 attempted
Requests made: 6 (limit 20)
```

A document whose download fails is reported as `Outcome: FAILED`, together with the reason (for example `FAILED (HTTP 404)`).

---

## Safety and Politeness Limits

Users of this scraper are expected to act respectfully and without malicious intent. To support this, the following limits are defined at the top of `scraper.py`:

| Variable          | Default | Description                                                              |
|-------------------|---------|--------------------------------------------------------------------------|
| `MAX_REQUESTS`    | `20`    | Maximum total requests per program execution (index page + downloads).   |
| `TIMEOUT_SECONDS` | `10`    | Timeout for each request made to the site.                               |
| `DELAY_SECONDS`   | `1.0`   | Pause between consecutive requests.                                      |

> [!TIP]
> A normal run makes 6 requests through `fetch()` (1 index page + 5 downloads), well within `MAX_REQUESTS`. Note that redirects followed automatically by `requests` are not counted by `fetch()`, so the actual number of HTTP requests can be higher. A normal run is also at the edge of the live site's own rate limit: in one of our runs the last document received HTTP 429 and was reported as `FAILED (HTTP 429)`. Raising `MAX_DOCS` makes such failures more likely.

---

## Exit Codes

As part of professional practice, the program returns appropriate exit codes to indicate whether it executed successfully. Similar to C-style exit codes:

| Code | Meaning                                                                              |
|------|--------------------------------------------------------------------------------------|
| `0`  | At least one document was downloaded successfully.                                   |
| `1`  | The index page could not be fetched, or no document was downloaded successfully.     |

As a minimal prototype, the scraper does not handle index-page failures gracefully: a network error (e.g. the site is unreachable) stops the program with a Python traceback, which also exits with code `1`, and an index page returned with an HTTP error status is parsed as normal, so no documents are found and the program exits with code `1`.
