from enum import Enum
from Cards.card_base import CardBase, CardType


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
