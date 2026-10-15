import requests #for http request
from bs4 import BeautifulSoup

URL = 'https://uwa-policy.cits5501.arranstewart.io/policy/'
# send HTTP GET request
res = requests.get(URL)
print(res.status_code)
content = res.content

# parse HTML and format
soup = BeautifulSoup(content, 'html.parser')
#soup.prettify

current_policy_heading = None
policies = {}
current_policy = None


for element in soup.select("h3.policy__heading, ul.items li.item a div.label, ul.policy__list--documents li a"):

    if element.name == "h3":
        current_policy_heading = element.text.strip()
        policies.setdefault(current_policy_heading, {})

    elif "label" in element.get("class", []):
        current_policy = element.get_text(strip = True)

        if current_policy_heading is not None:
            policies[current_policy_heading].setdefault(current_policy, [])

    elif element.name == "a": # need to be more specific to avoid other hrefs!!!!!
        policy_pdf = element.find(string = True, recursive = False).strip()

        if current_policy_heading is not None and current_policy is not None:
            policies[current_policy_heading][current_policy].append(policy_pdf)

print(policies)
