from Game.gameboard import Gameboard
from Cards.Card_Objects.card_base import *

"""
Method for calculating score for a given card specific_type
(ths could do with a refactor)
 - Takes in CardType to be scored
 - Takes in PlayedCards of the scoring player
 - Takes in precomputed statistics
 - Needs to take in more stuff!
ONLY TRIGGERS AT END OF ROUND!!
"""

# TODO: implement this idea
# Scoring object (maintains internal list of partial statistics)
# Score method that scores
# Decorator construction + calc method for triggering each scoring rule indexed by enum

# A ton of auxiliary methods defining scoring for each card type


def score_cards(card_type: CardType,
                player: int,
                gameboard: Gameboard,
                precomp_stats) -> int:
    # Digest precomputed stats:
    played_cards_counts = precomp_stats
    player_played_cards = gameboard.played_cards[player]

    # Main scoring rules
    score = 0
    match card_type:
        case CardType.nigiri:
            for card in player_played_cards:
                if card.card_type == CardType.nigiri:
                    score += card.specific_type # Little enum trick

        case CardType.maki:
            # For each player, count maki?
            maki_totals = []
            for played_cards in gameboard.played_cards:
                player_maki_total = 0
                for card in played_cards:
                    if card.card_type == CardType.maki:
                        player_maki_total += card.specific_type # Enum trick again
                maki_totals.append(player_maki_total)
            # Index of highest score is winner



        case _:
            raise Exception("No scoring rule for the specified CardType!")
    return score
