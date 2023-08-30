from Game.hand import *
from card_build_rules import *
import random

"""
Deck class
 - build_deck method calls card_builder to build collection of cards of each CardType
 - Contains methods for dealing, shuffling, appending cards
"""


class Deck:
    # Making this inherit from List might be a much better way of doing this!
    def __init__(self,
                 card_type_dict: dict[CardCategory, list[CardType]],
                 category_count_dict: dict[CardCategory, list[int]]) -> None:
        self.card_type_dict = card_type_dict
        self.category_counts = category_count_dict
        self.cards = []

        # Builds deck:
        self.reset(1)
        return

    def reset(self,
              round_number: int):
        self.build_deck(round_number)
        self.shuffle()
        return

    """
    Build the deck from the chosen CardTypes and Counts
    """
    def build_deck(self,
                   round_number: int) -> None:
        # Takes card types and builds the requisite cards
        self.cards = []
        for category, card_types in self.card_type_dict.items():
            if category != CardCategory.dessert:
                for card_type in card_types:
                    count = self.category_counts[category]

                    print("outer", card_type, count)
                    cards = build_cards(card_type, count)   # Error disable
                    self.cards += cards
            else:
                # Dessert cards have changing amounts per round
                for card_type in card_types:
                    count = self.category_counts[category][round_number - 1]
                    cards = build_cards(card_type, count)
                    self.cards += cards
        return

    """
    Shuffling
    """
    def shuffle(self) -> None:
        random.shuffle(self.cards)
        return

    def append_and_shuffle(self,
                           cards: list[CardBase]) -> None:
        self.cards += cards
        self.shuffle()
        return

    """
    Drawing and hand creation
    """
    def draw(self,
             num_cards: int) -> list[CardBase]:
        if num_cards > len(self.cards):
            raise Exception("There are too few cards left in the deck for drawing!")
        else:
            drawn_cards = self.cards[-num_cards:]
            del self.cards[-num_cards:]
            return drawn_cards

    def deal_hands(self,
                   num_hands: int,
                   num_cards_per_hand: int) -> list[Hand]:
        if num_hands*num_cards_per_hand > len(self.cards):
            raise Exception("There are too few cards left in the deck to deal!")
        else:
            hands = []
            for i in range(num_hands):
                hand = Hand(self.draw(num_cards_per_hand))
                hands.append(hand)
            return hands
