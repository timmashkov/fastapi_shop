from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base import Base
from .order_product_link import order_product_link


if TYPE_CHECKING:
    from .user import User
    from .order import Order


class Product(Base):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship("User", back_populates="products")
    orders: Mapped[list["Order"]] = relationship(secondary=order_product_link, back_populates="products")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(name={self.name})(description={self.description})"
            f"(price={self.price})"
        )

    def __repr__(self):
        return str(self)
