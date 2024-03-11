from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f

from kbds import reply

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник', reply_markup=reply.start_kb)


@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def echo(message: types.Message):
    await message.answer("Вот меню:")



@user_private_router.message(F.text.lower() == "о нас")
@user_private_router.message(Command('about'))
async def echo(message: types.Message):
    await message.answer("О нас")



@user_private_router.message(F.text.lower() == "варианты оплаты")
@user_private_router.message(Command('payment'))
async def echo(message: types.Message):
    await message.answer("Варианты оплаты")



@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def echo(message: types.Message):
    await message.answer("Варианты доставки")





