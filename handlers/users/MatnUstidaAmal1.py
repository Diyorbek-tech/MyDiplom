from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
import re
from keyboards.inline.NextButtons import nextback
from keyboards.inline.Sozturkmlari import SozTurkum
from keyboards.inline.morfologik_btn import marfo_btn1, marfodef1, marfodef2, marfodef3
from states.AsosiyHolat import Marfologik, Matnyuborish, AsosiyHolatlar


def createsoz(gap, index):
    sozlar = gap.split()
    return sozlar[index]


async def gapberish(index, state):
    filelistqilish = open("filelar/Gaplar", 'r', encoding='utf8').readlines()
    shablon = f"<b>Gap:</b><i>{filelistqilish[index - 1][2:]}</i>\n" \
              f"<b>{index}/{len(filelistqilish)}</b>"
    await state.update_data({'gap': filelistqilish[index - 1][2:]})
    return shablon


# Asosiy oyna tugmalari
@dp.message_handler(Text(equals="Gap taxrirlash"))
async def btn1(message: Message, state: FSMContext):
    await AsosiyHolatlar.GapTaxrirlash.set()
    index = 1
    await state.update_data({'index': index})
    gap = await gapberish(index, state)
    await message.answer(text=gap, reply_markup=nextback)


@dp.callback_query_handler(Text(equals="marfologikbtn"), state=AsosiyHolatlar.GapTaxrirlash)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Marfologik.Marfologik1.set()
    index_soz = 0
    gaplar = await state.get_data()
    # gap = gaplar.get('gap')
    await call.message.answer(createsoz(gaplar.get('gap'), index_soz), reply_markup=marfo_btn1)
    # await bot.pin_chat_message(chat_id=call.message.from_user.id,message_id=call.message.message_id)
    await state.update_data({'soz': createsoz(gaplar.get('gap'), index_soz)})


@dp.callback_query_handler(Text(equals="oldingibtn"), state=Marfologik.Marfologik1)
async def deff1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await AsosiyHolatlar.GapTaxrirlash.set()
    gaplar = await state.get_data()
    gap = await gapberish(gaplar.get('index'), state)
    await call.message.answer(gap, reply_markup=nextback)


@dp.callback_query_handler(state=Marfologik.Marfologik1)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data({'item': call.data})
    await Marfologik.Marfologik2.set()
    gaplar = await state.get_data()

    rm = await marfodef1(call.data)
    await call.message.answer(gaplar.get('soz'), reply_markup=rm)


@dp.callback_query_handler(Text(equals="oldingibtn"), state=Marfologik.Marfologik2)
async def deff1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await Marfologik.Marfologik1.set()
    gaplar = await state.get_data()
    rm = marfo_btn1
    await call.message.answer(gaplar.get('soz'), reply_markup=rm)


@dp.callback_query_handler(state=Marfologik.Marfologik2)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data({'item2': call.data})
    await Marfologik.Marfologik3.set()
    gaplar = await state.get_data()
    item = gaplar.get('item')
    rm = await marfodef2(call.data, item)
    await call.message.answer(gaplar.get('soz'), reply_markup=rm)


@dp.callback_query_handler(Text(equals="oldingibtn"), state=Marfologik.Marfologik3)
async def deff1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    st = await state.get_data()
    item = st.get('item')
    await Marfologik.Marfologik2.set()
    gaplar = await state.get_data()
    rm = await marfodef1(item)
    await call.message.answer(gaplar.get('soz'), reply_markup=rm)


@dp.callback_query_handler(state=Marfologik.Marfologik3)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    st = await state.get_data()
    item = st.get('item')
    item2 = st.get('item2')
    await Marfologik.Tegberish.set()
    gaplar = await state.get_data()
    rm = await marfodef3(call.data, item, item2)
    await call.message.answer(gaplar.get('soz'), reply_markup=rm)


@dp.callback_query_handler(Text(equals="oldingibtn"), state=AsosiyHolatlar.GapTaxrirlash)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    gaplar = await state.get_data()
    gap = await gapberish(int(gaplar.get('index')) - 1 if int(gaplar.get('index')) > 1 else int(gaplar.get('index')),
                          state)
    await call.message.answer(gap, reply_markup=nextback)
    if int(gaplar.get('index')) > 1:
        await state.update_data({'index': int(gaplar.get('index')) - 1})


@dp.callback_query_handler(Text(equals="keyingibtn"), state=AsosiyHolatlar.GapTaxrirlash)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    filelistqilish = open("filelar/Gaplar", 'r').readlines()
    gaplar = await state.get_data()
    gap = await gapberish(
        int(gaplar.get('index')) + 1 if int(gaplar.get('index')) < len(filelistqilish) else int(gaplar.get('index')),
        state)
    await call.message.answer(gap, reply_markup=nextback)
    if int(gaplar.get('index')) < len(filelistqilish):
        await state.update_data({'index': int(gaplar.get('index')) + 1})


@dp.callback_query_handler(Text(equals="oldingisozbtn"), state=AsosiyHolatlar)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    st = await state.get_data()
    gap = st.get('gap')
    index = int(st.get('indexsoz'))
    if index > 0:
        index -= 1
        await state.update_data({'indexsoz': index})
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, index)}</b>", reply_markup=SozTurkum)
    elif index <= 0:
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, 0)}</b>", reply_markup=SozTurkum)


@dp.callback_query_handler(Text(equals="keyingisozbtn"), state=AsosiyHolatlar)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    st = await state.get_data()
    gap = st.get('gap')
    index = int(st.get('indexsoz'))
    lisstt = gap.split()
    if index < len(lisstt) - 1:
        index += 1
        await state.update_data({'indexsoz': index})
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, index)}</b>", reply_markup=SozTurkum)
    elif index <= len(lisstt) - 1:
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, len(lisstt) - 1)}</b>",
                                  reply_markup=SozTurkum)





