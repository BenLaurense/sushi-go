from enum import Enum
from random import shuffle


class Card(Enum):
    def type(self):
        conversion = {
            Card.egg_nigiri: CardType.nigiri,
            Card.salmon_nigiri: CardType.nigiri,
            Card.squid_nigiri: CardType.nigiri,
            Card.one_maki: CardType.maki,
            Card.two_maki: CardType.maki,
            Card.three_maki: CardType.maki,
            Card.temaki: CardType.temaki,
            # Card.one_uramaki: CardType.uramaki,
            # Card.two_uramaki: CardType.uramaki,
            # Card.three_uramaki: CardType.uramaki,
            # Card.four_uramaki: CardType.uramaki,
            # Card.five_uramaki: CardType.uramaki,
            Card.dumpling: CardType.dumpling,
            Card.eel: CardType.eel,
            Card.circle_onigiri: CardType.onigiri,
            Card.triangle_onigiri: CardType.onigiri,
            Card.square_onigiri: CardType.onigiri,
            Card.rectangle_onigiri: CardType.onigiri,
            Card.sashimi: CardType.sashimi,
            Card.tempura: CardType.tempura,
            Card.tofu: CardType.tofu,
        }
        return conversion[self]

    egg_nigiri = 1
    salmon_nigiri = 2
    squid_nigiri = 3

    one_maki = 4
    two_maki = 5
    three_maki = 6
    temaki = 7
    # one_uramaki = 8
    # two_uramaki = 9
    # three_uramaki = 10
    # four_uramaki = 11
    # five_uramaki = 12

    dumpling = 13
    # edamame = 14
    eel = 15
    circle_onigiri = 16
    triangle_onigiri = 17
    square_onigiri = 18
    rectangle_onigiri = 19
    # miso = 20
    sashimi = 21
    tempura = 22
    tofu = 23


class CardType(Enum):
    def category(self):
        conversion = {
            CardType.nigiri: CardCategory.nigiri,
            CardType.maki: CardCategory.rolls,
            CardType.temaki: CardCategory.rolls,
            CardType.uramaki: CardCategory.rolls,
            CardType.dumpling: CardCategory.appetisers,
            CardType.eel: CardCategory.appetisers,
            CardType.onigiri: CardCategory.appetisers,
            CardType.sashimi: CardCategory.appetisers,
            CardType.tempura: CardCategory.appetisers,
            CardType.tofu: CardCategory.appetisers,
        }
        return conversion[self]

    nigiri = 1
    maki = 2
    temaki = 3
    uramaki = 4
    dumpling = 5
    # edamame = 6
    eel = 7
    onigiri = 8
    # miso = 9
    sashimi = 10
    tempura = 11
    tofu = 12


class CardCategory(Enum):
    nigiri = 1
    rolls = 2
    appetisers = 3
    specials = 4
    dessert = 5


class Deck:
    _cards: list[Card]

    def __init__(self, cards: list[Card]):
        self._cards = cards # Only set on initialisation
        self.shuffle()
        return

    @property
    def cards(self):
        return [card.name for card in self._cards]

    def append(self, cards: list[Card]):
        self._cards += cards
        self.shuffle()
        return

    def draw(self, count: int) -> list[Card]:
        if count > len(self._cards):
            raise Exception("There are too few cards left in the deck for drawing!")
        else:
            draw = self._cards[-count:]
            del self._cards[-count:]
            return draw

    def deal_hands(self, num_hands: int, cards_per_hand: int) -> list[list[Card]]:
        if num_hands*cards_per_hand > len(self._cards):
            raise Exception("There are too few cards left in the deck to deal!")
        else:
            hands: list[list[Card]] = []
            for _ in range(num_hands):
                hand = self.draw(cards_per_hand)
                hands.append(hand)
            return hands

    def shuffle(self):
        shuffle(self._cards)


# Builder class for cards
def build_cards(card_type: CardType, count: int) -> list[Card]:
    match card_type:
        case CardType.nigiri:
            cards = [Card.egg_nigiri, Card.salmon_nigiri, Card.squid_nigiri] * (count // 3)

        case CardType.maki:
            cards = (4*[Card.one_maki] + 5*[Card.two_maki] + 3*[Card.three_maki]) * (count // 12)
        case CardType.temaki:
            cards = [Card.temaki] * count

        case CardType.eel:
            cards = [Card.eel] * count
        case CardType.tempura:
            cards = [Card.tempura] * count
        case CardType.sashimi:
            cards = [Card.sashimi] * count

        case _:
            raise Exception(f"Error in {build_cards}: invalid {CardType} specified")
    return cards


def build_round_additions(num_rounds: int, card_type: CardType, count: int) -> list[list[Card]]:
    # None for now
    return [[] for _ in range(num_rounds)]


# Want to keep the deck factory object around loaded with the correct configs,
# so we don't have to worry about reset methods
class DeckFactory:
    # Some params are fixed
    _category_counts = {
        CardCategory.nigiri: 12,
        CardCategory.rolls: 12,
        CardCategory.appetisers: 8,
        # CardCategory.specials: 3,
        # CardCategory.dessert: 15
    }

    _cards: list[Card]
    _round_additions: list[list[Card]]

    def __init__(self, num_rounds: int, card_types: list[CardType]):
        # Validate input?

        # Fill internal state
        self._cards = []
        self._round_additions = [[] for _ in range(num_rounds)]
        for card_type in card_types:
            category = card_type.category()
            count = self._category_counts[category]

            cards = build_cards(card_type, count)
            self._cards += cards

            round_additions = build_round_additions(num_rounds, card_type, count)
            self._round_additions = [self._round_additions[i] + round_additions[i] for i in range(num_rounds)]
        return

    def build_deck(self, round: int) -> Deck:
        this_round_cards = self._cards + self._round_additions[round]
        return Deck(this_round_cards)


class GameConfig:
    num_players: int
    num_rounds: int
    hand_size: int
    card_types: list[CardType]

    def __init__(self, num_players: int, num_rounds: int, hand_size: int, card_types: list[CardType]):
        self.num_players = num_players
        self.num_rounds = num_rounds
        self.hand_size = hand_size
        self.card_types = card_types
        return


class Game:
    _curr_round: int = 0
    _deckFactory: DeckFactory

    config: GameConfig
    deck: Deck
    hands: list[list[Card]]
    played_cards: list[list[Card]]
    round_scores: list[list[int]]

    def __init__(self, config: GameConfig):
        self.config = config # Could do config loader syntax here. Loadable throughout the game
        self._deckFactory = DeckFactory(config.num_rounds, config.card_types)

        self._reset_game()
        self._game_loop()
        return

    def _reset_game(self):
        # Only thing that needs reset that isn't round-dependent is the scores
        self.round_scores = [[0] * self.config.num_rounds] * self.config.num_players
        return

    def _game_loop(self):
        for round in range(self.config.num_rounds):
            self._curr_round = round

            # Prepare this round
            self._prepare_round()
            self._play_round()

            # Compute score for the round

            self._curr_round += 1
        # Game end sequence
        return

    def _prepare_round(self):
        # Resets anything round-secific
        self.deck = self._deckFactory.build_deck(self._curr_round)
        self.hands = self.deck.deal_hands(self.config.num_players, self.config.hand_size)
        self.played_cards = [[] for _ in range(self.config.num_players)]
        return

    def _play_round(self):
        for turn in range(self.config.hand_size):
            print(f'Playing turn {turn + 1}')
            self.show_hands()
            self.show_played_cards()
            self._play_turn()
        return

    def _compute_round_scores(self, round: int):
        return

    def get_player_input(self, player: int):
        move = int(input(f'Player {player + 1}: Enter valid move index:'))  # Integer index for now
        return move

    def _play_turn(self):
        # Collect moves:
        this_turn = []
        for player in range(self.config.num_players):
            move = self.get_player_input(player)
            played_card = self.hands[player].pop(move)
            this_turn.append(played_card)
            self.played_cards[player].append(played_card)

        # Reveal and execute moves:
        for player in range(self.config.num_players):
            print('Player {} played {} with specific type {}'
                  .format(player + 1, this_turn[player].type().name, this_turn[player].name))
            # Trigger any special card effects

        # End of turn:
        self.cycle_hands()
        return

    """
    Printing stuff
    """
    def show_hands(self):
        print('Hand:')
        for player in range(self.config.num_players):
            nice_rep = list(map(lambda x: x.name, self.hands[player]))
            print('Player {}:'.format(player + 1), nice_rep)
        return

    def show_played_cards(self):
        print('Played:')
        for player in range(self.config.num_players):
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
