from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class OrderProductLink(Base):
    __tablename__ = "order_product_link"
    __table_args__ = (
        UniqueConstraint("order_id", "product_id", name="uniq_index_order_product"),
    )

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    count: Mapped[int] = mapped_column(default=1, server_default="1")
    fixed_price: Mapped[int] = mapped_column(default=0, server_default="0")
