from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class DbSettings(BaseModel):
    db_host: str = os.environ.get("DB_HOST")
    db_name: str = os.environ.get("DB_NAME")
    db_port: str = os.environ.get("DB_PORT")
    db_user: str = os.environ.get("DB_USER")
    db_pass: str = os.environ.get("DB_PASS")
    url: str = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    echo: bool = False


class Settings(BaseSettings):
    auth_key: str = os.environ.get("SECRET_KEY")
    public_key: str = os.environ.get("PUBLIC_KEY")
    db: DbSettings = DbSettings()


settings = Settings()
