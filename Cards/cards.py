from enum import Enum


"""
Enums holding card
There will be a better design pattern here (hierarchical enums)
"""


class Card(Enum):
    def get_type(self):
        conversion = {
            Card.egg_nigiri: CardType.nigiri,
            Card.salmon_nigiri: CardType.nigiri,
            Card.squid_nigiri: CardType.nigiri,
            Card.one_maki: CardType.maki,
            Card.two_maki: CardType.maki,
            Card.three_maki: CardType.maki,
            Card.temaki: CardType.temaki,
            # Card.one_uramaki: CardType.uramaki,
            # Card.two_uramaki: CardType.uramaki,
            # Card.three_uramaki: CardType.uramaki,
            # Card.four_uramaki: CardType.uramaki,
            # Card.five_uramaki: CardType.uramaki,
            Card.dumpling: CardType.dumpling,
            Card.eel: CardType.eel,
            Card.circle_onigiri: CardType.onigiri,
            Card.triangle_onigiri: CardType.onigiri,
            Card.square_onigiri: CardType.onigiri,
            Card.rectangle_onigiri: CardType.onigiri,
            Card.sashimi: CardType.sashimi,
            Card.tempura: CardType.tempura,
            Card.tofu: CardType.tofu,
        }
        return conversion[self]

    egg_nigiri = 1
    salmon_nigiri = 2
    squid_nigiri = 3

    one_maki = 4
    two_maki = 5
    three_maki = 6
    temaki = 7
    # one_uramaki = 8
    # two_uramaki = 9
    # three_uramaki = 10
    # four_uramaki = 11
    # five_uramaki = 12

    dumpling = 13
    # edamame = 14
    eel = 15
    circle_onigiri = 16
    triangle_onigiri = 17
    square_onigiri = 18
    rectangle_onigiri = 19
    # miso = 20
    sashimi = 21
    tempura = 22
    tofu = 23


class CardType(Enum):
    def get_category(self):
        conversion = {
            CardType.nigiri: CardCategory.nigiri,
            CardType.maki: CardCategory.rolls,
            CardType.temaki: CardCategory.rolls,
            CardType.uramaki: CardCategory.rolls,
            CardType.dumpling: CardCategory.appetisers,
            CardType.eel: CardCategory.appetisers,
            CardType.onigiri: CardCategory.appetisers,
            CardType.sashimi: CardCategory.appetisers,
            CardType.tempura: CardCategory.appetisers,
            CardType.tofu: CardCategory.appetisers,
        }
        return conversion[self]

    nigiri = 1
    maki = 2
    temaki = 3
    uramaki = 4
    dumpling = 5
    # edamame = 6
    eel = 7
    onigiri = 8
    # miso = 9
    sashimi = 10
    tempura = 11
    tofu = 12


class CardCategory(Enum):
    nigiri = 1
    rolls = 2
    appetisers = 3
    specials = 4
    dessert = 5


def get_card_types(params: dict[Card, int]):
    card_types = set()
    for card in params:
        card_types.add(card.get_type())
    return list(card_types)
