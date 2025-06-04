import os
import dotenv

class Settings:
    def __call__(self):
        dotenvn.config()
        self.gpt_api_key = os.environ.get("GPT_API_KEY", "")
        self.jwt_secret = os.environ.get("JWT_SECRET", "")
        self.shell_user = os.environ.get("SHELL_USER", "retroko")
        self.shell_key_path = os.environ.get("SHELL_KEY_PATH", "/secret/key.pem")

settings = Settings()