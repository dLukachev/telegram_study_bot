import asyncio
import logging

from aiogram import Bot, Dispatcher

from Config import TOKEN
from hendlerStage.one import oneStage
from hendlerStage.two import twoStage
from hendlerStage.three import threeStage
from database.models import async_main


async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_routers(oneStage, twoStage, threeStage)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO) # Подключение логирования
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
