from peewee import SqliteDatabase, Model


DATABASE = 'db.db'
db = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = db
