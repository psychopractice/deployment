import os

from aiogram import Dispatcher, Bot
import asyncio
from dotenv import load_dotenv
import logging
from src.routers import client, data
import src.utils.database as db
from src.schedule_tasks.sheduler import start_scheduler


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    load_dotenv('.env')

    bot = Bot(token=os.getenv('TOKEN'))

    dp = Dispatcher()
    dp.include_routers(client.client_router, data.data_router)

    start_scheduler(bot)

    await db.db_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())

    except(SystemExit, KeyboardInterrupt):
        print('bot stopped')
