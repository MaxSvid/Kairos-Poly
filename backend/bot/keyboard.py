from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Back button (reused across menus)
back_button = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="menu_back")]]
)


# list of 2 buttons to render side by side.
main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Track/Untrack", callback_data="menu_track"),
            InlineKeyboardButton(text="📋 My wallets", callback_data="menu_wallets"),
        ],
        [
            InlineKeyboardButton(text="ℹ️ Help", callback_data="menu_help"),
            InlineKeyboardButton(text="🔔 Notify mode", callback_data="menu_notify"),
        ],
        [
            InlineKeyboardButton(text="💳 Subscribe", callback_data="menu_subscribe"),
            InlineKeyboardButton(text="💼 My plan", callback_data="menu_plan"),
        ],
    ]
)


# Every submenu ends with the same reusable back_button row, so pressing
# Back always returns to the main menu via the "menu_back" callback.

track_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Track a wallet", callback_data="track_add")],
        [InlineKeyboardButton(text="Untrack a wallet", callback_data="track_remove")],
        *back_button.inline_keyboard,
    ]
)

wallets_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="View tracked wallets", callback_data="wallets_list")],
        *back_button.inline_keyboard,
    ]
)

help_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Commands", callback_data="help_commands")],
        [InlineKeyboardButton(text="Contact support", callback_data="help_support")],
        *back_button.inline_keyboard,
    ]
)

notify_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="All alerts", callback_data="notify_all")],
        [InlineKeyboardButton(text="Large moves only", callback_data="notify_large")],
        [InlineKeyboardButton(text="Muted", callback_data="notify_off")],
        *back_button.inline_keyboard,
    ]
)

subscribe_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="View plans", callback_data="subscribe_view")],
        *back_button.inline_keyboard,
    ]
)

plan_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Current plan details", callback_data="plan_details")],
        *back_button.inline_keyboard,
    ]
)


# Settings menu kept from original file
settings_options = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bot GitHub", url="")],
        *back_button.inline_keyboard,
    ]
)