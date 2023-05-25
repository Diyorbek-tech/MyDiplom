import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.Homebuttons import Homebutton
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # try:
    #     user = await db.add_user(telegram_id=message.from_user.id,
    #                              full_name=message.from_user.full_name,
    #                              username=message.from_user.username)
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Xush kelibsiz!",reply_markup=Homebutton)
