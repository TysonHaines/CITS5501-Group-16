import requests #for http request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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

# print(policies)
policy_types = policies_dict.keys()
for policy_type in policy_types:
    policies = policies_dict[policy_type]
    print(f"==={policy_type}===")
    policy_titles = policies.keys()
    for policy_title in policy_titles:
        print(policy_title)
        policy_pdf_links = policies_dict[policy_type][policy_title]
        for policy_pdf_link in policy_pdf_links:
            print(f"> {policy_pdf_link}\n")
    print("\n\n")

