"""
Classes for storing a hand and a played board
"""


class Hand:
    # Subclass list?
    def __init__(self):
        self.cards = []
        return


class PlayedCards:
    def __init__(self):
        # Card objects IN ORDER
        self.cards = []
        return
