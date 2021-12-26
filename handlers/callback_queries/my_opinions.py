from aiogram.types import CallbackQuery

import models
from auth import dp
from ui.inline import users_keyboard
from user_states_group import UserStatesGroup


@dp.callback_query_handler(lambda query: query.data and query.data == 'my_opinions', state='*')
async def make_gift(callback_query: CallbackQuery):
    all_users = models.User.select().where((models.User.telegram_id != 1262766248) &
                                           (models.User.telegram_id != callback_query.from_user.id))

    keyboard = users_keyboard.build(all_users)
    await callback_query.message.answer('Всего пользователей: {}\nВыберите пользователя:'.format(len(all_users) + 1),
                                        reply_markup=keyboard)
    await callback_query.answer()
    await UserStatesGroup.default.set()
