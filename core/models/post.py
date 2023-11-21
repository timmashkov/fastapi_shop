from .mixin import UserRelationMixin
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


class Post(UserRelationMixin, Base):
    __tablename__ = "post"
    _user_back_populates_ = "posts"

    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=False)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")

    def __str__(self):
        return f'{self.__class__.__name__}(title={self.title})(body={self.body})'

    def __repr__(self):
        return str(self)
