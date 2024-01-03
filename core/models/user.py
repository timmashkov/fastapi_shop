from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base import Base


if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(40), nullable=False)
    username: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    post_link: Mapped[list["Post"]] = relationship("Post",
                                                   back_populates="user_link",
                                                   cascade="all, delete-orphan")
    profiles: Mapped["Profile"] = relationship("Profile",
                                               back_populates="owner",
                                               cascade="all, delete-orphan",
                                               passive_deletes=True,
                                               passive_updates=True)

    def __str__(self):
        return f"{self.__class__.__name__}(username={self.username})"

    def __repr__(self):
        return str(self)
