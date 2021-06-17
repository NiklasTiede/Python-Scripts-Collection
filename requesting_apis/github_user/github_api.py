import configparser
import json
from pprint import pprint

import requests  # type: ignore
# credentials of sender email account:
config = configparser.ConfigParser()
config.read("../settings.ini")
GITHUB_USERNAME = config.get("settings", "GITHUB_USERNAME")
GITHUB_PASSWORD = config.get("settings", "GITHUB_PASSWORD")


r = requests.get('https://api.github.com/user', auth=(GITHUB_USERNAME, GITHUB_PASSWORD))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

pprint(r.json())

with open('github_acc.json', 'w') as f:
    json.dump(r.json(), f, sort_keys=True, indent=2)
