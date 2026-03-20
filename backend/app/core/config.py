from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ProductPulse AI API"
    app_env: str = "dev"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    openai_api_key: str = ""
    openai_model: str = "gpt-5.4"
    postgres_url: str = "postgresql://postgres:postgres@localhost:5432/productpulse"
    qdrant_url: str = "http://localhost:6333"
    redis_url: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
