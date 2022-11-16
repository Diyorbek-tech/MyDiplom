from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

nextback=InlineKeyboardMarkup(
    inline_keyboard=[
    [
      InlineKeyboardButton(text="🖋 Morfologik",callback_data="marfologikbtn"),
      InlineKeyboardButton(text="🖌 Sintaktik",callback_data="sintaktikbtn")
    ],

    [
      InlineKeyboardButton(text="⬅ Oldingi",callback_data="oldingibtn"),
      InlineKeyboardButton(text="Keyingi ➡",callback_data="keyingibtn")
    ]
    ]
)