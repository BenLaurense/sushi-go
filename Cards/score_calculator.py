from Game.hand import *
from card_base import *
from Game.gameboard import Gameboard

"""
Method for calculating score for a given card specific_type 
(ths could do with a refactor)
 - Takes in CardType to be scored
 - Tales in PlayedCards of the scoring player
 - Needs to take in more stuff!
"""


def score_cards(card_type: CardType,
                player: int,
                gameboard: Gameboard,
                precomp_stats) -> int:
    # Digest precomputed stats:
    played_cards_counts = precomp_stats

    # Main scoring rules
    score = 0
    match card_type:
        case CardType.nigiri:
            player_played_cards = gameboard.played_cards[player]
            for card in player_played_cards:
                if card.card_type == CardType.nigiri:
                    score += card.specific_type # Little enum trick

        case _:
            raise Exception("No scoring rule for the specified CardType!")
    return score
