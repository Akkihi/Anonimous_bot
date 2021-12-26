import asyncio
import random
import os

from aiogram.types import Message, User


def get_gif(gif_type: str):
    files = os.listdir('static/gifs/' + gif_type)
    file_index = random.randint(0, len(files) - 1)
    file_path = 'static/gifs/{}/{}'.format(gif_type, files[file_index])
    return file_path


def get_full_name(user: User):
    return (user.first_name or '') + ' ' + (user.last_name or '')


async def try_delete(message: Message):
    try:
        await message.delete()
        await asyncio.sleep(2)
    except:
        pass
