from Game.hand import *
from card_base import *

"""
Method for calculating score for a given card specific_type 
(ths could do with a refactor)
 - Takes in CardType to be scored
 - Tales in PlayedCards of the scoring player
 - Needs to take in more stuff!
"""


def score_cards(card_type: CardType,
                played_cards: PlayedCards) -> int:
    score = 0
    match card_type:
        case CardType.nigiri:
            # Nigiri scoring rule
            for card in played_cards.cards:
                if card.card_type == CardType.nigiri:
                    score += card.specific_type # Little hack

        case _:
            raise Exception("No scoring rule for the specified CardType!")
    return score
