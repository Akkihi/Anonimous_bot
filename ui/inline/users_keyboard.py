from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import models


def build(users: List[models.User]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    for user in users:
        button = InlineKeyboardButton(text=user.first_name or '' + user.last_name or '',
                                      callback_data='select_user$' + str(user.telegram_id))
        keyboard.add(button)
    return keyboard
