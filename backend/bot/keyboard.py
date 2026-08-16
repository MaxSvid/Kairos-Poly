from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Back button (reused across menus)
back_button = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="menu_back")]]
)

# Main menu
main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Polymarket", callback_data="reports_menu")],
        [InlineKeyboardButton(text="Wallets", callback_data="reports_menu")],
        [InlineKeyboardButton(text="Positions", callback_data="reports_menu")],
        [InlineKeyboardButton(text="Settings", callback_data="menu_settings")]
    ]
)

# Settings menu
settings_options = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bot GitHub", url="")],
        *back_button.inline_keyboard,
    ]
)