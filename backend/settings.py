from dataclasses import dataclass, field
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class BotSettings:
    bot_token: str = field(default_factory=lambda: os.getenv("BOT_TOKEN", ""))
    bot_name: str = field(default_factory=lambda: os.getenv("BOT_NAME", ""))
    bot_username: str = field(default_factory=lambda: os.getenv("BOT_USERNAME", ""))

    # The only two people allowed to use the bot.
    user_id: int = field(default_factory=lambda: int(os.getenv("USER_ID", "0")))
    my_id: int = field(default_factory=lambda: int(os.getenv("MY_ID", "0")))
 
    @property
    def allowed_user_ids(self) -> set[int]:
        return {self.user_id, self.my_id}

@dataclass
class DatabaseSettings:
    db_host: str = field(default_factory=lambda: os.getenv("DB_HOST"))
    db_port: str = field(default_factory=lambda: os.getenv("DB_PORT"))
    db_name: str = field(default_factory=lambda: os.getenv("DB_NAME"))
    db_user: str = field(default_factory=lambda: os.getenv("DB_USER"))
    db_password: str = field(default_factory=lambda: os.getenv("DB_PASSWORD"))

# Instantiate clean global configuration objects
bot_settings = BotSettings()
db_settings = DatabaseSettings() 
 