from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base import Base

if TYPE_CHECKING:
    from .user import User


class Post(Base):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=False)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    user_link: Mapped["User"] = relationship("User", back_populates="post_link")
