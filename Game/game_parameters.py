from Cards.card_base import CardCategory, CardType

"""
Default Game parameters
"""

# This needs to be some special record class, indexed by enum - another design pattern I don't know
default_card_types = {CardCategory.nigiri: [CardType.nigiri],
                      # The rest
                      }

default_counts = {CardCategory.nigiri: [12],
                  CardCategory.rolls: [12],
                  CardCategory.appetizers: [8],
                  CardCategory.special: [3],
                  CardCategory.dessert: [5, 3, 2]}

test_card_types = {CardCategory.nigiri: [CardType.nigiri]}
test_counts = {CardCategory.nigiri: [10],
               CardCategory.rolls: [0],
               CardCategory.appetizers: [0],
               CardCategory.special: [0],
               CardCategory.dessert: [0, 0, 0]}


"""
Helper method for unpacking one of these special record types into a list of card types
"""


def unpack_card_types(card_type_dict: dict[CardCategory, list[CardType]]) -> list[CardType]:
    unpacked_card_types = []
    for _, card_types in card_type_dict.items():
        unpacked_card_types += card_types
    return unpacked_card_types
