from enum import Enum
from Cards.card_base import CardBase, CardCategory, CardType

"""
Nigiri card specific_type - there is only one variety

Scoring rule is simple!
"""


class NigiriType(Enum):
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
        return 'Nigiri'
