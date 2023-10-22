import aiosqlite
from aiogram.fsm.context import FSMContext


async def db_start():
    async with aiosqlite.connect('src/utils/tg.db') as db:
        cur = await db.cursor()

        await cur.execute("CREATE TABLE IF NOT EXISTS accounts ("
                          "id INTEGER PRIMARY KEY,"
                          "eng_level TEXT, "
                          "name TEXT, "
                          "surname TEXT,"
                          "phone INTEGER,"
                          "user_id INTEGER) ")

        await db.commit()


async def add_item(state: FSMContext):
    async with aiosqlite.connect('src/utils/tg.db') as db:
        cur = await db.cursor()
        data = await state.get_data()
        await cur.execute(
            "INSERT INTO accounts (eng_level, name, surname, phone, user_id) VALUES (?, ?, ?, ?, ?)",
            (data['eng_level'], data['name'], data['surname'], data['phone'], data['user_id']))
        await db.commit()


async def get_user_id():
    async with aiosqlite.connect('src/utils/tg.db') as db:
        cur = await db.cursor()
        await cur.execute("SELECT user_id FROM accounts")
        dates = await cur.fetchall()
        return dates


async def get_user_data():
    async with aiosqlite.connect('src/utils/tg.db') as db:
        cur = await db.cursor()
        await cur.execute("SELECT * FROM accounts")
        dates = await cur.fetchall()
        return dates
