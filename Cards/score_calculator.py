from Game.hand import PlayedCards
from card_base import CardType, CardBase

"""
Method for calculating score for a given card specific_type 
 - Takes in full gameboard?
"""


# This could do with a refactor
def score_cards(card_type: CardType, played_cards: PlayedCards):
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
