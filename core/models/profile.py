from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from core.models.base import Base
from .mixin import UserRelationMixin


class Profile(UserRelationMixin, Base):
    __tablename__ = "profile"
    _user_id_unique_ = True
    _user_back_populates_ = "profile"

    first_name: Mapped[str | None] = mapped_column(String(20), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(20), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__}(first_name={self.first_name})(last_name={self.last_name})" \
               f"(biography={self.bio})"

    def __repr__(self):
        return str(self)
