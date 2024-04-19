from Game.gameboard import *


if __name__ == "__main__":
    test_params = {
        Card.egg_nigiri: 3,
        Card.salmon_nigiri: 3,
        Card.squid_nigiri: 3,
        Card.one_maki: 2,
        Card.two_maki: 2,
        Card.three_maki: 2,
        Card.eel: 4,
        Card.dumpling: 4,
    }

    # S = Card.two_uramaki
    # print(S.get_type() == CardType.uramaki)
    # print(S.get_type().get_category())
    #
    # print(get_card_types(test_params))

    # D = Deck(test_params)
    # print(D, len(D))
    # H = D.deal_hands(2, 2)
    # print(H[0], H[1])
    # print(D, len(D))
    # D.shuffle()
    # print(D, len(D))

    G = Game(test_params)
    G.game_loop()
