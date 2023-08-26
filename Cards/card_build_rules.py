from card_base import CardCategory, CardType
from Nigiri.nigiri import Nigiri, NigiriType

"""
Method that constructs cards based on their specific_type and count
Might want this to be able to take in a config of build rules
"""


def build_cards(card_type: CardType, category_count: int):
    match card_type:
        case CardType.nigiri:
            # Return a list of cards of the correct format
            # For nigiri, standardised format
            standard_unit = [Nigiri(NigiriType.egg), Nigiri(NigiriType.salmon), Nigiri(NigiriType.squid)]
            return (category_count // 3) * standard_unit
        case _:
            raise Exception("No build rule for the specified CardType!")
