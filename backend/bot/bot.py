from aiogram import Bot, Dispatcher

from backend.settings import bot_settings
from backend.bot.handlers.start import router as start_router
from backend.bot.handlers.menu import router as menu_router


def create_bot() -> Bot:
    return Bot(token=bot_settings.bot_token)


def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher()

    dispatcher.include_router(start_router)
    dispatcher.include_router(menu_router)
    return dispatcher
