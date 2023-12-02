from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from core.models import Base


class Order(Base):
    __tablename__ = "order"

    promocode: Mapped[str] = mapped_column(String(30), unique=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
