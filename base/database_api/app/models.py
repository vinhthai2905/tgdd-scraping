from typing import List
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, Numeric

class Base(DeclarativeBase):
    pass
    
    
class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(Text, nullable=False)
    product_image: Mapped[str] = mapped_column(Text)
    exclusive_tag: Mapped[str] = mapped_column(Text)
    product_new: Mapped[str] = mapped_column(Text)
    product_installment: Mapped[str] = mapped_column(Text)
    product_tech: Mapped[str] = mapped_column(Text)
    product_price: Mapped[str] = mapped_column(Text)
    old_price: Mapped[str] = mapped_column(Text)
    gift: Mapped[str] = mapped_column(Text)
    sold_quantity: Mapped[str] = mapped_column(Text)
    star: Mapped[float] = mapped_column(Numeric(3, 1), nullable=True)

    choices: Mapped[List["ProductChoice"]] = relationship(
    back_populates="product", cascade="all, delete"
)

class ProductChoice(Base):
    __tablename__ = 'product_choices'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'))
    choice: Mapped[str] = mapped_column(Text)

    product: Mapped["Product"] = relationship(back_populates="choices")

