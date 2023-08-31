from Cards.Card_Objects.card_base import *

"""
Classes for storing a hand and a played board
"""


class Hand:
    # This might be better subclassing list
    def __init__(self,
                 init_cards=None):
        self.cards = []
        if init_cards is not None:
            self.cards += init_cards
        return


class PlayedCards:
    # This might be better subclassing list
    def __init__(self):
        self.cards = []
        return

    def reset(self):
        # Resets the hand, leaving desserts!
        for card in self.cards:
            if card.CardType not in card_enum_dict[CardCategory.dessert]:
                self.cards.remove(card)
        return
