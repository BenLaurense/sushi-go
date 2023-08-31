from enum import Enum
from Cards.Card_Objects.card_base import CardBase, CardType


class FruitType(Enum):
    pp = 1
    mm = 2
    ww = 3
    pm = 4
    pw = 5
    mw = 6


class Fruit(CardBase):
    def __init__(self, specific_type=FruitType):
        super().__init__(CardType.fruit, specific_type)
        return

    def __str__(self):
        return 'Something lol'


class GreenTeaIceCream(CardBase):
    def __init__(self):
        super().__init__(CardType.green_tea_ice_cream)
        return

    def __str__(self):
        return 'Green Tea Ice Cream'


class Pudding(CardBase):
    def __init__(self):
        super().__init__(CardType.pudding)
        return

    def __str__(self):
        return 'Pudding'
