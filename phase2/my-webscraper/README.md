### CITS5501 Project Phase 2 - Task 1 Prototype
`This is a minimal prototype, which has the objective of identifying and 'downloading' policy documents from the 'UWA Policy Library index page'. To
show that the scraper has achieved this, useful prints to the console are
used. Which outline the current progress of the scraper for retrieving policy documents, and metadata including: the policy document's url, HTTP status and reason of the request made for this action, declared content-type of the document, the downloaded size, and the initial bytes of the downloaded file.`

Group Number: 16
Group Name: '404 Brain Not Found'
Group Members:
                        Tyson Haines       (23779585)
                        Akshay Raghuwanshi (24991278)
                        Celine Xu          (24714078)
                        Kevin Tan          (23789621)
                        Khushi Sesetti     (23823678)


# What our scraper does?
  1. fetches the index page at:
            `https://uwa-policy.cits5501.arranstewart.io/policy/`

  2. extracts every '<a href>' link and resolves it to an absolute url.

  3. Keeps any link that is recognised as a policy document using the
     file extension expressed in the url.

  4. Removes any duplicate links and selects the first '5' distinct documents.
     Note: You can increase the number of distinct documents by increasing the
           'MAX_DOCS' variable. However, this scraper was built with the
           intention of a smaller request of downloads out of respect for site.

  5. Downloads each distinct document that was selected via stream (not saved
     to disk). Additionally, a console print displays the:

     -URL of the policy document
     -HTTP status and reason
     -Declared Content-Type
     -Downloaded Size
     -First 16 Bytes of the file
     -Outcome of the download: 'SUCCESS' or 'FAILED'



# What are the Requirements to run our Scraper?
    - have at least Python 3.8 or later installed

    - use the packages already provided in our 'requirements.txt'.
      This is to ensure the dependencies and their respective versioning
      for this scraper are configured and installed appropriately.

    * Network Access to the Policy site. Access to the site this scraper
      has been built for may be restricted based on the network you have
      access to. To use this scraper, you must either have access to the
      UWA Policy Library index page or at least a local copy of it.


# How to Run
  -  First retrieve our scraper script and other essential documents at
     our public GitHub repository:
              `https://github.com/TysonHaines/CITS5501-Group-16`

  #option 1
  -  Using `uv`, run in the command:
          `uv run --with-requirements requirements.txt scraper.py`
      
      -make sure `uv` is installed, and
      -make sure your CLI accepts bash commands

  #option 2
  -  If you do not have `uv` you can run the following commands:
          `python3 -m venv .venv
          source .venv/bin/activate          # Windows: .venv\Scripts\activate
          pip install -r requirements.txt
          python3 scraper.py`

  - If you are using a local copy `e.g. at localhost:3000`, run with the
    command:
`uv run --with-requirements requirements.txt scraper.py http://localhost:3000/`




# Safety and Politeness Limits
  As defined at the top of `scraper.py`, it is expected that users our scraper
  act respectfully and without malicious intent. To adhere to this, we have 
  limitation inducing variables:

  `MAX_REQUESTS` at 20 requests maximum (index page + downloads). Which   
  defines the total requests allowed for each program execution.
  -since our prototype only makes at most 6 request (1 index page + 5 downloads)
   the `MAX_DOCS` can be adjusted accordingly to make more requests within the
   20 requests limit.

  `TIMEOUT_SECONDS` at 10, as a timeout between each request made to the site

  `DELAY_SECONDS` at 1.0, to create a pause between consecutive requests



# Exit Codes
  `As part of professional practice, It was decided that the execution of the
  program should respond with appropriate exit codes for whether the program
  executed accordingly.`

  Similar to C-style exit codes, we had:
    0 - at least one document was downloaded successfully
    1 - the index page could not be fetched, or no document downloaded
        successfully















