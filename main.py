from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from decimal import Decimal

strg = MemoryStorage()
token = Bot('6166978879:AAH6tie3OwOTBjQwfBB4BOwiUqwRhYfqNs4')
dp = Dispatcher(token)

class Get_Num(StatesGroup):
    num = State()

async def on_start(_):
    print('Бот запустился')

request_for_num = """Напишите мне десятичное число"""

@dp.message_handler(commands=['start'])
async def say_hello(msg: types.Message):
    await msg.answer('Здравствуйте! Я умею конвертировать десятичные дроби')
    await asyncio.sleep(0.5)
    await msg.answer('Напишите мне десятичную дробь чтобы я смог ее перевести в обычную')

@dp.message_handler()
async def get_a_num(msg: types.Message):
    try:
        numerator = Decimal(msg.text).as_integer_ratio()[0]
        detominator = Decimal(msg.text).as_integer_ratio()[1]
        await msg.answer(f'{numerator}/{detominator}')
    except:
        return
        
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)