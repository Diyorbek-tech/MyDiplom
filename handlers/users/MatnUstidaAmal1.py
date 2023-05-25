from typing import Union

import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.utils.exceptions import MessageNotModified

from keyboards.inline.menu_keyboards import categories_keyboard, subcategories_keyboard, menu_cd, \
    subcategories_keyboard2, subcategories_keyboard3, subcategories_keyboard4, subcategories_keyboard5, menukey
from loader import dp, bot

async def gapberish(index):
    filelistqilish = open("filelar/Gaplar", 'r', encoding='utf8').readlines()
    shablon = f"<b>Gap:</b><i>{filelistqilish[index - 1][2:]}</i>\n<b>{filelistqilish[index - 1][2:].split()[0]}</b>"
    return shablon



@dp.message_handler(Text(equals="Gap taxrirlash"))
async def btn1(message: Union[CallbackQuery, Message],**kwargs):
    if isinstance(message, Message):
        index = 1
        # await state.update_data({'index': index})
        gap = await gapberish(index)
        markup = await menukey()
        await message.answer(text=gap, reply_markup=markup)

    elif isinstance(message,CallbackQuery):
        callback=message
        markup1 =await menukey()
        await callback.message.edit_text(text=f"{callback.message.text.splitlines()[0]}\n\n<b>{callback.message.text.splitlines()[2]}</b>",reply_markup=markup1)




async def list_category(message: Union[CallbackQuery, Message],menu,**kwargs):
    markup = await menukey()


    if isinstance(message, CallbackQuery):
        callback = message
        gap=callback.message.text.splitlines()[0]
        soz=callback.message.text.splitlines()[2].split()[-1]
        # print(soz,type(soz))
        # print(gap,type(gap))
        index=gap.split().index(soz)+1 if soz in gap.split() else gap.split().index(gap.split()[-1])
        # print(index)
        if menu == "➕":
            try:
                index += 1
                await callback.message.edit_text(
                    text=f"{gap}\n\n<b>{' '.join(gap.split()[1:index])}</b>", reply_markup=markup)
            except MessageNotModified as ar:
                pass


        elif menu == "➖":
            try:
                if index>2:
                    index -= 1
                    await callback.message.edit_text(
                        text=f"{gap}\n\n<b>{' '.join(gap.split()[1:index])}</b>", reply_markup=markup)
            except MessageNotModified as ar:
                pass
        else:
            markup = await categories_keyboard(menu)
            await callback.message.edit_reply_markup(markup)




async def list_subcategory1(callback: CallbackQuery,menu,category, **kwargs):
    markup = await subcategories_keyboard(menu,category)
    await callback.message.edit_text(text=f"{callback.message.text.splitlines()[0]}\n\n<b>{callback.message.text.splitlines()[2]}</b>\n\n<i>{menu}: {category}</i>", reply_markup=markup)
    # await callback.message.edit_reply_markup(markup)

async def list_subcategory2(callback: CallbackQuery,menu, category, subcategory, **kwargs):
    markup = await subcategories_keyboard2(menu,category, subcategory)
    # await callback.message.edit_text(text="Mahsulot tanlang", reply_markup=markup)
    await callback.message.edit_text(text=f"{callback.message.text.splitlines()[0]}\n\n<b>{callback.message.text.splitlines()[2]}</b>\n\n<i>{menu}: {category}/{subcategory}</i>", reply_markup=markup)
    # await callback.message.edit_reply_markup(markup)

async def list_subcategory3(callback: CallbackQuery,menu, category, subcategory,subcategory2, **kwargs):
    markup = await subcategories_keyboard3(menu,category, subcategory,subcategory2)
    await callback.message.edit_text(text=f"{callback.message.text.splitlines()[0]}\n\n<b>{callback.message.text.splitlines()[2]}</b>\n\n<i>{menu}: {category}/{subcategory}/{subcategory2}</i>", reply_markup=markup)

    # await callback.message.edit_reply_markup(markup)

async def list_subcategory4(callback: CallbackQuery,menu, category, subcategory,subcategory2,item_id, **kwargs):
    markup =  subcategories_keyboard4(menu,category, subcategory,subcategory2,item_id)
    # await callback.message.edit_text(text="Mahsulot tanlang", reply_markup=markup)
    await callback.message.edit_text(text=f"{callback.message.text.splitlines()[0]}\n\n<b>{callback.message.text.splitlines()[2]}</b>\n\n<i>{menu}: {category}/{subcategory}/{subcategory2}/{item_id}</i>", reply_markup=markup)

async def list_subcategory5(callback: CallbackQuery,menu, category, subcategory,subcategory2,item_id,item_id2, **kwargs):
    markup =  subcategories_keyboard5(menu,category, subcategory,subcategory2,item_id,item_id2)
    # await callback.message.edit_text(text="Mahsulot tanlang", reply_markup=markup)
    await callback.message.edit_text(text=f"{callback.message.text.splitlines()[0]}\n\n<b>{callback.message.text.splitlines()[2]}</b>\n\n<i>{menu}: {category}/{subcategory}/{subcategory2}/{item_id}/{item_id2}</i>", reply_markup=markup)

    # await callback.message.edit_reply_markup(markup)

# Yuqoridagi barcha funksiyalar uchun yagona handler


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict,):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    menu=callback_data.get('menu')
    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    subcategory = callback_data.get("subcategory")

    subcategory2= callback_data.get("subcategory2")

    # Mahsulot ID raqami (har doim ham bo'lavermaydi)
    item_id = callback_data.get("item_id")
    item_id2 = callback_data.get("item_id2")
    print(callback_data)

    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz

    levels = {
        "0": btn1,  # Kategoriyalarni qaytaramiz
        "1": list_category,  # Kategoriyalarni qaytaramiz
        "2": list_subcategory1,  # Ost-kategoriyalarni qaytaramiz
        "3": list_subcategory2,  # Mahsulotlarni qaytaramiz
        "4": list_subcategory3,  # Mahsulotni ko'rsatamiz
        "5": list_subcategory4,  # Mahsulotni ko'rsatamiz
        "6": list_subcategory5,  # Mahsulotni ko'rsatamiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    await current_level_function(
        call,menu=menu, category=category, subcategory=subcategory,subcategory2=subcategory2, item_id=item_id,item_id2=item_id2
    )

