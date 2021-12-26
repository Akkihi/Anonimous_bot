import asyncio
import random
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, User, InputMediaDocument, InputFile

from auth import dp
import handlers


executor.start_polling(dp, skip_updates=True)
