import json

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

# Turli tugmalar uchun CallbackData-obyektlarni yaratib olamiz
menu_cd = CallbackData("show_menu", "level", "menu", "category", "subcategory", "subcategory2", "item_id", "item_id2",
                       "teg")

with open("data/Morfologik_buttons.json") as json_file:
    data = json.load(json_file)
with open("data/Sintaktik_teglar_buttons.json") as json_file:
    data2 = json.load(json_file)


# Quyidagi funksiya yordamida menyudagi har bir element uchun calbback data yaratib olinadi
# Agar mahsulot kategoriyasi, ost-kategoriyasi va id raqami berilmagan bo'lsa 0 ga teng bo'ladi
def make_callback_data(level, menu="0", category="0", subcategory="0", subcategory2="0", item_id="0", item_id2="0",
                       teg="0"):
    return menu_cd.new(
        level=level, menu=menu, category=category, subcategory=subcategory, subcategory2=subcategory2,
        item_id=item_id, item_id2=item_id2, teg=teg
    )


# Bizning menu 3 qavat (LEVEL) dan iborat
# 0 - Kategoriyalar
# 1 - Ost-kategoriyalar
# 2 - Mahsulotlar
# 3 - Yagona mahsulot


# Kategoriyalar uchun keyboardyasab olamiz
async def menukey():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)
    for i in ["Marfologik", "Sintaktik", "➕", "➖"]:
        callback_data = make_callback_data(
            level=CURRENT_LEVEL + 1, menu=i
        )
        tugma = InlineKeyboardButton(text=i, callback_data=callback_data)
        markup.insert(tugma)
    return markup


async def categories_keyboard(menu):
    # Eng yuqori 0-qavat ekanini ko'rsatamiz
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=4)

    if menu == "Marfologik":
        for i in data:
            callback_data = make_callback_data(
                level=CURRENT_LEVEL + 1, menu=menu, category=i
            )
            tugma = InlineKeyboardButton(text=i, callback_data=callback_data)
            markup.insert(tugma)
    elif menu == "Sintaktik":
        for i in data2:
            callback_data = make_callback_data(
                level=CURRENT_LEVEL + 1, menu=menu, category=i
            )
            tugma = InlineKeyboardButton(text=i, callback_data=callback_data)
            markup.insert(tugma)
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)
        )
    )
    return markup


async def subcategories_keyboard(menu, category):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=3)
    if menu == "Marfologik":
        if category == "Ko'makchi" or category == "Modal":
            print(data[category])
        else:
            for i in data[category]:
                callback_data = make_callback_data(
                    level=CURRENT_LEVEL + 1,
                    menu=menu,
                    category=category,
                    subcategory=i,
                )
                tugma = InlineKeyboardButton(text=i, callback_data=callback_data)
                markup.insert(tugma)

    elif menu == "Sintaktik":
        for i in data2[category]:
            callback_data = make_callback_data(
                level=CURRENT_LEVEL + 1,
                menu=menu,
                category=category,
                subcategory=i,
            )
            tugma = InlineKeyboardButton(text=i, callback_data=callback_data)
            markup.insert(tugma)

    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga", callback_data=make_callback_data(level=CURRENT_LEVEL - 1, menu=menu)
        )
    )
    return markup


async def subcategories_keyboard2(menu, category, subcategory):
    CURRENT_LEVEL = 3

    markup = InlineKeyboardMarkup(row_width=3)
    if menu == "Marfologik":
        if category == "Taqlid" or category == "Undov" or category == "Yuklama":
            # print(data[category][subcategory])
            CURRENT_LEVEL = 0
            markup.row(
                InlineKeyboardButton(
                    text="So`z teglandi tasdiqlash ✅",
                    callback_data=make_callback_data(
                        level=CURRENT_LEVEL,teg=f"{data[category][subcategory]}"
                    ),

                )
            )
        else:
            for j in data[category][subcategory]:
                callback_data = make_callback_data(
                    level=CURRENT_LEVEL + 1,
                    menu=menu,
                    category=category,
                    subcategory=subcategory,
                    subcategory2=j,
                )
                tugma = InlineKeyboardButton(text=j, callback_data=callback_data)
                markup.insert(tugma)

    elif menu == "Sintaktik":
        if subcategory == "Ega" or subcategory == "Undalma" or subcategory == "Kiritma" or subcategory == "Keyingi so'z bilan birga":
            print(data2[category][subcategory])
        else:
            for j in data2[category][subcategory]:
                callback_data = make_callback_data(
                    level=CURRENT_LEVEL + 1,
                    menu=menu,
                    category=category,
                    subcategory=subcategory,
                    subcategory2=j,
                )
                tugma = InlineKeyboardButton(text=j, callback_data=callback_data)
                markup.insert(tugma)
                markup.row(
                    InlineKeyboardButton(
                        text="⬅️Ortga",
                        callback_data=make_callback_data(
                            level=CURRENT_LEVEL - 1, menu=menu, category=category
                        ),
                    )
                )

    # Ortga qaytish tugmasi

    return markup


async def subcategories_keyboard3(menu, category, subcategory, subcategory2):
    CURRENT_LEVEL = 4

    markup = InlineKeyboardMarkup(row_width=3)

    if menu == "Marfologik":
        if category == "Sifat" or category == "Son" or category == "Olmosh" or category == "Ravish" or category == "Bog'lovchi" or subcategory == "Harakat nomi":
            print(data[category][subcategory][subcategory2])
        else:
            print(subcategory2)
            for j in data[category][subcategory][subcategory2]:
                callback_data = make_callback_data(
                    level=CURRENT_LEVEL + 1,
                    menu=menu,
                    category=category,
                    subcategory=subcategory,
                    subcategory2=subcategory2,
                    item_id=j
                )
                tugma = InlineKeyboardButton(text=j, callback_data=callback_data)
                markup.insert(tugma)

    elif menu == "Sintaktik":
        for j in data2[category][subcategory][subcategory2]:
            callback_data = make_callback_data(
                level=CURRENT_LEVEL + 1,
                menu=menu,
                category=category,
                subcategory=subcategory,
                subcategory2=subcategory2,
                item_id=j
            )
            tugma = InlineKeyboardButton(text=j, callback_data=callback_data)
            markup.insert(tugma)

    # Ortga qaytish tugmasi
    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, menu=menu, category=category, subcategory=subcategory
            ),
        )
    )
    return markup


def subcategories_keyboard4(menu, category, subcategory, subcategory2, item_id):
    CURRENT_LEVEL = 5
    markup = InlineKeyboardMarkup(row_width=1)

    if isinstance(data[category][subcategory][subcategory2][item_id], str):
        print(data[category][subcategory][subcategory2][item_id])

    else:
        for j in data[category][subcategory][subcategory2][item_id]:
            callback_data = make_callback_data(
                level=CURRENT_LEVEL + 1,
                menu=menu,
                category=category,
                subcategory=subcategory,
                subcategory2=subcategory2,
                item_id=item_id,
                item_id2=j
            )
            tugma = InlineKeyboardButton(text=j, callback_data=callback_data)
            markup.insert(tugma)
        # markup.row(
        #     InlineKeyboardButton(
        #         text="⬅️Ortga",
        #         callback_data=make_callback_data(
        #             level=CURRENT_LEVEL - 1,menu=menu, category=category, subcategory=subcategory, subcategory2=subcategory2,item_id=item_id
        #         ),
        #     )
        # )

    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, menu=menu, category=category, subcategory=subcategory,
                subcategory2=subcategory2
            ),
        )
    )

    return markup


def subcategories_keyboard5(menu, category, subcategory, subcategory2, item_id, item_id2):
    CURRENT_LEVEL = 6
    markup = InlineKeyboardMarkup(row_width=2)

    markup.row(
        InlineKeyboardButton(
            text="⬅️Ortga",
            callback_data=make_callback_data(
                level=CURRENT_LEVEL - 1, menu=menu, category=category, subcategory=subcategory,
                subcategory2=subcategory2,
                item_id=item_id
            ),
        )
    )

    print(data[category][subcategory][subcategory2][item_id][item_id2])

    return markup
