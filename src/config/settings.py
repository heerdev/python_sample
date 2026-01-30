from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    app_name: str = "SampleApp"
    env: str = "dev"

    class Config:
        env_file = f".env.{os.getenv('PROFILE', 'dev')}"


settings = Settings()
