from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class DbSettings(BaseModel):
    """
    DataBase driver settings + db_url
    """
    db_host: str = os.environ.get("DB_HOST")
    db_name: str = os.environ.get("DB_NAME")
    db_port: str = os.environ.get("DB_PORT")
    db_user: str = os.environ.get("DB_USER")
    db_pass: str = os.environ.get("DB_PASS")
    url: str = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    echo: bool = False


class Settings(BaseSettings):
    """
    All api settings
    """
    auth_key: str = os.environ.get("SECRET_KEY")
    public_key: str = os.environ.get("PUBLIC_KEY")
    # email parameters
    GOOGLE_API_PASS: str = os.environ.get("GOOGLE_API_PASS")
    MAIL_PORT: str = os.environ.get("MAIL_PORT")
    MAIL_FROM: str = os.environ.get("MAIL_FROM")
    MAIL_SERVER: str = os.environ.get("MAIL_SERVER")
    MAIL_USERNAME: str = os.environ.get("MAIL_USERNAME")
    # db settings link
    db: DbSettings = DbSettings()
    # CORS сетап
    origins: list = ["http://127.0.0.1:8000"]


settings = Settings()
