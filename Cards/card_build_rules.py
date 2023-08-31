from Cards.Card_Objects.nigiri_objects import *

"""
Method that constructs cards based on their specific_type and count
(Might want this to be able to take in a config of build rules)
 - Each case must ALWAYS spit out EXACTLY category_count cards
"""


def build_cards(card_type: CardType,
                category_count: int) -> list[CardBase]:
    match card_type:
        case CardType.nigiri:
            # wrong it's 4 5 3
            scaling = category_count // 3
            return (category_count - 2*scaling)*[Nigiri(NigiriType.egg)] \
                + scaling*[Nigiri(NigiriType.salmon), Nigiri(NigiriType.squid)]

        case _:
            raise Exception("No build rule for the specified CardType!")
