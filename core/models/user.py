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

    post_link: Mapped[list["Post"]] = relationship('Post', backref="user_link")
    profiles: Mapped["Profile"] = relationship('Profile', backref='profile')

    def __str__(self):
        return f"{self.__class__.__name__}(username={self.username})"

    def __repr__(self):
        return str(self)
