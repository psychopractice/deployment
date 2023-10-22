from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from src.keyboards.client_kb import eng_levels
import asyncio
from aiogram.fsm.state import State, StatesGroup
import src.utils.database as db
from src.keyboards.basic import cancel_kb

data_router = Router()


class NewOrder(StatesGroup):
    eng_level = State()
    name = State()
    surname = State()
    phone = State()
    user_id = State()


@data_router.message(F.text == 'Записаться')
async def cmd_reg(message: types.Message, state: FSMContext):
    await state.set_state(NewOrder.eng_level)

    await message.answer('Для записи на твое первое занятие укажи, пожалуйста, уровень владения английским языком ',
                         reply_markup=eng_levels())


@data_router.message(NewOrder.eng_level)
async def cmd_answer(message: types.Message, state: FSMContext):
    await state.update_data(eng_level=message.text)
    await state.set_state(NewOrder.name)

    await message.answer('Напишите своё имя',
                         reply_markup=cancel_kb())


@data_router.message(NewOrder.name)
async def cmd_answer(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(NewOrder.surname)

    await message.answer('Напишите свою фамилию',
                         reply_markup=cancel_kb())


@data_router.message(NewOrder.surname)
async def cmd_answer(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(NewOrder.phone)

    await message.answer('Введите ваш номер телефона',
                         reply_markup=cancel_kb())


@data_router.message(NewOrder.phone)
async def cmd_answer(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.update_data(user_id=message.from_user.id)

    await db.add_item(state)
    await state.clear()

    await message.answer(
        'Поздравляем, ты записался на первое занятие разговорного клуба Debate Clubs c Виталием Селюном🥳'
        'Занятие пройдет в субботу в 11:00. Ссылку на занятие вышлем перед занятием.'
    )

    await asyncio.sleep(20)

    await message.answer(
        'А пока подписывайся на наши соцсети\n'
        'P.S. там много полезных видео от наших преподавателей:\n'
        'Instagram: https://www.instagram.com/yesgrodno/\n'
        'TikTok: https://www.tiktok.com/@yesgrodno\n'
    )

