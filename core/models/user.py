from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base

class User(Base):
    __tablename__ = 'user'

    username: Mapped[str] = mapped_column(String(20), unique=True)
