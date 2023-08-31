from enum import Enum
from Cards.Card_Objects.card_base import CardBase, CardType


class MakiType(Enum):
    one = 1
    two = 2
    three = 3


class Maki(CardBase):
    def __init__(self, specific_type: MakiType):
        super().__init__(CardType.maki, specific_type)
        return

    def __str__(self):
        return 'Maki: {} roll(s)'.format(self.specific_type.name)


class Temaki(CardBase):
    def __init__(self):
        super().__init__(CardType.temaki)
        return

    def __str__(self):
        return 'Temaki'


class UramakiType(Enum):
    three = 3
    four = 4
    five = 5


class Uramaki(CardBase):
    def __init__(self, specific_type: UramakiType):
        super().__init__(CardType.uramaki, specific_type)
        return

    def __str__(self):
        return 'Uramaki: {} roll(s)'.format(self.specific_type.name)
