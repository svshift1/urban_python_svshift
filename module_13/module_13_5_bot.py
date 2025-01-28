
# использую aiogram 3.x !!!!!!!!!!!
import asyncio
import os.path

from aiogram import Bot, Dispatcher,  F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.command import Command, Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import  State, StatesGroup
from aiogram.fsm.context import FSMContext

api = ""  # ваш ключ
if os.path.exists("module_13_key.py"):  # это мой ключ на моем локальном компе
    from module_13_key import api  #

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
calButton = KeyboardButton(text='Калории')
infoButton = KeyboardButton(text='Информация')
kb = ReplyKeyboardMarkup(keyboard=[[calButton, infoButton]],
                         resize_keyboard=True,
                         input_field_placeholder="что хотите узнать?")




class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command("start"))
async def start(message : Message):
    print('Привет! Я бот мешающий твоему здоровью.')
    await message.answer('Привет! Я бот мешающий твоему здоровью.', reply_markup=kb)

@dp.message(F.text.lower().contains('калории'))
async def reply_calories(message: Message, state: FSMContext):
    await state.clear()
    await asyncio.sleep(2)
    await message.answer('Введите свой возраст (лет):')
    await state.set_state(UserState.age)

@dp.message(F.text.lower().contains('информация'))
async def reply_info(message: Message, state: FSMContext):
    await message.answer('(с) Виталий Шишаков 2025г. по заказу Urban University')
@dp.message(F.text, UserState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=float(message.text))
    await asyncio.sleep(2)
    await message.answer('Введите свой рост (см):')
    await state.set_state(UserState.growth)


@dp.message(F.text, UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(growth=float(message.text))
    await asyncio.sleep(2)
    await message.answer('Введите свой вес (кг):')
    await state.set_state(UserState.weight)


@dp.message(F.text, UserState.weight)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    age=data['age']
    growth=data['growth']
    weight=data['weight']
    cal = 10*weight + 6.25*growth - 5*age + 5
    await asyncio.sleep(2)
    await state.clear()
    await message.answer(f"Ваша норма калорий: {cal:.0f}ккал/день", reply_markup=kb)



@dp.message(F.text)
async def default_message(message : Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

# @dp.message()
# async def default_message(msg):
#     print(f"мы получили:{msg.text}")

# цикл обработки сообщения. вместо executor.start_polling
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
