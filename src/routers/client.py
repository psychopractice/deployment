from aiogram.filters import CommandStart
from src.keyboards.client_kb import start_kb
from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext


client_router = Router()


@client_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        'Привет👋\n'
        'На связи студия разговорного английского языка YES! https://yes-grodno.by/\n'
        'Добро пожаловать на разговорный клуб Debate Clubs c Виталием Селюном.\n\n'
        'Для записи нажми кнопку "Записаться"',
        reply_markup=start_kb()
    )


@client_router.message(F.text == "Отмена")
async def cmd_panel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Вы вернулись обратно', reply_markup=start_kb())
