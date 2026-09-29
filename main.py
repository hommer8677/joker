import asyncio, logging, os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats
from aiogram import F, types

#from handlers.private import private_router
from handlers.groups import group_router

load_dotenv()
TOKEN=os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_routers(group_router)
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
    except Exception:
        logging.exception("Бот остановлен из-за ошибки")
        raise