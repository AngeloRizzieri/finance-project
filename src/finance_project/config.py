from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Project settings loaded from .env (copy from .env.example)."""
    DATA_DIR: str = "src/finance_project/data"
    RISK_FREE_DEFAULT: float = 0.0

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
