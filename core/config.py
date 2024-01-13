from pydantic_settings import BaseSettings
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)

class DbSettings(BaseSettings):
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


class TestConfig(BaseSettings):
    db_host_test: str = os.environ.get("DB_HOST_TEST")
    db_name_test: str = os.environ.get("DB_NAME_TEST")
    db_port_test: str = os.environ.get("DB_PORT_TEST")
    db_user_test: str = os.environ.get("DB_USER_TEST")
    db_pass_test: str = os.environ.get("DB_PASS_TEST")
    test_url: str = f"postgresql+asyncpg://{db_user_test}:{db_pass_test}@{db_host_test}:{db_port_test}/{db_name_test}"
    lite_url: str = "sqlite+aiosqlite:///./test.db"
    echo: bool = True


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
    # Redis
    redis_port: str = os.environ.get("REDIS_PORT")
    redis_host: str = os.environ.get("REDIS_HOST")
    # TestConfig
    test_config: TestConfig = TestConfig()


settings = Settings()
