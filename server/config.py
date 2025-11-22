import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self):
        self.gpt_api_key = os.environ.get("GPT_API_KEY", "")
        self.jwt_secret = os.environ.get("JWT_SECRET", "default-secret-change-me")
        self.shell_user = os.environ.get("SHELL_USER", "retroko")
        self.shell_key_path = os.environ.get("SHELL_KEY_PATH", "/secret/key.pem")

settings = Settings()
