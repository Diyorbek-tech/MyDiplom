from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
import re
from keyboards.inline.NextButtons import nextback
from keyboards.inline.Sozturkmlari import SozTurkum
from states.AsosiyHolat import AsosiyHolatlar, Matnyuborish
def createsoz(gap,index):
    sozlar=gap.split()
    return sozlar[index]

def createlist(matn):
    sentence_endings = r"[.?!]"
    matnlist = re.split(sentence_endings, matn)
    gaplist = open("filelar/Gaplar", 'a')
    gapsoni = 1
    for i in matnlist:
        if len(matnlist) > gapsoni:
            gaplist.write(f'{gapsoni}) {i.strip()}\n')
            gapsoni += 1
    gaplist.close()


async def gapberish(index, call,state):
    filelistqilish = open("filelar/Gaplar", 'r').readlines()
    shablon = f"<b>Gap:</b><i>{filelistqilish[index][2:]}</i>\n" \
              f"<b>{index+1}/{len(filelistqilish)}</b>"
    await call.message.answer(text=shablon, reply_markup=nextback)
    await state.update_data({'gap':filelistqilish[index][2:]})


@dp.message_handler(state=AsosiyHolatlar)
async def btn1(message: Message, state: FSMContext):
    malumot = await state.get_data()
    index=malumot.get('index')
    newindex=int(index)+1
    await message.answer(f"Siz gap taxlillash xolatidasiz!!!{newindex}")


# Asosiy oyna tugmalari
@dp.message_handler(Text(equals="Gap taxrirlash"))
async def btn1(message: Message, state: FSMContext):
    await AsosiyHolatlar.GapTaxrirlash.set()
    index = 1
    await state.update_data({'index':index})

    filelistqilish = open("filelar/Gaplar", 'r').readlines()
    shablon = f"<b>Gap:</b><i>{filelistqilish[index-1][2:]}</i>\n" \
              f"<b>{index}/{len(filelistqilish)}</b>"
    await message.answer(text=shablon, reply_markup=nextback)
    await state.update_data({'gap':filelistqilish[index-1][2:]})


@dp.callback_query_handler(Text(equals="marfologikbtn"),state=AsosiyHolatlar)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    st=await state.get_data()
    gap=st.get('gap')
    index=0
    await state.update_data({'indexsoz':index})
    await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, index)}</b>",reply_markup=SozTurkum)

@dp.callback_query_handler(Text(equals="oldingisozbtn"),state=AsosiyHolatlar)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    st=await state.get_data()
    gap=st.get('gap')
    index = int(st.get('indexsoz'))
    if index>0:
        index-=1
        await state.update_data({'indexsoz':index})
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, index)}</b>", reply_markup=SozTurkum)
    elif index<=0:
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, 0)}</b>", reply_markup=SozTurkum)


@dp.callback_query_handler(Text(equals="keyingisozbtn"),state=AsosiyHolatlar)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    st = await state.get_data()
    gap = st.get('gap')
    index = int(st.get('indexsoz'))
    lisstt=gap.split()
    if index <len(lisstt)-1:
        index += 1
        await state.update_data({'indexsoz':index})
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, index)}</b>", reply_markup=SozTurkum)
    elif index<=len(lisstt)-1:
        await call.message.answer(f"<i>{gap}</i>\n\n\t\t\t<b>{createsoz(gap, len(lisstt)-1)}</b>", reply_markup=SozTurkum)


@dp.callback_query_handler(Text(equals="oldingibtn"),state=AsosiyHolatlar)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    malumot = await state.get_data()
    index = int(malumot.get('index'))
    if index > 1:
        index -= 1
        await gapberish(index-1, call,state)
        await state.update_data({'index': index})
    else:
        await gapberish(0, call,state)

@dp.callback_query_handler(Text(equals="keyingibtn"),state=AsosiyHolatlar)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    filelistqilish = list(open("filelar/Gaplar", 'r').readlines())
    malumot = await state.get_data()
    index =int(malumot.get('index'))
    if index!= len(filelistqilish):
        index +=1
        await gapberish(index-1, call,state)
        await state.update_data({'index': index})
    else:
        await gapberish(len(filelistqilish) - 1, call,state)


@dp.message_handler(commands="SendText")
async def funk1(message: Message):
    await Matnyuborish.matnyuborish.set()
    await message.answer("Siz matn yuborish holatidasiz,\nbotga matn yoki (.txt) file yuboring.")


@dp.message_handler(state=Matnyuborish.matnyuborish, content_types="document")
async def funk1(message: Message, state: FSMContext):
    await message.document.download()
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    fileopen = open(file.file_path, 'r').read()
    createlist(str(fileopen))
    await message.answer("File qabul qilindi!")
    await state.finish()


@dp.message_handler(state=Matnyuborish.matnyuborish)
async def funk1(message: Message, state: FSMContext):
    matn = message.text
    createlist(matn)
    await message.answer("Matn qabul qilindi!")
    await state.finish()
