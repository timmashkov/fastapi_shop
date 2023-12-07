from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class Chat(Base):
    __tablename__ = "chat"

    message: Mapped[str] = mapped_column(String(50), nullable=True, unique=False)
    sent_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
