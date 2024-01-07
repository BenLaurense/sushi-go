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


class SimpleScorer:
    def __init__(self, gameboard: Gameboard):
        self.gameboard = gameboard
        self.scoring_function_dict = {
            CardType.nigiri: self.score_nigiri,
        }
        return

    def score(self, player):
        score = 0

        # calcs score according to scoring rules
        for card_type in self.gameboard.card_types:
            # Call individual scoring methods
            # This is where the tricky design pattern comes in
            score += self.scoring_function_dict[card_type](player)

        return score

    def score_nigiri(self, player):
        return player


if __name__ == "__main__":
    from Game.game_parameters import test_counts, test_card_types
    G = Gameboard(test_card_types, test_counts)



# def score_cards(card_type: CardType,
#                 player: int,
#                 gameboard: Gameboard,
#                 precomp_stats) -> int:
#     # Digest precomputed stats:
#     played_cards_counts = precomp_stats
#     player_played_cards = gameboard.played_cards[player]
#
#     # Main scoring rules
#     score = 0
#     match card_type:
#         case CardType.nigiri:
#             for card in player_played_cards:
#                 if card.card_type == CardType.nigiri:
#                     score += card.specific_type # Little enum trick
#
#         case CardType.maki:
#             # For each player, count maki?
#             maki_totals = []
#             for played_cards in gameboard.played_cards:
#                 player_maki_total = 0
#                 for card in played_cards:
#                     if card.card_type == CardType.maki:
#                         player_maki_total += card.specific_type # Enum trick again
#                 maki_totals.append(player_maki_total)
#             # Index of highest score is winner
#
#
#
#         case _:
#             raise Exception("No scoring rule for the specified CardType!")
#     return score
