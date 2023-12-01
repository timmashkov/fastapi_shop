from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


class Post(Base):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(String(100), nullable=False, unique=False)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    #user_link: Mapped["User"] = relationship('User', backref='post_link')
