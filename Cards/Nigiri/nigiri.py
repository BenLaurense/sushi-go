from enum import Enum
from Cards.card_base import CardBase, CardCategory, CardType


class NigiriType(Enum):
    # This also represents the score of the nigiri
    egg = 1
    salmon = 2
    squid = 3


class Nigiri(CardBase):
    def __init__(self, nigiri_type: NigiriType):
        super().__init__(CardType.nigiri)

        # Specific variables
        self.specific_type = nigiri_type
        return

    def __str__(self):
        return '{} Nigiri'.format(self.specific_type)
