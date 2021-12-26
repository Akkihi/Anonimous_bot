import os
from typing import List

from aiogram.types import User as TelegramUser
from aiogram.types import Message as TelegramMessage
from aiogram.types import Chat as TelegramChat
from peewee import *

from .base_model import BaseModel, DATABASE
from .user import User
from .opinion import Opinion


def init():
    db = SqliteDatabase(DATABASE)
    db.create_tables([
        User,
        Opinion
    ])


if not os.path.exists(DATABASE):
    init()


def get_user(telegram_user: TelegramUser) -> User:
    user, created = User.get_or_create(telegram_id=telegram_user.id)
    user.first_name = telegram_user.first_name
    user.last_name = telegram_user.last_name
    user.username = telegram_user.username
    user.save()
    return user


def get_opinions_ids(opinions) -> List[str]:
    opinions_ids = []
    for db_opinion in opinions:
        opinions_ids.append(db_opinion.id)
    return opinions_ids
