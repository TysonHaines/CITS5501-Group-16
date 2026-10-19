# Policy scraper prototype -- Python starter

Starter code for Task 1 of the CITS5501 Project, Phase 2.

`scraper.py` fetches the policy index page, extracts its links and prints them.
Your job is to fill in the parts marked `TODO`: decide which links look like
policy documents, download 3-5 of them, and print their metadata.

## Requirements

- [uv](https://docs.astral.sh/uv/) (recommended), or plain `pip`
- Python 3.11 or later (which can be installed using uv - see below)

Dependencies (`requests`, `beautifulsoup4`) are included in `requirements.txt`,
and the sections below show how they can be installed.

It should be possible to develop on any of Linux, macOS or Windows.
(The marking environment is Linux, as previously specified - so it is a good idea
if someone can run the code on Linux before submitting - but in general, Python
code should work equally well on any platform.)

## Recommended approach, using uv

The only thing you *need* to install is [uv](https://docs.astral.sh/uv/); it runs on Windows, Linux, and
macOS, and will fetch a working version of Python and the other project
dependencies for you. You are welcome to install Python in some other way if you wish, but
we provide instructions that use uv.

A recommended way to manage requirements is as follows.

First, install uv by following the instructions at
<https://docs.astral.sh/uv/getting-started/installation/>.

Then, unzip this zip file to some location on your computer.
Included in the zip file is a `.python-version` file, which tells uv to use Python 3.12.
If you don't have Python already installed, then uv will install it the first time you run the following
ommand:

```bash
uv run --with-requirements requirements.txt scraper.py
```

uv downloads the dependencies _once_, and puts them into a cache, so that later
runs start quickly. To start from a different page (for instance, a server you
are running locally for testing):

```bash
uv run --with-requirements requirements.txt scraper.py http://localhost:3000/
```

## Using uv and an explicit virtual environment

You may be familiar with Python *virtual environments*. As an alternative to the "quick and
simple" approach above, it's also possible to create a virtual environment in the project directory:

```bash
uv venv
uv pip install -r requirements.txt
uv run scraper.py
```

This creates a directory `.venv` containing all project requirements. (Note that in general,
a `.venv` directory is tied to the exact location it's been created -- if you try to move or
rename your project directory, it may stop working.)

## Running without uv

If you already have a version of Python you prefer to use, the following commands
should work to install dependencies and run the main script.

```bash
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scraper.py
```

## Request limits

All requests should go through the `fetch()` function, which:

- sets a 10-second timeout (the `requests` library has no timeout by default),
- identifies the program with a User-Agent header,
- waits 1 second between requests, and
- stops the program after 20 requests.

It's recommended you keep these limits when running against the live site.

## Updating this README

When you submit, update this README -- delete the contents, and replace it with
your own content, so it describes *your* prototype: how to
run it, and anything a marker should know (e.g. extra command-line options or
dependencies you added).


