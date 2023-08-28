from Nigiri.nigiri import *

"""
Method that constructs cards based on their specific_type and count
(Might want this to be able to take in a config of build rules)
 - Each case must ALWAYS spit out exactly category_count cards
"""


def build_cards(card_type: CardType,
                category_count: int) -> list[CardBase]:
    match card_type:
        case CardType.nigiri:
            scaling = category_count // 3
            return (category_count - 2*scaling)*[Nigiri(NigiriType.egg)] \
                + scaling*[Nigiri(NigiriType.salmon), Nigiri(NigiriType.squid)]

        case _:
            raise Exception("No build rule for the specified CardType!")
