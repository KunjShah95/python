from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool 
    
input_data ={'id': 1, 'name': 'John Doe', 'email': 'abc@gmail.com', 'is_active': True}       
    
user = User(**input_data)
print(user)