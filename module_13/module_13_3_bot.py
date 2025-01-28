
# использую aiogram 3.x !!!!!!!!!!!
import asyncio
import os.path

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage

api = ""  # ваш ключ
if os.path.exists("module_13_key.py"):  # это мой ключ на моем локальном компе
    from module_13_key import api  #

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start(message : types.Message):
    print('Привет! Я бот мешающий твоему здоровью.')
    await message.answer('Привет! Я бот мешающий твоему здоровью.')


@dp.message()
async def default_message(message : types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

# @dp.message()
# async def default_message(msg):
#     print(f"мы получили:{msg.text}")

# цикл обработки сообщения. вместо executor.start_polling
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
