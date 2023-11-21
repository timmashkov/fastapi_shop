from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from core.models.base import Base


class Profile(Base):
    __tablename__ = "profile"

    first_name: Mapped[str | None] = mapped_column(String(20), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(20), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), unique=True)
