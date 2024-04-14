"""
Файл настроек
"""
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    """
    Записанные параметры
    """
    server_host: str = '0.0.0.0'
    server_port: int = 8000
    database_url: str = 'sqlite:///./test.db'
    postgres_password: str = 'qwerty'

settings = Settings(
    _env_file=Path(__file__).parents[2].resolve()/".env",
    _env_file_encoding='utf-8'
)
