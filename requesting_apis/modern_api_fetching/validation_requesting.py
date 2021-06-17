import dataclasses
import json
from dataclasses import dataclass

import desert
import requests  # type: ignore
from marshmallow import EXCLUDE
from marshmallow import fields
from marshmallow import pre_dump
from marshmallow import Schema
from marshmallow import validate


@dataclass
class Activity:
    activity: str
    participants: int = dataclasses.field(metadata=desert.metadata(
        fields.Int(
            requird=True,
            validate=validate.Range(
                min=1, max=50, error='Participants must be between 1 and 50')
        )
    ))
    price: float = dataclasses.field(metadata=desert.metadata(
        fields.Float(
            required=True,
            validate=validate.Range(
                min=0, max=.5, error="Price must be between 0 (0$) and .5 (50$)")
        ))
    )

    def __post_init__(self):
        """

        """
        self.price = self.price * 100


def get_activity():
    resp = requests.get('https://boredapi.com/api/activity').json()
    schema = desert.schema(Activity, meta={"unknown": EXCLUDE})
    return schema.load(resp)


print(get_activity())


# @dataclass
# class Activity:
#     activity: str
#     participants: int
#     price: float


# class ActivitySchema(Schema):
#     activity = fields.Str(required=True)
#     participants = fields.Int(required=True)
#     price = fields.Float(required=True)


# def get_activity():
#     resp = requests.get('https://boredapi.com/api/activity').json()
#     validated_resp = ActivitySchema(unknown=EXCLUDE).load(resp)
#     return Activity(
#         activity=resp["activity"],
#         participants=resp["participants"],
#         price=resp["price"]
#     )


# print(get_activity())

# with open('boredapi_request.json', 'w') as f:
#    the_dump = json.dumps(activity, sort_keys=True, indent=4)
#    f.write(the_dump)

# --------------

# dataclass makes more obvious which art of data the API returns
# marshmellow is used to deserialize and **validate data**

# easy way: for data validation, I should prfer to use something different than desert!
