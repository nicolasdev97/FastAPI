from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Ortiz"
    signup_ts: datetime | None = None
    friends: list[int] = []

# Datos que recibirá la clase User
external_data = {
    "id": 123,
    "signup_ts": "2017-07-01 12:35",
    "friends": [125, 130, 135]
}

# Desestructurar los atributos de external_data
user = User(**external_data)
print(user)
print(user.id)