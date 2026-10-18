import requests #for http request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import os
from pathlib import Path

URL = 'https://uwa-policy.cits5501.arranstewart.io/policy/'
# send HTTP GET request
res = requests.get(URL)
print(res.status_code)
content = res.content

# parse HTML and format
soup = BeautifulSoup(content, 'html.parser')
#soup.prettify

current_policy_heading = None
policies_dict = {}
current_policy = None

total_requests_made = 0
MAX_REQUESTS_PERMITTED = 5
new_session_required = False
for element in soup.select("h3.policy__heading, ul.items li.item a div.label, ul.policy__list--documents li a"):

    if element.name == "h3":
        current_policy_heading = element.text.strip()
        policies_dict.setdefault(current_policy_heading, {})

    elif "label" in element.get("class", []):
        current_policy = element.get_text(strip = True)

        if current_policy_heading is not None:
            policies_dict[current_policy_heading].setdefault(current_policy, [])

    elif element.name == "a": # need to be more specific to avoid other hrefs!!!!!
        policy_pdf_link = element.get("href") # this retrieves the relative link
        complete_url = urljoin(URL, policy_pdf_link) # this ensures the absolute link for each policy is resolved

        if current_policy_heading is not None and current_policy is not None:
            policies_dict[current_policy_heading][current_policy].append(complete_url)


def download_file(url, proj_dir="policy_downloads"):
    global total_requests_made
    global new_session_required
    if total_requests_made < MAX_REQUESTS_PERMITTED:
        # get tye current project directory path
        proj_dir_path = Path(__file__).parent.absolute()
        # create the target destination directory
        dest_dir = proj_dir_path / proj_dir
        dest_dir.mkdir(parents=True, exist_ok=True)
        # extract the original filename from the url
        filename = url.split("/")[-1]
        file_path = dest_dir / filename

        print(f"downloading '{filename}' to: {file_path}")

        # stream and write the file in binary mode
        with requests.get(url, stream=True) as response:
            response.raise_for_status() # check for HTTP errors
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        print("DOWNLOAD COMPLETE")
        total_requests_made += 1
    else:
        print("requests limit reached. Must create new session continuing from here")
        new_session_required = True


# print(policies)
policy_types = policies_dict.keys()
for policy_type in policy_types:
    policies = policies_dict[policy_type]
   # print(f"==={policy_type}===")
    policy_titles = policies.keys()
    for policy_title in policy_titles:
        # print(policy_title)
        policy_pdf_links = policies_dict[policy_type][policy_title]
        while (new_session_required == False):
            for policy_pdf_link in policy_pdf_links:
            # print(f"> {policy_pdf_link}\n")
                download_file(policy_pdf_link)
    print("\n\n")

