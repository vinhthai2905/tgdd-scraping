from pydantic import BaseModel, Field
from typing import List, Optional
from decimal import Decimal


class ProductChoice(BaseModel):
    choice: str

class ProductChoiceCreate(ProductChoice):
    product_id: int

class ProductChoiceRead(ProductChoice):
    id: int

    model_config = {
        "from_attributes": True  
    }

class Product(BaseModel):
    name: str
    image: Optional[str] = None
    exclusive_tag: Optional[str] = None
    product_new: Optional[str] = None
    product_installment: Optional[str] = None
    product_tech: Optional[str] = None
    product_price: Optional[str] = None
    old_price: Optional[str] = None
    gift: Optional[str] = None
    sold_quantity: Optional[str] = None
    star: Optional[float] = None

class ProductCreate(Product):
    pass

class ProductRead(Product):
    id: int
    choices: List[ProductChoiceRead] = []

    model_config = {
        "from_attributes": True  
    }