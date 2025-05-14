from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, ForeignKey, CheckConstraint

class Base(DeclarativeBase):
    pass

class Brand(Base):
    __tablename__ = 'brand'

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    brandName: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'User(id={self.id!r})'
    
class Product(Base):
    __tablename__ = 'product'

    __table_args__ = (
        CheckConstraint('price >= 0'),
        CheckConstraint('lastPrice >= 0'), 
        CheckConstraint('discount >= 0'),
        CheckConstraint('quantity >= 0'),
        CheckConstraint('sold >= 0'),
    )

    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    brandID: Mapped[str] = mapped_column(String(255), ForeignKey('brand.id'))
    productName: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    lastPrice: Mapped[int] = mapped_column(nullable=False)
    productDescription: Mapped[str] = mapped_column(nullable=True)
    discount: Mapped[int] = mapped_column(default=0)
    quantity: Mapped[int] = mapped_column(nullable=False)
    sold: Mapped[int] = mapped_column(default=0)    


class ProductImage(Base):
    __tablename__ = 'product_image'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    productID: Mapped[str] = mapped_column(String(50), ForeignKey('product.id'))
    imageURL: Mapped[str] = mapped_column(String(255), nullable=False)