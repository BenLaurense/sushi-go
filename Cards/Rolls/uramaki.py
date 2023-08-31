from enum import Enum
from Cards.card_base import CardBase, CardType


class UramakiType(Enum):
    three = 3
    four = 4
    five = 5


class Nigiri(CardBase):
    def __init__(self, specific_type: UramakiType):
        super().__init__(CardType.uramaki, specific_type)
        return

    def __str__(self):
        return 'Uramaki: {} roll(s)'.format(self.specific_type.name)
