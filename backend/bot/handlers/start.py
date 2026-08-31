from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

WELCOME_TEXT = (
    "Hi! I track Polymarket positions.\n\n"
    "Commands:\n"
    "/track <wallet_address> [name] — start tracking a wallet\n"
    "/untrack <wallet_address> — stop tracking\n"
    "/list — show tracked wallets\n"
    "/plan — show your plan, wallets and notification stats\n"
    "/notifymode <full|compact> — set notification style\n"
    "/subscribe — view subscription plans\n"
    "/help — show this message\n\n"
    "For support, contact @mak_sjr"
)

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(WELCOME_TEXT)
    await message.answer("Main menu:")


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(WELCOME_TEXT)