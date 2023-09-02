from Game.gameboard import Gameboard
from Game.game_parameters import test_counts, test_card_types

# Testing

if __name__ == '__main__':
    G = Gameboard(test_card_types, test_counts)
    print(G.deck.cards)
