from Game.hand import Hand
from Game.game_parameters import default_counts
from card_base import CardType, CardCategory, dessert_types
from card_build_rules import build_cards
import random

"""
Deck class
 - build_deck method calls card_builder to build collection of cards of each CardType
"""


class Deck:
    # Making this inherit from List might be a much better way of doing this!
    def __init__(self,
                 card_type_dict: dict[CardCategory, list[CardType]],
                 category_counts: dict[CardCategory, list[int]]):
        self.card_type_dict = card_type_dict  # List of card types
        self.category_counts = category_counts
        self.cards = []  # This stores the INSTANTIATED card objects

        # Builds deck:
        self.reset()
        return

    def reset(self, round=1):
        self.build_deck(round)
        return

    """
    Build the deck from the chosen CardTypes and Counts
    """
    def build_deck(self,
                   round: int):
        # Takes the cardtypes and constructs a deck. Special rule for desserts
        self.cards = []
        for card_type in self.card_types:
            if card_type not in dessert_types:
                count = self.category_counts[card_type]
            else:
                count = self.category_counts[card_type][round - 1]

            cards = build_cards(card_type, count)
            self.cards += cards

        self.shuffle()
        return

    def build_deck_2(self, round:int):

        return

    """
    Shuffling
    """
    def shuffle(self):
        random.shuffle(self.cards)
        return

    def append(self, cards: list):
        self.cards += cards
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


# """
# Helper methods
# """
#
#
# def unpack_card_types(card_type_dict: dict[CardCategory, list[CardType]]):
#     # This should be a common operation
#     card_types = []
#     for _, value in card_type_dict.items():
#         card_types += value
#     return card_types
