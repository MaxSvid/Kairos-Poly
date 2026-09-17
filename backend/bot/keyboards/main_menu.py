from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔄 Track/Untrack"), KeyboardButton(text="📋 My wallets")],
        [KeyboardButton(text="ℹ️ Help"), KeyboardButton(text="🔔 Notify mode")],
        [KeyboardButton(text="💳 Subscribe"), KeyboardButton(text="💼 My plan")],
    ],
    resize_keyboard=True,
)
