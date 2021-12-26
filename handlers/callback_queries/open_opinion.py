from aiogram.types import CallbackQuery

import models
from auth import dp
from ui.inline import opened_opinion_keyboard
from user_states_group import UserStatesGroup
from utils.general import get_full_name


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('open_opinion$'), state='*')
async def open_opinion(callback_query: CallbackQuery):
    opinion_id = callback_query.data.split('$')[1]

    try:
        opinion = models.Opinion.get(id=opinion_id)
        opinion.received = True
        opinion.save()
    except models.opinion.DoesNotExist:
        await callback_query.answer('Ошибка!')
        await UserStatesGroup.default.set()
        return

    reply_markup = callback_query.message.reply_markup
    inline_keyboard_row = reply_markup['inline_keyboard'][0]

    for index in range(0, len(inline_keyboard_row)):
        callback_data = inline_keyboard_row[index]['callback_data']
        current_opinion_id = callback_data.split('$')[1]
        if current_opinion_id == opinion_id:
            inline_keyboard_row[index]['callback_data'] = 'opened_opinion$' + opinion_id
            inline_keyboard_row[index]['text'] = '🦜'

    keyboard = opened_opinion_keyboard.build(opinion_id)
    await callback_query.answer()
    await callback_query.message.edit_reply_markup(reply_markup)
    await callback_query.message.answer(opinion.text, reply_markup=keyboard)
    await UserStatesGroup.default.set()
