from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


Homebutton=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Gap taxrirlash"),
            KeyboardButton(text="Men taxrirlagan gaplar"),
        ],
        [
            KeyboardButton(text="Bazadagi gaplar"),
            KeyboardButton(text="Taxrirlashni o`rganish"),
        ],
        [
            KeyboardButton(text="Ro`yxatdan o`tish"),
        ]
    ],resize_keyboard=True,
    one_time_keyboard=True
)