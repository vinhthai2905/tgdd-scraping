from pydantic import BaseModel, Field
from typing import List, Optional
from decimal import Decimal


class ProductChoiceBase(BaseModel):
    choice: str

class ProductChoiceCreate(ProductChoiceBase):
    product_id: int

class ProductChoiceRead(ProductChoiceBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
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

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    choices: List[ProductChoiceRead] = []

    class Config:
        orm_mode = True