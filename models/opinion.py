from peewee import *

from .base_model import BaseModel
from .user import User


class Opinion(BaseModel):
    id = AutoField()
    from_user = ForeignKeyField(User, backref='created_opinions')
    to_user = ForeignKeyField(User, backref='received_opinions', null=True)
    text = TextField()
    received = BooleanField(default=False)
