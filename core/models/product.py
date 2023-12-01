from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base import Base


if TYPE_CHECKING:
    from .user import User


class Product(Base):
    __tablename__ = 'product'

    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["User"] = relationship('User', back_populates='products')

    def __str__(self):
        return f'{self.__class__.__name__}(name={self.name})(description={self.description})' \
               f'(price={self.price})'

    def __repr__(self):
        return str(self)
