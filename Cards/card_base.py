from enum import Enum

"""
Base class for card objects. A card object stores:
 - The CardType of the card
 - The CardCategory fo the card
"""


# There will be a nicer way of doing this! I could go full OO and have another layer of subclassing...
# There might be an Enum Dict class?
class CardCategory(Enum):
    nigiri = 1
    rolls = 2
    appetizers = 3
    special = 4
    dessert = 5


class CardType(Enum):
    # Nigiri
    nigiri = 1

    # Rolls
    maki = 2
    temaki = 3
    uramaki = 4

    # Appetizers
    dumpling = 5
    edamame = 6
    eel = 7
    miso = 8
    onigiri = 9
    sashimi = 10
    tempura = 11
    tofu = 12

    # Special
    chopsticks = 13
    menu = 14
    soy_sauce = 15
    special_order = 16
    spoon = 17
    takeout_box = 18
    tea = 19
    wasabi = 20

    # Dessert
    fruit = 21
    green_tea_ice_cream = 22
    pudding = 23


card_enum_dict = {CardCategory.nigiri: [CardType.nigiri],
                  CardCategory.rolls: [CardType.maki, CardType.temaki, CardType.uramaki],
                  CardCategory.appetizers: [CardType.dumpling, CardType.edamame, CardType.eel,
                                            CardType.miso, CardType.onigiri, CardType.sashimi,
                                            CardType.tempura, CardType.tofu],
                  CardCategory.special: [CardType.chopsticks, CardType.menu, CardType.soy_sauce,
                                         CardType.special_order, CardType.spoon, CardType.takeout_box,
                                         CardType.tea, CardType.wasabi],
                  CardCategory.dessert: [CardType.fruit, CardType.green_tea_ice_cream, CardType.pudding]}


class CardBase:
    def __init__(self,
                 card_type: CardType,
                 specific_type=None):
        self.card_type = card_type
        self.specific_type = specific_type
        return

    def __str__(self):
        raise NotImplementedError
