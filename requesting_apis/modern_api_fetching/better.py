

import json
from typing import Optional

from pydantic import BaseModel
import requests


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None



class ActivitySchema(BaseModel):
    activity: str
    participants: int
    # price: float


def get_activity():
    resp = requests.get('https://boredapi.com/api/activity').json()
    validated_resp = ActivitySchema().validate(resp)
    print(validated_resp)
    # return Activity(
    #     activity=resp["activity"],
    #     participants=resp["participants"],
    #     price=resp["price"]
    # )


print(get_activity())

# with open('boredapi_request.json', 'w') as f:
#    the_dump = json.dumps(activity, sort_keys=True, indent=4)
#    f.write(the_dump)