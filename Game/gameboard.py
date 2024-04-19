from Cards.deck import Deck
from Cards.scorers import calculate_score
from Game.game_parameters import *
from numpy import argmax


"""
Main Game class
"""


class Game:
    def __init__(self, card_counts: dict[Card, int]):
        # Instance vars
        self.card_counts = card_counts
        self.card_types = get_card_types(card_counts)   # Precompute for speed
        self.deck = Deck(card_counts)
        self.hands: list[list[Card]] = self.deck.deal_hands(NUM_PLAYERS, HAND_SIZE)
        self.played_cards: list[list[Card]] = [[] for _ in range(NUM_PLAYERS)]  # Lol
        self.scores = [0]*NUM_PLAYERS

        # Counters
        self.round = 0  # Round counter from 0 to 2
        self.turn = 0   # Turn counter from 0 to hand_size

        # TODO: Refactor statistics computation
        self.stats = {card_type: [0]*NUM_PLAYERS for card_type in self.card_types}
        return

    """
    Game loop stuff
    """
    def game_loop(self):
        """
        Outer game loop
        - Play rounds
        - Reset scores, turn counter
        - Game end condition
        """
        print('Starting game of {} rounds'.format(NUM_ROUNDS + 1))
        for round_num in range(NUM_ROUNDS):
            print('====================')
            self.play_round(round_num)

        # End the game:
        print('FINAL SCORES ARE: {}'.format(self.scores))
        winner = argmax(self.scores) + 1
        print('Winner is Player {}!'.format(winner))
        self.round = 0
        self.scores = [0]*NUM_PLAYERS

        play_again = input('Play another game? Y/N')
        while play_again not in ['Y', 'N']:
            play_again = input('Play another game? Y/N')
        if play_again == 'Y':
            exit('Implement me lol')
        else:
            exit('Game over')

    def play_round(self, round_num: int):
        print('Round {} starting'.format(round_num + 1))
        while self.turn < HAND_SIZE:
            print('====================')
            self.play_turn()
        print('====================')
        print('ROUND OVER')

        # End of round
        self.show_played_cards()
        this_round_scores = calculate_score(self.card_types, NUM_PLAYERS, self.stats)
        self.scores = list(map(lambda s, x: s + x, self.scores, this_round_scores))
        print('SCORES FOR THIS ROUND: {}'.format(this_round_scores))

        # Reset game
        self.deck.reset()
        self.hands = self.deck.deal_hands(NUM_PLAYERS, HAND_SIZE)
        self.played_cards = [[] for _ in range(NUM_PLAYERS)]
        self.stats = {card_type: [0]*NUM_PLAYERS for card_type in self.card_types}
        self.turn = 0

        self.round += 1
        return

    def play_turn(self):
        self.show_hands()
        self.show_played_cards()

        # TODO: Update this when game env is made
        this_turn = []
        for player in range(NUM_PLAYERS):
            move = int(input('Enter valid move index:'))  # Integer index for now
            played_card = self.hands[player][move]
            this_turn.append(played_card)
            self.hands[player].remove(played_card)
            self.played_cards[player].append(played_card)

            self.precompute_stats(player, played_card)

        # Reveal and execute moves:
        for player in range(NUM_PLAYERS):
            print('Player {} played {} with specific type {}'
                  .format(player + 1, this_turn[player].get_type().name, this_turn[player].name))
            # Trigger any special card effects

        # End of turn:
        self.cycle_hands()
        print('STATS:', self.stats)  # Debugging

        self.turn += 1
        return

    """
    Stats computation
    """
    def precompute_stats(self, player: int, played_card: Card):
        additive = {
            Card.egg_nigiri: 1,
            Card.salmon_nigiri: 2,
            Card.squid_nigiri: 3,
            Card.one_maki: 1,
            Card.two_maki: 2,
            Card.three_maki: 3,
            Card.temaki: 1,
            # Card.one_uramaki: 1,
            # Card.two_uramaki: 2,
            # Card.three_uramaki: 3,
            # Card.four_uramaki: 4,
            # Card.five_uramaki: 5,
            Card.dumpling: 1,
            Card.eel: 1,
            # Onigiri encoding
            Card.circle_onigiri: 1,
            Card.triangle_onigiri: 10,
            Card.square_onigiri: 100,
            Card.rectangle_onigiri: 1000,
            Card.sashimi: 1,
            Card.tempura: 1,
            Card.tofu: 1,
        }

        self.stats[played_card.get_type()][player] += additive[played_card]
        return

    """
    Printing stuff
    """
    def show_hands(self):
        print('Hand:')
        for player in range(NUM_PLAYERS):
            nice_rep = list(map(lambda x: x.name, self.hands[player]))
            print('Player {}:'.format(player + 1), nice_rep)
        return

    def show_played_cards(self):
        print('Played:')
        for player in range(NUM_PLAYERS):
            nice_rep = list(map(lambda x: x.name, self.played_cards[player]))
            print('Player {}:'.format(player + 1), nice_rep)
        return

    """
    Helpers
    """
    def cycle_hands(self):
        x = self.hands.pop(0)
        self.hands.append(x)
        return

