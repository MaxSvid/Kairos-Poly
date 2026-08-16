from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from backend.settings import BotSettings

router = Router()
bot_settings = BotSettings()


@router.message(Command("start"))
async def start_handler(message: Message):
    user_id = message.from_user.id

    if user_id not in bot_settings.allowed_user_ids:
        await message.answer("You are not authorized to use it.")
        return

    await message.answer("Welcome to Kairos Bot")