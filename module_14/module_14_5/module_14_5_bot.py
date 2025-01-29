# использую aiogram 3.x !!!!!!!!!!!
import asyncio
import os.path
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.types import (Message, ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from aiogram.types.input_file import FSInputFile
from aiogram.filters.command import Command, Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3
from crud_functions import *

api = ""  # ваш ключ
if os.path.exists("module_13_key.py"):  # это мой ключ на моем локальном компе
    from module_13_key import api  #

bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
calcButton = KeyboardButton(text='Рассчитать')
infoButton = KeyboardButton(text='Информация')
regButton = KeyboardButton(text='Регистрация')
buyButton = KeyboardButton(text='Купить')
kb = ReplyKeyboardMarkup(keyboard=[[calcButton, infoButton, regButton],[buyButton]],
                         resize_keyboard=True,
                         input_field_placeholder="что хотите узнать?")

calcIButton = InlineKeyboardButton(text='Рассчитать калории', callback_data='calories')
formulaIButton = InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')
ikb = InlineKeyboardMarkup(inline_keyboard=[[calcIButton, formulaIButton]])

# база данных продуктов
try:
    conn = sqlite3.connect('products.db')
except Exception as e:
    print(str(e))
    sys.exit(-1)


initiate_db(conn)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username=State()
    email=State()
    age=State()


@dp.message(Command("start"))
async def start(message: Message):
    print('Привет! Я бот мешающий твоему здоровью.')
    await message.answer('Привет! Я бот мешающий твоему здоровью.', reply_markup=kb)

############  users stuff ####################################
@dp.message(F.text.lower().contains('регистрация'))
async def sign_up(message: Message, state: FSMContext):
    await message.answer("Введите username (строго латиницей):")
    await state.set_state(RegistrationState.username)

@dp.message(F.text, RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    if is_included(conn,message.text):
        await message.answer("Пользователь с таким username уже существует. \nВведите другой username:")
        await state.set_state(RegistrationState.username)
        return

    await state.update_data(username=message.text)
    await asyncio.sleep(1)
    await message.answer('Введите свой e-mail:')
    await state.set_state(RegistrationState.email)

@dp.message(F.text, RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await asyncio.sleep(1)
    await message.answer('Введите свой возраст (лет):')
    await state.set_state(RegistrationState.age)

@dp.message(F.text, RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(conn, data['username'], data['email'], data['age'])
    await message.answer(f"Ну вот, теперь еще и вас в базе хранить, {data['username']} ", reply_markup=kb)
    await state.clear()

###########  product stuff ####################################
@dp.message(F.text.lower().contains('купить'))
async def get_buying_list(message: Message):
    products = get_all_products(conn)
    productButtons=[]
    for p in products:
        productButtons.append([InlineKeyboardButton(text=p['title'], callback_data='product_buying')])
    ikb2 = InlineKeyboardMarkup(inline_keyboard=productButtons)

    for p in products:
        #await  message.answer(f" {p['title']} | {p['description']} | цена: {p['price']}")
        img_name=str(p['id'])+'.jpg'
        await  message.answer_photo(FSInputFile(img_name),f" {p['title']} | {p['description']} | цена: {p['price']}")
    #     await  message.answer(p['desc'])
    await message.answer('\nВыберите продукт для покупки:', reply_markup=ikb2)

@dp.callback_query(F.data == 'product_buying')
async def best_buy(callback: CallbackQuery):
    await callback.message.answer('\nПоздравляем вас с напрасной тратой денег!\n')


###########  calories stuff ####################################
@dp.message(F.text.lower().contains('рассчитать'))
async def main_menu(message: Message):
    await message.answer('Выберете опцию:', reply_markup=ikb)


@dp.callback_query(F.data == 'calories')
async def reply_calories(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await asyncio.sleep(1)
    await callback.message.answer('Введите свой возраст (лет):')
    await state.set_state(UserState.age)


@dp.callback_query(F.data == 'formulas')
async def reply_formula(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Формула Миффлина-Сан Жеора:')
    await callback.message.answer('calories (kkal) = \n10 * weight (kg)  + 6.25 * growth (cm) - 5 * age (years) + 5')


@dp.message(F.text.lower().contains('информация'))
async def reply_info(message: Message, state: FSMContext):
    await message.answer('(с) Виталий Шишаков 2025г. по заказу Urban University')


@dp.message(F.text, UserState.age)
async def set_age(message: Message, state: FSMContext):
    await state.update_data(age=float(message.text))
    await asyncio.sleep(1)
    await message.answer('Введите свой рост (см):')
    await state.set_state(UserState.growth)


@dp.message(F.text, UserState.growth)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(growth=float(message.text))
    await asyncio.sleep(1)
    await message.answer('Введите свой вес (кг):')
    await state.set_state(UserState.weight)


@dp.message(F.text, UserState.weight)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    cal = 10 * weight + 6.25 * growth - 5 * age + 5
    await asyncio.sleep(1)
    await state.clear()
    await message.answer(f"Ваша норма калорий: {cal:.0f}ккал/день", reply_markup=kb)


@dp.message(F.text)
async def default_message(message: Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')



# цикл обработки сообщения. вместо executor.start_polling
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
