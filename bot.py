import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from config import BOT_TOKEN

# импорт моделей (создает таблицы)
import models

# импорт обработчиков
from handlers.start import router as start_router
from handlers.admin import router as admin_router


bot = Bot(BOT_TOKEN)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(admin_router)


async def main():
    print("===================================")
    print("BOT STARTED")
    print("===================================")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
