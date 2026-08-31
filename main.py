import asyncio
import logging
import sys

from backend.bot.bot import create_bot, create_dispatcher


async def main() -> None:
    bot = create_bot()
    dispatcher = create_dispatcher()

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(
            level=logging.INFO,
            stream=sys.stdout,
        )
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
