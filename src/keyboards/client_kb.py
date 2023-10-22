from aiogram import types


def start_kb() -> types.ReplyKeyboardMarkup:
    start_btn = [
            [
                types.KeyboardButton(text='Записаться')
            ]
        ]

    start_cmd = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=start_btn
        )

    return start_cmd


def eng_levels() -> types.ReplyKeyboardMarkup:
    start_btn = [
        [
            types.KeyboardButton(text='С нуля'),
            types.KeyboardButton(text='Начальный'),
            types.KeyboardButton(text='Продвинутый')
        ]
    ]

    start_cmd = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=start_btn
    )

    return start_cmd
