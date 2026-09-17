from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from backend.bot.keyboards.main_menu import main_reply_keyboard

router = Router()


@router.message(Command("menu"))
async def show_main_menu(message: Message):
    await message.answer("Main menu:", reply_markup=main_reply_keyboard)


# Reply keyboard button presses arrive as plain text messages.
# F.text == "..." matches the exact label on the button.

@router.message(F.text == "🔄 Track/Untrack")
async def on_track_untrack(message: Message):
    await message.answer("Track/Untrack menu goes here.")


@router.message(F.text == "📋 My wallets")
async def on_my_wallets(message: Message):
    await message.answer("Your tracked wallets go here.")


@router.message(F.text == "ℹ️ Help")
async def on_help(message: Message):
    await message.answer("Help text goes here.")


@router.message(F.text == "🔔 Notify mode")
async def on_notify_mode(message: Message):
    await message.answer("Notify mode options go here.")


@router.message(F.text == "💳 Subscribe")
async def on_subscribe(message: Message):
    await message.answer("Subscription options go here.")


@router.message(F.text == "💼 My plan")
async def on_my_plan(message: Message):
    await message.answer("Your plan details go here.")
