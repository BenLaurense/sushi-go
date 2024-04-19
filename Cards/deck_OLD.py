import random
from Cards.card_build_rules_OLD import build_cards
from Cards.Card_Objects_OLD.card_base import CardBase, CardType, CardCategory
from Cards.hand import Hand

"""
Deck class
 - build_deck method calls card_builder to build collection of cards of each CardType
 - Contains methods for dealing, shuffling, appending cards
"""


class Deck(list[CardBase]):
    def __init__(self,
                 card_type_dict: dict[CardCategory, list[CardType]],
                 category_counts: dict[CardCategory, list[int]]) -> None:
        super().__init__()

        self.card_type_dict = card_type_dict
        self.category_counts = category_counts

        # Builds deck:
        self.reset(round_num=1)
        return

    def reset(self, round_num: int):
        self.clear() # We clear here rather than before
        self.build_deck(round_num)
        random.shuffle(self)
        return

    """
    Build the deck from the chosen CardTypes and Counts
    """
    def build_deck(self, round_num: int):
        for category, card_types in self.card_type_dict.items():
            for card_type in card_types:

                # Note we don't filter by desserts here!
                count = self.category_counts[category][round_num - 1]
                cards = build_cards(card_type, count)
                for card in cards:
                    self.append(card)
        return

    """
    Shuffling
    """
    def append_and_shuffle(self, cards: list[CardBase]):
        for card in cards:
            self.append(card)
        random.shuffle(self)
        return

    """
    Drawing and hand creation
    """
    def draw(self, num_cards: int) -> list[CardBase]:
        if num_cards > len(self):
            raise Exception("There are too few cards left in the deck for drawing!")
        else:
            drawn_cards = self[-num_cards:]
            del self[-num_cards:]
            return drawn_cards

    def deal_hands(self, num_hands: int, num_cards_per_hand: int) -> list[Hand]:
        if num_hands*num_cards_per_hand > len(self):
            raise Exception("There are too few cards left in the deck to deal!")
        else:
            hands: list[Hand] = []
            for _ in range(num_hands):
                hand = Hand(self.draw(num_cards_per_hand))
                hands.append(hand)
            return hands


if __name__ == "__main__":
    from Game.game_parameters import test_counts, test_card_types
    D = Deck(test_card_types, test_counts)
    print(D)
