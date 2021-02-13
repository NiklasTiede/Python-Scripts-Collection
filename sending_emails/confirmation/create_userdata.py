
import json

users = {}

users['AliceCooper@gmail.com'] = {'firstName': 'Alice', 'lastName': 'Cooper'}
users['OzzyOsbourne@gmail.com'] = {'firstName': 'Ozzy', 'lastName': 'Osbourne'}

# check dict
for email, info in users.items():
    firstName, lastName = info.values()

with open('userData.json', 'w') as f:
    json.dump(users, f, sort_keys=True, indent=2)
