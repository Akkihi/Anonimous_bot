from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import models
from auth import dp
from user_states_group import UserStatesGroup


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('change_opinion$'), state='*')
async def change_opinion(callback_query: CallbackQuery, state: FSMContext):
    try:
        opinion = models.Opinion.get(models.Opinion.id == int(callback_query.data.split('$')[1]))
        to_user = opinion.to_user
        opinion.delete_instance()
    except Exception as e:
        print(e)
        await callback_query.message.answer('Ошибка')
        return
    await callback_query.message.answer('Старое мнение удалено {}\nВаше новое мнение:'.format(to_user.username))
    await UserStatesGroup.wait_opinion.set()
    await state.update_data(to_user_id=to_user.telegram_id)
    await callback_query.answer()
