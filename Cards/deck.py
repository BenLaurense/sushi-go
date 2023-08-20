from Game.hand import Hand
from Game.game_parameters import default_counts
from card_base import CardType, CardCategory
from card_builder import CardBuilder
import random

"""
Deck and deck-building classes

build_deck takes a list of card types and produces a deck object
"""


class Deck:
    # Making this inherit from List might be a much better way of doing this!
    def __init__(self, card_types, category_counts=default_counts):
        self.card_types = card_types  # List of card types
        self.category_counts = category_counts
        self.cards = []  # This stores the INSTANTIATED card objects

        # Builds deck:
        self.build_deck()
        return

    """
    Build the deck from the chosen CardTypes and Counts
    """

    def build_deck(self):
        # Takes the cardtypes and constructs a deck
        self.cards = []
        for card_type in self.card_types:
            cards = CardBuilder.build(card_type, self.category_counts[card_type])
            self.cards += cards

        self.shuffle()
        return

    """
    Shuffling
    """
    def shuffle(self):
        random.shuffle(self.cards)
        return

    def append_and_shuffle(self, cards: list):
        self.cards += cards
        self.shuffle()
        return

    """
    Drawing and hand creation
    """
    def draw(self, num_cards: int) -> list:
        # Check that this doesn't cause issues
        drawn_cards = self.cards[-num_cards:]
        del self.cards[-num_cards:]
        return drawn_cards

    def deal_hands(self, num_hands: int, num_cards_per_hand: int) -> list:
        hands = []
        for i in range(num_hands):
            hand = Hand()
            hand.cards = self.draw(num_cards_per_hand)
        return hands
