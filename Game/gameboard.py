from Cards.card_base import CardCategory, CardType, dessert_types
from game_parameters import default_counts
from hand import Hand, PlayedCards
from Cards.deck import Deck
from Cards.score_calculator import score_cards
from numpy import argmax


"""
Gameboard class - object which tracks game global variables, and has methods for playing turns
"""


class Gameboard:
    def __init__(self,
                 card_types: dict[CardCategory, list[CardType]],
                 card_category_counts=default_counts):
        # Global game vars:
        self.num_players = 2
        self.num_rounds = 3
        self.card_types = card_types

        # Internal vars:
        self.deck = Deck(card_types, card_category_counts)  # Should be Deck object with DEFAULT PARAMS
        self.hands = [Hand()]*self.num_players   # List of hand objects
        self.played_cards = [PlayedCards()]*self.num_players    # List of board objects

        self.num_cards_remaining = len(self.deck.cards)

        # Round-specific vars:
        return

    """
    Game loop
    """
    def game_loop(self):
        print('Starting game of {} rounds'.format(self.num_rounds))
        for round in range(self.num_rounds):
            scores = self.play_round(round)

        # Final round has special scoring, but this is done withing play_round

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
    def play_round(self, round: int):
        # Plays round, calcs scores, and resets deck at the end
        if round < self.num_rounds - 1:
            print('Round {} starting'.format(round))
        else:
            print('Round {} starting. Desserts will count after this round'.format(round))

        # Loop through turns within the round
        while self.num_cards_remaining > 0:
            self.play_turn()

        # Show scores:
        include_dessert = (round == self.num_rounds - 1)
        scores = self.calc_scores(include_dessert)
        print('Scores are {}'.format(scores))

        # End of round:
        # Reset the board (and consider desserts):
        self.deck.reset(round)
        for played_cards in self.played_cards:
            played_cards.reset()

        print('Round {} over'.format(round))
        return scores

    def play_turn(self):
        # Collects player input for their round and changes gameboard accordingly
        # Show info:
        self.show_hands()
        self.show_played_cards()

        # Get player inputs:
        moves = []
        for player in range(self.num_players):
            move = 1000  # Arbitrary large number
            while move > self.num_cards_remaining:
                move = input('Enter valid move')
            moves.append(move)

        # Reveal and execute moves:
        for player in range(self.num_players):
            print('Player {} played {}'.format(player + 1, self.hands[player]))
            # Trigger any special card effects?
            move = moves[player]
            played_card = self.hands[player].cards.pop(move)
            self.played_cards[player].cards.append(played_card)

        # Perform special effects according to execution order
        ### Not needed yet

        # Increment turn timer:
        self.num_cards_remaining -= 1

        # Cycle the hands:
        self.hands = cycle_hands(self.hands)
        return

    """
    Functions for calculating score
    """
    def calc_scores(self, include_dessert=False):
        scores = []
        for player in range(self.num_players):
            score = 0
            for card_type in self.card_types:
                # Score for dessert is only counted in the final round
                if card_type not in dessert_types or include_dessert:
                    # Get corresponding card variety
                    score += score_cards(card_type, self.played_cards[player])
            scores.append(score)
        return scores

    """
    Functions for showing info
    """
    def show_hands(self):
        for player in range(self.num_players):
            print('Player {}:'.format(player), self.hands[player])
        return

    def show_played_cards(self):
        for player in range(self.num_players):
            print('Player {}:'.format(player), self.played_cards[player])
        return


"""
Helper methods
"""


def cycle_hands(hands: list) -> list:
    x = hands.pop(0)
    hands.append(x)
    return hands
