import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TIMEZONE: str   = os.getenv("TIMEZONE", "UTC")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "unsafe-dev-key")
    DEBUG: bool     = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")
    ALLOWED_HOSTS: list[str] = [
        host.strip()
        for host in os.getenv("APP_URL", "localhost,127.0.0.1").split(",")
        if host.strip()
    ]
    DB_NAME: str = os.getenv("DB_NAME", "")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASS: str = os.getenv("DB_PASS", "")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 3306))
