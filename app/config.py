from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    
    Follows the 12-Factor App methodology: configuration varies
    per environment but code remains identical.
    """

    model_config = SettingsConfigDict(
        env_file=".env",           # Load from .env file in development
        env_file_encoding="utf-8", # Encoding for .env file
        extra="ignore"             # Ignore extra env vars not defined here
    )

    # Database configuration
    database_url: str = "sqlite:///./test.db"  # Default to SQLite for local dev

    #security settings
    secret_key: str = "dev-secret-key"

    # Application
    debug: bool = False
    app_name: str = "Python API Learning"
    app_version: str = "0.1.0"

# Singleton instance: created once, imported everywhere
settings = Settings()