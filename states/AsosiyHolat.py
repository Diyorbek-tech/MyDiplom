from aiogram.dispatcher.filters.state import StatesGroup, State
'''
/start
Xush kelibsiz:
 if signup is false
    Ro`yhatdan o`tish
 else
    Gap taxrirlash:
        Gap:
            Marfologik:
                ot 
                sifat
                son
                ravish
                olmosh
                qo`shish+
                minus -
            Sintaksis:
                ....
                ....
                ....
                qo`shish+
                minus - bnm,.
            bekor qilish
            oldingi
            keyingi
    Men taxrirlagan gaplar
    Bazadagi gaplar
    Taxrirlashni o`rganish
 
 
 
'''

class Matnyuborish(StatesGroup):
    matnyuborish=State()

class AsosiyHolatlar(StatesGroup):
    GapTaxrirlash=State()
    MenTaxrirlaganGaplar=State()
    BazadagiGaplar=State()
    TaxrirlashniOrganish=State()
    RoyxatdanOtish=State()

class Marfologik(StatesGroup):
    Marfologik1=State()
    Marfologik2=State()
    Marfologik3=State()
    Tegberish=State()





