from V2.Game import *


if __name__ == "__main__":
    card_types = [CardType.nigiri, CardType.maki, CardType.sashimi]
    # factory = DeckFactory(3, card_types)
    # deck = factory.build_deck(0)
    # cards = deck.cards
    # print(cards)
    # print(len(cards))

    config = GameConfig(2, 2, 2, card_types)
    Game = Game(config)

