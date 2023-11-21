from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base

class Product(Base):
    __tablename__ = 'product'

    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer)

    def __str__(self):
        return f'{self.__class__.__name__}(name={self.name})(description={self.description})' \
               f'(price={self.price})'

    def __repr__(self):
        return str(self)
