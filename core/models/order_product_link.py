from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint

from .base import Base

order_product_link = Table(
    "order_product_link",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("order.id"), nullable=False),
    Column("product_id", ForeignKey("product.id"), nullable=False),
    UniqueConstraint("order_id", "product_id", name="uniq_index_order_product")
)
