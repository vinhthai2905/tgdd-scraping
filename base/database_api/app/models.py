from typing import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String


class Base(DeclarativeBase):
    pass

class Brand(Base):
    __tablename__ = 'brand'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f'User(id={self.id!r})'
    
print(Base.metadata.tables)
