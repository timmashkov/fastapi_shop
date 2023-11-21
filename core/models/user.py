from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base import Base


if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(20), unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profiles: Mapped["Profile"] = relationship(back_populates='profile')
