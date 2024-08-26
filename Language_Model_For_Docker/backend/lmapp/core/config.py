from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Language Model API"
    API_V1_STR: str = "/lmapi/v1"
    API_KEY: str = os.getenv("API_KEY", "default-secret-api-key")  # Use a default value if not set
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")  # Default to localhost

    class Config:
        # Read environment variables from the .env file
        env_file = ".env"

settings = Settings()
