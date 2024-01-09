import contextlib

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from .config import settings
from asyncio import current_task


class DataBase:
    def __init__(self, url: str, echo: bool = False):
        """
        Создаю асинхронный движок для алхимии
        """
        self._engine = create_async_engine(url=url, echo=echo)
        self._session_factory = async_sessionmaker(
            bind=self._engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def get_scoped_session(self):
        """
        Метод для работы с асинхронной БД
        """
        session = async_scoped_session(
            session_factory=self._session_factory, scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """
        Метод для работы с асинхронной БД с контекстным менеджером
        """
        session = self._session_factory()
        async with session as sess:
            yield sess
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        """
        Метод для работы с асинхронной БД без контекстного менеджера
        """
        session = self.get_scoped_session()
        yield session
        await session.close()


vortex = DataBase(settings.db.url, settings.db.echo)
