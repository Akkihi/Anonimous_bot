from aiogram.types import Message

import models
from auth import dp
from ui.inline import menu_keyboard
from user_states_group import UserStatesGroup


@dp.message_handler(lambda msg: msg.chat.id == msg.from_user.id, commands=['start', 'menu'], state='*')
async def start(message: Message):
    if not message.from_user.is_bot:
        models.get_user(message.from_user)

    keyboard = menu_keyboard.build()
    await message.answer(
        'Привет!\nЗдесь ты можешь анонимно написать о человеке все что ты о нем думаешь и узнать что думают о тебе другие.\n'
        'Чтобы заново вызвать меню, используйте /start или /menu\n'
        'Выбери действие:',
        reply_markup=keyboard)
    await UserStatesGroup.default.set()
