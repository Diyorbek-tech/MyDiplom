import re

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from states.AsosiyHolat import  Matnyuborish
from loader import dp, bot


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

''' Matn qabul qilish'''
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
