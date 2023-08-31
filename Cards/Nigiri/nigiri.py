from enum import Enum
from Cards.card_base import CardBase, CardType


class NigiriType(Enum):
    # This also represents the score of the nigiri
    egg = 1
    salmon = 2
    squid = 3


class Nigiri(CardBase):
    def __init__(self, specific_type: NigiriType):
        super().__init__(CardType.nigiri, specific_type)
        return

    def __str__(self):
        return '{} Nigiri'.format(self.specific_type.name)
