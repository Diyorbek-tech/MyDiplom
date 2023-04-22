import json

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.AsosiyHolat import AsosiyHolatlar, Marfologik

with open("data/Morfologik_buttons.json") as json_file:
    data = json.load(json_file)

marfo_btn1 = InlineKeyboardMarkup(row_width=4)
for i in data:
    tugma = InlineKeyboardButton(text=i, callback_data=i)
    marfo_btn1.insert(tugma)
oldingi = InlineKeyboardButton(text="⬅ Oldingi", callback_data="oldingibtn")
marfo_btn1.insert(oldingi)
'''
3 4 ot
2 sifat
2 son
2 olmosh
2 ravish
4 2 fel
2 bog`lovchi
0 komakchi
1 yuklama
1 undov
1 taqlid
0 modal


'''


async def tegqaytar(btn):
    print(btn)
    await Marfologik.Marfologik1.set()
    return btn


async def marfodef1(callback):
    if callback == "Ko'makchi" or callback == "Modal":
        await tegqaytar(data[callback])
        return marfo_btn1
    else:
        marfo_btn2 = InlineKeyboardMarkup(row_width=3)
        for i in data[callback]:
            tugma = InlineKeyboardButton(text=i, callback_data=i)
            marfo_btn2.insert(tugma)
        oldingi = InlineKeyboardButton(text="⬅ Oldingi", callback_data="oldingibtn")
        marfo_btn2.insert(oldingi)
        return marfo_btn2


async def marfodef2(callback, item):
    if item == "Yuklama" or item == "Undov" or item == "Taqlid":
        await tegqaytar(data[item][callback])
        return marfo_btn1
    else:
        marfo_btn3 = InlineKeyboardMarkup(row_width=3)
        for j in data[item][callback]:
            tugma = InlineKeyboardButton(text=j, callback_data=j)
            marfo_btn3.insert(tugma)
        oldingi = InlineKeyboardButton(text="⬅ Oldingi", callback_data="oldingibtn")
        marfo_btn3.insert(oldingi)
        return marfo_btn3


async def marfodef3(callback, item, item2):
    if item == "Sifat" or \
            item == "Son" or \
            item == "Olmosh" or \
            item == "Ravish" or \
            item == "Bog'lovchi":
        await tegqaytar(data[item][item2][callback])
        return marfo_btn1
    else:
        marfo_btn4 = InlineKeyboardMarkup(row_width=3)
        for j in data[item][item2][callback]:
            tugma = InlineKeyboardButton(text=j, callback_data=j)
            marfo_btn4.insert(tugma)
        teglar = InlineKeyboardButton(text="📝Teglar", callback_data='teglarbtn')
        oldingi = InlineKeyboardButton(text="⬅ Oldingi", callback_data="oldingibtn")
        marfo_btn4.insert(teglar)
        marfo_btn4.insert(oldingi)
        return marfo_btn4


def marfodef4(callback, item, item2, item3):
    marfo_btn5 = InlineKeyboardMarkup(row_width=3)
    for j in data[item][item2][item3][callback]:
        tugma = InlineKeyboardButton(text=j, callback_data=j)
        marfo_btn5.insert(tugma)
    teglar = InlineKeyboardButton(text="📝Teglar", callback_data='teglarbtn')
    oldingi = InlineKeyboardButton(text="⬅ Oldingi", callback_data="oldingibtn")
    marfo_btn5.insert(teglar)
    marfo_btn5.insert(oldingi)
    return marfo_btn5
