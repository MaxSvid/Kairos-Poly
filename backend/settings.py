from dataclasses import dataclass 
from dotenv import load_dotenv
import os

load_dotenv()

class Bot_Settings:
    BOT_TOKEN = os.environ.get("BOT_TOKEN"),
    BOT_NAME = os.environ.get(""),
    BOT_USERNAME = os.environ.get("")

bot_settings = Bot_Settings()   

class API_Settings:
    pass