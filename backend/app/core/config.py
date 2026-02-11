from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Aurum"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/aurum"

settings = Settings()
