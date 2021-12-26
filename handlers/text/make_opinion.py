from aiogram.dispatcher import FSMContext
from aiogram.types import Message

import models
from auth import dp
from ui import menus_text
from ui.inline import menu_keyboard
from user_states_group import UserStatesGroup


@dp.message_handler(state=UserStatesGroup.wait_opinion)
async def make_opinion(message: Message, state: FSMContext):
    user_data = await state.get_data()

    to_user = models.User.get(models.User.telegram_id == int(user_data['to_user_id']))
    from_user = models.get_user(message.from_user)

    opinion_text = message.text
    models.Opinion.create(from_user=from_user, to_user=to_user, text=opinion_text)

    keyboard = menu_keyboard.build()
    await message.answer(menus_text.GIFT_SAVED)
    await message.answer(menus_text.MAIN_MENU, reply_markup=keyboard)
    await message.bot.send_message(to_user.telegram_id, 'Кто-то оставил мнение о тебе!')
    await UserStatesGroup.default.set()
