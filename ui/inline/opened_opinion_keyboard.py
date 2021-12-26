from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build(opinion_id) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    delete_button = InlineKeyboardButton(text='Удалить', callback_data='delete_opinion$' + str(opinion_id))
    keyboard.row(delete_button)
    return keyboard
