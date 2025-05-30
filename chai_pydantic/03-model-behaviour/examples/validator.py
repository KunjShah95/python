from pydantic import BaseModel,field_validator, model_validator, computed_field

class User(BaseModel):
    username: str
    
    @field_validator('username')
    def username_length(cls, value):
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return value
    
class SignupData(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode='after')
    def passwords_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values
    
class Product(BaseModel):
    price: float
    quantity:int
    
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    