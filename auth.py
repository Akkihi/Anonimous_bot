import datetime

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.files import JSONStorage


TOKEN = ''
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=JSONStorage('aiogram.json'))
runner = Executor(dp, skip_updates=True)

