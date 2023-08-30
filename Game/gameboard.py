from game_parameters import *
from Cards.deck import *
from numpy import argmax
from collections import Counter


"""
Gameboard class - object which tracks game global variables, and has methods for playing turns
"""


class Gameboard:
    def __init__(self,
                 card_type_dict: dict[CardCategory, list[CardType]],
                 card_category_counts: dict[CardCategory, list[int]]) -> None:
        # Global game vars:
        self.num_players = 2
        self.num_rounds = 3
        self.hand_size = 2

        self.card_type_dict = card_type_dict # Maybe not needed!
        self.card_types = unpack_card_types(card_type_dict)

        # Internal vars:
        self.deck = Deck(card_type_dict, card_category_counts)  # Should be Deck object with DEFAULT PARAMS
        self.hands = self.deck.deal_hands(self.num_players, self.hand_size)
        self.played_cards = [PlayedCards()]*self.num_players

        self.turn_timer = self.hand_size # recalc this?

        # Round-specific vars:
        return

    """
    Game loop
    """
    def game_loop(self) -> None:
        print('Starting game of {} rounds'.format(self.num_rounds))
        for round_num in range(self.num_rounds):
            scores = self.play_round(round_num)

        # Final round_num has special scoring, but this is done withing play_round

        # End the game:
        print('Final scores are {}'.format(scores))
        winner = argmax(scores) + 1
        print('Winner is Player {}!'.format(winner))

        play_again = input('Play another game? Y/N')
        while play_again not in ['Y', 'N']:
            play_again = input('Play another game? Y/N')
        if play_again == 'Y':
            # Reset the gamestate
            exit('Implement me lol')
        else:
            exit('Game over')

    """
    Functions for playing rounds/turns within that round
    """
    def play_round(self,
                   round_num: int) -> list[int]:
        # Plays round, calcs scores, and resets deck at the end
        if round_num < self.num_rounds - 1:
            print('Round {} starting'.format(round_num))
        else:
            print('Round {} starting. Desserts will count after this round'.format(round_num))

        # Loop through turns within the round
        while self.turn_timer > 0:
            self.play_turn()

        # Show scores:
        include_dessert = (round_num == self.num_rounds - 1)
        scores = self.calc_scores(include_dessert)
        print('Scores are {}'.format(scores))

        # End of round:
        # Reset the board (and consider desserts):
        self.deck.reset(round_num)
        self.hands = self.deck.deal_hands(self.num_players, self.hand_size)
        for played_cards in self.played_cards:
            played_cards.reset()
        self.turn_timer = self.hand_size

        print('Round {} over'.format(round_num))
        return scores

    def play_turn(self) -> None:
        # Collects player input for their round and changes gameboard accordingly
        # Show info:
        self.show_hands()
        self.show_played_cards()

        # Get player inputs:
        moves = []
        for player in range(self.num_players):
            move = input('Enter valid move index') # Integer index for now
            moves.append(move)

        # Reveal and execute moves:
        for player in range(self.num_players):
            played_card = self.hands[player].cards[moves[player]]
            print('Player {} played {}'.format(player + 1, played_card))
            # Trigger any special card effects?
            self.hands[player].cards.remove(played_card)
            self.played_cards[player].cards.append(played_card)

        # Perform special effects according to execution order
        ### Not needed yet

        # Increment turn timer:
        self.turn_timer -= 1

        # Cycle the hands:
        self.hands = cycle_hands(self.hands)
        return

    """
    Functions for calculating score
    """
    # This could do with a refactor. Suggestion: This functions requests basic statistics to be precomputed
    # e.g. counts of each cardtype
    # These are fed along with the whole Gameboard object into a scoring function
    # This seems cleanest? Some of the scoring rules don't need this though.

    # Precompute EVERYTHING? A partial score object that updates each turn?
    # def calc_scores(self,
    #                 include_dessert=False) -> list[int]:
    #     scores = []
    #     for player in range(self.num_players):
    #         score = 0
    #         for category, card_types in self.card_type_dict.items():
    #             if category != CardCategory.dessert or include_dessert:
    #                 for card_type in card_types:
    #                     score += score_cards(card_type, self.played_cards[player])
    #     return scores

    def calc_scores(self,
                    include_dessert=False) -> list[int]:
        from Cards.score_calculator import score_cards # Circular import avoiding

        # Precompute some statistics?
        def played_cards_counts(played_cards):
            # Spit out one of those special record classes I need to make?
            # Or an array?
            out = []
            for player_played_cards in played_cards:
                type_counts = Counter(player_played_cards)
                out.append(type_counts)
            return out

        stat1 = played_cards_counts(self.played_cards)

        # Main loop
        scores = []
        for player in range(self.num_players):
            for card_type in self.card_types:
                scores[player] = score_cards(card_type, player, self, stat1[player])
        return scores

    """
    Functions for showing info
     - These should probably be factored over the objects themselves
    """
    def show_hands(self):
        for player in range(self.num_players):
            print('Player {}:'.format(player), self.hands[player].cards)
        return

    def show_played_cards(self):
        for player in range(self.num_players):
            print('Player {}:'.format(player), self.played_cards[player].cards)
        return


"""
Helper methods
"""


def cycle_hands(hands: list) -> list:
    x = hands.pop(0)
    hands.append(x)
    return hands
