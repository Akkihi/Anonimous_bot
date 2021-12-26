from aiogram.types import CallbackQuery

import models
from auth import dp
from ..commands.start import start


@dp.callback_query_handler(lambda query: query.data and query.data.startswith('delete_opinion$'), state='*')
async def delete_opinion(callback_query: CallbackQuery):
    opinion_id = callback_query.data.split('$')[1]
    db_opinion = models.Opinion.get(id=opinion_id)
    db_opinion.delete_instance()

    await callback_query.message.delete_reply_markup()

    await start(callback_query.message)
