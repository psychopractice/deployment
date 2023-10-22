from aiogram import Bot
import src.utils.database as db
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime


async def sched_message_fri(bot: Bot):
    userid_list = await db.get_user_id()

    for user_id in map(lambda x: int(x[0]), userid_list):

        await bot.send_message(
            chat_id=user_id,
            text='Привет!\n\n'
                 'Встречаемся уже завтра в 11:00 по ссылке: https://us02web.zoom.us/j/5952329889\n'
                 'Meeting ID: 595 232 9889'
        )
        await asyncio.sleep(0.3)


async def sched_message_sat(bot: Bot):
    userid_list = await db.get_user_id()

    for user_id in map(lambda x: int(x[0]), userid_list):

        await bot.send_message(
            chat_id=user_id,
            text='Hey\n'
                 'Сегодня у тебя первое занятие в нашем разговорном клубе'
                 ' Debate Clubs c Виталием Селюном. Подключайся в 11:00 по ссылке:\n'
                 'https://us02web.zoom.us/j/5952329889\n'
                 'Meeting ID: 595 232 9889\n'
                 'До встречи 😀'

        )
        await asyncio.sleep(0.3)


async def sched_message_soon(bot: Bot):
    userid_list = await db.get_user_id()

    for user_id in map(lambda x: int(x[0]), userid_list):

        await bot.send_message(
            chat_id=user_id,
            text='Hey\n'
                 'Начинаем уже через 15 минут! Ты готов к разговорной практике?'
                 'Подключайся по ссылке:\n'
                 'https://us02web.zoom.us/j/5952329889\n'
                 'Meeting ID: 595 232 9889\n'
                 'До встречи 😀'

        )
        await asyncio.sleep(0.3)


async def sched_message_last(bot: Bot):
    userid_list = await db.get_user_id()

    for user_id in map(lambda x: int(x[0]), userid_list):

        await bot.send_message(
            chat_id=user_id,
            text='Мы начинаем и уже ждем тебя!\n\n'
                 'Подключайся:\n'
                 'https://us02web.zoom.us/j/5952329889\n'
                 'Meeting ID: 595 232 9889'
        )
        await asyncio.sleep(0.3)


def start_scheduler(bot):
    schedule = AsyncIOScheduler(timezone='Europe/Moscow')

    schedule.add_job(sched_message_fri, trigger='cron', day_of_week='fri', hour=19,
                     start_date=datetime.now(), kwargs={'bot': bot})

    schedule.add_job(sched_message_sat, trigger='cron', day_of_week='sat', hour=9,
                     minute=45, start_date=datetime.now(), kwargs={'bot': bot})

    schedule.add_job(sched_message_last, trigger='cron', day_of_week='sat', hour=10,
                     minute=45, start_date=datetime.now(), kwargs={'bot': bot})

    schedule.add_job(sched_message_soon, trigger='cron', day_of_week='sat', hour=11,
                     minute=00, start_date=datetime.now(), kwargs={'bot': bot})

    schedule.start()
