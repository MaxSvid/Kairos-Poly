from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from backend.settings import BotSettings
from backend.bot import keyboards

router = Router()
bot_settings = BotSettings()

WELCOME_TEXT = (
    "Hi! Welcome to Kairos Bot!\n\n"
    "Commands:\n"
    "/track <wallet_address> [name] — start tracking a wallet\n"
    "/untrack <wallet_address> — stop tracking\n"
    "/list — show tracked wallets\n"
    "/plan — show your plan, wallets and notification stats\n"
    "/notifymode <full|compact> — set notification style\n"
    "/add — add new wallet to database\n"
    "/help — show this message\n"
    "/kairos_whales — showing main wallets that being tracked"
)


@router.message(Command("start"))
async def start_handler(message: Message):
    user_id = message.from_user.id

    if user_id not in bot_settings.allowed_user_ids:
        await message.answer("You are not authorized to use it.")
        return

    await message.answer(WELCOME_TEXT, reply_markup=keyboards.main)