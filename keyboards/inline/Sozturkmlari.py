from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

sozturkum = ['Ot', 'Sifat', 'Son', 'Olmosh', 'Ravish', 'Fe`l', 'Bog`lovchi',
             'Ko`makchi', 'Yuklama', 'Undov', 'Taqlid', 'Modal', 'Tinish belgisi']

SozTurkum = InlineKeyboardMarkup(row_width=4)

for i in sozturkum:
    tugma = InlineKeyboardButton(text=i, callback_data=i)
    SozTurkum.insert(tugma)

tasdiqlash = InlineKeyboardButton(text="✅Tasdiqlash", callback_data="tasdiqlashbtn")
teglar = InlineKeyboardButton(text="📝Teglar", callback_data='teglarbtn')
oldingi = InlineKeyboardButton(text="⬅ Oldingi", callback_data="oldingisozbtn")
keyingi = InlineKeyboardButton(text="Keyingi ➡", callback_data="keyingisozbtn")

SozTurkum.insert(teglar)
SozTurkum.insert(tasdiqlash)

SozTurkum.insert(oldingi)
SozTurkum.insert(keyingi)
