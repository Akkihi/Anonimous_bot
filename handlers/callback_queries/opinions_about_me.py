from aiogram.types import CallbackQuery

import models
from auth import dp
from ui.inline import opinions_about_me_keyboard
from user_states_group import UserStatesGroup


@dp.callback_query_handler(lambda query: query.data and query.data == 'see_opinions', state='*')
async def opinions_about_me(callback_query: CallbackQuery):
    db_user = models.get_user(callback_query.from_user)
    opinions = models.Opinion.select().where(models.Opinion.to_user == db_user)

    if len(opinions) == 0:
        await callback_query.message.answer('Еще никто не оставил мнение о тебе')
        await callback_query.answer()
        await UserStatesGroup.default.set()
        return

    opinions_ids = models.get_opinions_ids(opinions)

    keyboard = opinions_about_me_keyboard.build(opinions_ids)
    await callback_query.message.answer('Мнения которые оставили о тебе:', reply_markup=keyboard)
    await callback_query.answer()
    await UserStatesGroup.default.set()
