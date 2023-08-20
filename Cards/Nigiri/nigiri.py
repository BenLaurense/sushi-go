from enum import Enum
from Cards.card_base import CardBase, CardCategory, CardType

"""
Nigiri card type - there is only one variety

Scoring rule is simple!
"""


class NigiriType(Enum):
    egg = 1
    salmon = 2
    squid = 3


class Nigiri(CardBase):
    def __init__(self, nigiri_type: NigiriType):
        card_category = CardCategory.nigiri
        super().__init__(CardType(card_category).nigiri)

        # Specific variables
        self.type = nigiri_type
        return

    def __str__(self):
        return 'Nigiri'

    def scoring_rule(self):
        return

# Scoring rule class should be here probably

# Builder class
