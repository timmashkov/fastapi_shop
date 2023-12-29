from typing import TYPE_CHECKING

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from core.models import Base
from .order_product_link import OrderProductLink

if TYPE_CHECKING:
    from .product import Product


class Order(Base):
    __tablename__ = "order"

    promocode: Mapped[str | None] = mapped_column(
        String(30), unique=True, nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="order_product_link",
        back_populates="orders"
    )
