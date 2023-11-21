from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User


class UserRelationMixin:
    """
    Класс миксин для связи между моделями
    """
    _user_id_unique_: bool = False
    _user_back_populates_: str = None
    _user_id_nullable_: bool = False

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("user.id"),
                             unique=cls._user_id_unique_,
                             nullable=cls._user_id_nullable_)

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship("User",
                            back_populates=cls._user_back_populates_)
