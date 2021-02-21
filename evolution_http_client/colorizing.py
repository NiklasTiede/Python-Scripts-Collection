

import requests
from pprint import pprint
url = 'https://google.com'
# r = requests.get(url)
# pprint(r.json())

params = dict(search='cats')

res = requests.get(url, params=params)
pprint(res.text)
