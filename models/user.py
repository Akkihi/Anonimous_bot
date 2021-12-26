from peewee import *

from .base_model import BaseModel


class User(BaseModel):
    telegram_id = BigIntegerField(primary_key=True)
    first_name = TextField(null=True)
    last_name = TextField(null=True)
    username = TextField(null=True, unique=True)
