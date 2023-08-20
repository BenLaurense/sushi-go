from enum import Enum

"""
Base class for card objects. A card object stores:
 - The scoring rule for that given card type is stored in the card object
"""


class CardCategory(Enum):
    nigiri = 1
    rolls = 2
    appetizers = 3
    specials = 4
    dessert = 5


# There will be a nicer way of doing this! I could go full OO and have another layer of subclassing...
class CardType(Enum):
    def __init__(self, category: CardCategory):
        self.card_category = category
    nigiri = 1 # does this work??
    maki = 2
    temaki = 3
    uramaki = 4


class CardBase:
    def __init__(self, card_type: CardType):
        self.card_type = card_type
        return

    def __str__(self):
        raise NotImplementedError

    def scoring_rule(self):
        # Virtual method for scoring rule
        raise NotImplementedError
