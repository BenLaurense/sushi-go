from Cards.cards import *
from random import shuffle


"""
Deck object and associated methods
"""


class Deck(list[Card]):
    """
    Deck object
    Stores list of Cards
    """
    def __init__(self, card_counts: dict[Card, int]):
        super().__init__()
        self.card_counts = card_counts

        self.reset()    # Initialise the deck
        return

    def reset(self):
        for card in self.card_counts:
            self += self.card_counts[card] * [card]
        shuffle(self)
        return

    def draw(self, count: int) -> list[Card]:
        if count > len(self):
            raise Exception("There are too few cards left in the deck for drawing!")
        else:
            draw = self[-count:]
            del self[-count:]
            return draw

    def deal_hands(self, num_hands: int, cards_per_hand: int) -> list[list[Card]]:
        if num_hands*cards_per_hand > len(self):
            raise Exception("There are too few cards left in the deck to deal!")
        else:
            hands: list[list[Card]] = []
            for _ in range(num_hands):
                hand = self.draw(cards_per_hand)
                hands.append(hand)
            return hands


# TODO: deck build rules
