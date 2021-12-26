from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

import models
from auth import dp
from ui.inline import selected_opinion_keyboard
from user_states_group import UserStatesGroup


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('select_user$'), state='*')
async def select_user(callback_query: CallbackQuery, state: FSMContext):
    from_user = models.get_user(callback_query.from_user)
    to_user = models.User.get(models.User.telegram_id == int(callback_query.data.split('$')[1]))

    try:
        opinion = models.Opinion.get((models.Opinion.from_user == from_user) & (models.Opinion.to_user == to_user))
    except:
        await callback_query.message.answer('Вы еще не оставили мнение о {}\nВаше мнение:'.format(to_user.username))
        await UserStatesGroup.wait_opinion.set()
        await state.update_data(to_user_id=to_user.telegram_id)
        await callback_query.answer()
        return

    has_readed_text = 'Не было прочитано'
    if opinion.received:
        has_readed_text = 'Было прочитано'

    keyboard = selected_opinion_keyboard.build(opinion.id)
    await callback_query.message.answer('Ваше мнение оставленное о {}: \n{}\n{}'.format(to_user.username,
                                                                                        opinion.text, has_readed_text),
                                        reply_markup=keyboard)
    await UserStatesGroup.default.set()
    await callback_query.answer()
