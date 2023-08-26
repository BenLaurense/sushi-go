from enum import Enum

"""
Base class for card objects. A card object stores:
 - The CardType of the card
 - The CardCategory fo the card
 - The ScoringRule?
"""


# There will be a nicer way of doing this! I could go full OO and have another layer of subclassing...
class CardCategory(Enum):
    nigiri = 1
    rolls = 2
    appetizers = 3
    specials = 4
    dessert = 5


class CardType(Enum):
    # Nigiri card types
    nigiri = 1
    maki = 2
    temaki = 3
    uramaki = 4

    # Rolls card types

    # etc

    # Dessert card types
    pudding = 10
    ice_cream = 11


dessert_types = [CardType.pudding, CardType.ice_cream]


class CardBase:
    def __init__(self, card_type: CardType):
        self.card_type = card_type
        return

    def __str__(self):
        raise NotImplementedError
