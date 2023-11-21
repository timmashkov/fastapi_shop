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
