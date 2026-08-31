from aiogram import Bot, Dispatcher

from backend.settings import bot_settings
from backend.bot.handlers.start import router as start_router


def create_bot() -> Bot:
    return Bot(token=bot_settings.bot_token)


def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher()

    dispatcher.include_router(start_router)
    return dispatcher
