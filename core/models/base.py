from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Чтобы таблица базовой модели не создавалась, укажу аттрибут __abstract__
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
