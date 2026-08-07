from dataclasses import dataclass, field
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class BotSettings:
    bot_token: str = field(default_factory=lambda: os.getenv("BOT_TOKEN", ""))
    bot_name: str = field(default_factory=lambda: os.getenv("BOT_NAME", ""))
    bot_username: str = field(default_factory=lambda: os.getenv("BOT_USERNAME", ""))

@dataclass
class DatabaseSettings:
    db_host: str = field(default_factory=lambda: os.getenv("DB_HOST", "localhost"))
    db_port: str = field(default_factory=lambda: os.getenv("DB_PORT", "5432"))
    db_name: str = field(default_factory=lambda: os.getenv("DB_NAME", "kairos_test_db"))
    db_user: str = field(default_factory=lambda: os.getenv("DB_USER", "project_service"))
    db_password: str = field(default_factory=lambda: os.getenv("DB_PASSWORD", "change_me_bot_password"))

# Instantiate clean global configuration objects
bot_settings = BotSettings()
db_settings = DatabaseSettings()
