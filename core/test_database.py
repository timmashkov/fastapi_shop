from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from core.config import settings


class TestDatabase:
    def __init__(self, url: str, echo: bool):
        self.test_engine = create_async_engine(url=url,
                                               poolclass=NullPool,
                                               echo=echo)
        self.test_session_maker = async_sessionmaker(bind=self.test_engine,
                                                     class_=AsyncSession,
                                                     expire_on_commit=False,
                                                     autoflush=False,
                                                     autocommit=False)


test_database = TestDatabase(url=settings.test_config.test_url, echo=settings.test_config.echo)
