from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

class DbSettings(BaseModel):
    url: str = f'sqlite+aiosqlite:///{BASE_DIR}/test.sqlite3'
    echo: bool = True


class Settings(BaseSettings):
    db: DbSettings = DbSettings()


settings = Settings()
