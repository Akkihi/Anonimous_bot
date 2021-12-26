from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build(opinions_ids: List[str]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=10)
    for id in opinions_ids:
        opinion_button = InlineKeyboardButton('💭', callback_data='open_opinion$' + str(id))
        keyboard.insert(opinion_button)
    return keyboard
