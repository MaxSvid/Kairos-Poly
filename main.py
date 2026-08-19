import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from backend.settings import BotSettings
from dotenv import load_dotenv

load_dotenv()


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BotSettings.BOT_TOKEN)
    dp = Dispatcher()


    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt():
        print("Bot stopped")

