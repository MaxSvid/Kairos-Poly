from aiogram import BaseMiddleware
from backend.settings import bot_settings


class WhitelistMiddleware(BaseMiddleware):

    async def __call__(self, handler, event, data):
        user_id = event.from_user.id

        if user_id not in bot_settings.allowed_user_ids:
            await event.answer("You are not authorized to use it.")
            return

        return await handler(event, data)