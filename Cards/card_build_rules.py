from Card_Objects.appetisers_objects import *
from Card_Objects.desserts_objects import *
from Card_Objects.nigiri_objects import *
from Card_Objects.rolls_objects import *

"""
Method that constructs cards based on their specific_type and count
(Might want this to be able to take in a config of build rules)
"""


def build_cards(card_type: CardType,
                category_count: int) -> list[CardBase]:
    # Re-enable different deck sizing!
    match card_type:
        # Nigiri
        case CardType.nigiri:
            return 4*[Nigiri(NigiriType.egg)] + 5*[Nigiri(NigiriType.salmon)] + 3*[Nigiri(NigiriType.squid)]
        # Rolls
        case CardType.maki:
            return 4*[Maki(MakiType.one)] + 5*[Maki(MakiType.two)] + 3*[Maki(MakiType.three)]
        case CardType.temaki:
            return 12*[Temaki()]
        case CardType.uramaki:
            return 4*[Uramaki(UramakiType.three), Uramaki(UramakiType.four), Uramaki(UramakiType.five)]
        # Appetisers
        case CardType.dumpling:
            return 8*[Dumpling()]
        case CardType.edamame:
            return 8*[Edamame()]
        case CardType.eel:
            return 8*[Eel()]
        case CardType.miso:
            return 8*[Miso()]
        case CardType.onigiri:
            return 2*[Onigiri(OnigiriType.triangle), Onigiri(OnigiriType.circle),
                      Onigiri(OnigiriType.square), Onigiri(OnigiriType.rectangle)]
        case CardType.sashimi:
            return 8*[Sashimi()]
        case CardType.tempura:
            return 8*[Tempura()]
        case CardType.tofu:
            return 8*[Tofu()]
        # Specials

        # Desserts
        case CardType.fruit:
            return 2*[Fruit(FruitType.pp), Fruit(FruitType.mm), Fruit(FruitType.ww)] \
                + 3*[Fruit(FruitType.pm), Fruit(FruitType.pw), Fruit(FruitType)]
        case CardType.green_tea_ice_cream:
            return 15*[GreenTeaIceCream()]
        case CardType.pudding:
            return 15*[Pudding()]
        case _:
            raise Exception("No build rule for the specified CardType!")
