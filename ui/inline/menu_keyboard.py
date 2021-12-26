from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    my_opinions = InlineKeyboardButton(text='Мои мнения', callback_data='my_opinions')
    see_opinions = InlineKeyboardButton(text='Посмотреть мнения про меня', callback_data='see_opinions')
    keyboard.add(my_opinions)
    keyboard.add(see_opinions)
    return keyboard
