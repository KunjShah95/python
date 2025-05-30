from pydantic import BaseModel
from typing import List, Optional, Dict

class Cart(BaseModel):
    user_id:int
    quantities:List[str]
    items: List[Dict[str, int]]  # List of dictionaries with item_id and quantity
    total_price: Optional[float] = None  # Optional field for total price
    discount: Optional[float] = None  # Optional field for discount
    shipping_address: Optional[str] = None  # Optional field for shipping address
    
class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str] = []  # List of tags, default to empty list
    published_date: Optional[str] = None  # Optional field for published date
    comments: Optional[List[Dict[str, str]]] = None  # Optional list of comments


# Example usage
cart_data = {
    "user_id": 123,
    "quantities": ["item1", "item2"],
    "items": [{"item_id": 1, "quantity": 2}, {"item_id": 2, "quantity": 3}],
    "total_price": 99.99,
    "discount": 10.0,
    "shipping_address": "123 Main St, Anytown, USA"
}

cart = Cart(**cart_data)
print(cart)

blog= BlogPost(
    title="My First Blog Post",
    content="This is the content of my first blog post.",
    author="John Doe",
    tags=["blogging", "tutorial"],
    published_date="2023-10-01",
    comments=[{"user": "Jane", "comment": "Great post!"}, {"user": "Bob", "comment": "Thanks for sharing!"}]
)