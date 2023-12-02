from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class Profile(Base):
    __tablename__ = "profile"

    first_name: Mapped[str | None] = mapped_column(String(20), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(20), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), unique=True)
    owner: Mapped["User"] = relationship("User", back_populates="profiles")
