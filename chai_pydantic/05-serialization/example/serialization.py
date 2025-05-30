from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
class User(BaseModel):
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S") if isinstance(v, datetime) else v}
    )
    
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = True
    created_at: datetime = datetime.now()
    tags: List[str] = []
    
     
# Create a user instance

user= User(
    id=1,
    name="Alice Smith",
    email="alice@example.com",
    address=Address(
        street="123 Main St",
        city="Anytown",
        zip_code="12345"
    ),
    is_active=True,
)

#using model_dump()  -> dict
user_data = user.model_dump()
print(user_data)
print("-------------------------------------------------------------")
print("\n")

#using model_dump_json() -> json
user_json = user.model_dump_json()
print(user_json)