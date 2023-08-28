from Cards.card_base import *

"""
Classes for storing a hand and a played board
"""


class Hand:
    # This might be better subclassing list
    def __init__(self):
        self.cards = []
        return


class PlayedCards:
    def __init__(self):
        self.cards = []
        return

    def reset(self):
        # Resets the hand, leaving desserts!
        for card in self.cards:
            if card.CardType not in dessert_types:
                self.cards.remove(card)
        return
