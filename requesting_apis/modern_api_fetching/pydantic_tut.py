from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'


user = User(id='12')
print(user)

print(user.dict())
print(user.json())
