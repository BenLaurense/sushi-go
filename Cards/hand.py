from Cards.Card_Objects.card_base import CardBase, CardCategory

"""
Classes for storing a hand and a played board
"""


class Hand(list[CardBase]):
    def __init__(self, init_cards=None):
        super().__init__()
        if init_cards is not None:
            self.__add__(init_cards)
        return


class PlayedCards(list[CardBase]):
    def __init__(self):
        super().__init__()
        return

    # def get_desserts(self):
    #     desserts = []
    #     for card in self.__iter__():
    #         if card.card_type not in card_enum_dict[CardCategory.dessert]:
    #             desserts.append(card)

    def reset(self, leave_desserts=True):
        # Resets the hand, leaving desserts!
        for card in self.__iter__():
            if not (leave_desserts and card.card_type in card_enum_dict[CardCategory.dessert]):
                self.remove(card)
        return
