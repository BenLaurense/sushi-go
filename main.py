from enum import Enum
from numpy import argmax
import random


# Testing being done in a jupyter notebook instead
# What is going on with this weird importing issue?!
# Also, the strange match/case issue... Not really sure what's going on TBH
"""
Base class for card objects. A card object stores:
 - The CardType of the card
 - The CardCategory fo the card
"""


# There will be a nicer way of doing this! I could go full OO and have another layer of subclassing...
# There might be an Enum Dict class?
class CardCategory(Enum):
    nigiri = 1
    rolls = 2
    appetizers = 3
    special = 4
    dessert = 5


class CardType(Enum):
    # Nigiri
    nigiri = 1

    # Rolls
    maki = 2
    temaki = 3
    uramaki = 4

    # Appetizers
    dumpling = 5
    edamame = 6
    eel = 7
    miso = 8
    onigiri = 9
    sashimi = 10
    tempura = 11
    tofu = 12

    # Special
    chopsticks = 13
    menu = 14
    soy_sauce = 15
    special_order = 16
    spoon = 17
    takeout_box = 18
    tea = 19
    wasabi = 20

    # Dessert
    fruit = 21
    green_tea_ice_cream = 22
    pudding = 23


card_enum_dict = {CardCategory.nigiri: [CardType.nigiri],
                  CardCategory.rolls: [CardType.maki, CardType.temaki, CardType.uramaki],
                  CardCategory.appetizers: [CardType.dumpling, CardType.edamame, CardType.eel,
                                            CardType.miso, CardType.onigiri, CardType.sashimi,
                                            CardType.tempura, CardType.tofu],
                  CardCategory.special: [CardType.chopsticks, CardType.menu, CardType.soy_sauce,
                                         CardType.special_order, CardType.spoon, CardType.takeout_box,
                                         CardType.tea, CardType.wasabi],
                  CardCategory.dessert: [CardType.fruit, CardType.green_tea_ice_cream, CardType.pudding]}


class CardBase:
    def __init__(self,
                 card_type: CardType,
                 specific_type=None):
        self.card_type = card_type
        self.specific_type = specific_type
        return

    def __str__(self):
        raise NotImplementedError


"""
Individual card types: Nigiri
"""


class NigiriType(Enum):
    # This also represents the score of the nigiri
    egg = 1
    salmon = 2
    squid = 3


class Nigiri(CardBase):
    def __init__(self, specific_type: NigiriType):
        super().__init__(CardType.nigiri, specific_type)
        return

    def __str__(self):
        return '{} Nigiri'.format(self.specific_type.name)


"""
Individual card types: Rolls
"""


class MakiType(Enum):
    one = 1
    two = 2
    three = 3


class Maki(CardBase):
    def __init__(self, specific_type: MakiType):
        super().__init__(CardType.maki, specific_type)
        return

    def __str__(self):
        return 'Maki: {} roll(s)'.format(self.specific_type.name)


class Temaki(CardBase):
    def __init__(self):
        super().__init__(CardType.temaki)
        return

    def __str__(self):
        return 'Temaki'


class UramakiType(Enum):
    three = 3
    four = 4
    five = 5


class Uramaki(CardBase):
    def __init__(self, specific_type: UramakiType):
        super().__init__(CardType.uramaki, specific_type)
        return

    def __str__(self):
        return 'Uramaki: {} roll(s)'.format(self.specific_type.name)


"""
Individual card types: Appetisers
"""


class Dumpling(CardBase):
    def __init__(self):
        super().__init__(CardType.dumpling)
        return

    def __str__(self):
        return 'Dumpling'


class Edamame(CardBase):
    def __init__(self):
        super().__init__(CardType.edamame)
        return

    def __str__(self):
        return 'Edamame'


class Eel(CardBase):
    def __init__(self):
        super().__init__(CardType.eel)
        return

    def __str__(self):
        return 'Eel'


class Miso(CardBase):
    def __init__(self):
        super().__init__(CardType.miso)
        return

    def __str__(self):
        return 'Miso'


class OnigiriType(Enum):
    triangle = 1
    circle = 2
    square = 3
    rectangle = 4


class Onigiri(CardBase):
    def __init__(self, specific_type: OnigiriType):
        super().__init__(CardType.onigiri, specific_type)
        return

    def __str__(self):
        return '{} Onigiri'.format(self.specific_type.name)


class Sashimi(CardBase):
    def __init__(self):
        super().__init__(CardType.sashimi)
        return

    def __str__(self):
        return 'Sashimi'


class Tempura(CardBase):
    def __init__(self):
        super().__init__(CardType.tempura)
        return

    def __str__(self):
        return 'Tempura'


class Tofu(CardBase):
    def __init__(self):
        super().__init__(CardType.tofu)
        return

    def __str__(self):
        return 'Tofu'


"""
Individual card types: Specials
"""


"""
Individual card types: Desserts
"""


class FruitType(Enum):
    pp = 1
    mm = 2
    ww = 3
    pm = 4
    pw = 5
    mw = 6


class Fruit(CardBase):
    def __init__(self, specific_type: FruitType):
        super().__init__(CardType.fruit, specific_type)
        return

    def __str__(self):
        return 'Something lol'


class GreenTeaIceCream(CardBase):
    def __init__(self):
        super().__init__(CardType.green_tea_ice_cream)
        return

    def __str__(self):
        return 'Green Tea Ice Cream'


class Pudding(CardBase):
    def __init__(self):
        super().__init__(CardType.pudding)
        return

    def __str__(self):
        return 'Pudding'


"""
Default Game parameters
"""

# This needs to be some special record class, indexed by enum - another design pattern I don't know
default_card_types = {CardCategory.nigiri: [CardType.nigiri],
                      # The rest
                      }

default_counts = {CardCategory.nigiri: [12],
                  CardCategory.rolls: [12],
                  CardCategory.appetizers: [8],
                  CardCategory.special: [3],
                  CardCategory.dessert: [5, 3, 2]}

test_card_types = {CardCategory.nigiri: [CardType.nigiri]}
test_counts = {CardCategory.nigiri: [10],
               CardCategory.rolls: [0],
               CardCategory.appetizers: [0],
               CardCategory.special: [0],
               CardCategory.dessert: [0, 0, 0]}


"""
Classes for storing a hand and a played board
"""


class Hand:
    # This might be better subclassing list
    def __init__(self,
                 init_cards=None):
        self.cards = []
        if init_cards is not None:
            self.cards += init_cards
        return


class PlayedCards:
    # This might be better subclassing list
    def __init__(self):
        self.cards = []
        return

    def reset(self):
        # Resets the hand, leaving desserts!
        for card in self.cards:
            if card.CardType not in card_enum_dict[CardCategory.dessert]:
                self.cards.remove(card)
        return


"""
Method that constructs cards based on their specific_type and count
(Might want this to be able to take in a config of build rules)
"""


def build_cards(card_type: CardType,
                category_count: int) -> list[CardBase]:
    # Re-enable different deck sizing!
    if card_type == CardType.nigiri:
        return 4 * [Nigiri(NigiriType.egg)] + 5 * [Nigiri(NigiriType.salmon)] + 3 * [Nigiri(NigiriType.squid)]
    elif card_type == CardType.maki:
        return 4 * [Maki(MakiType.one)] + 5 * [Maki(MakiType.two)] + 3 * [Maki(MakiType.three)]
    else:
        raise Exception("No build rule for the specified CardType!")

        # Rolls
        # case CardType.maki:
        #     return 4*[Maki(MakiType.one)] + 5*[Maki(MakiType.two)] + 3*[Maki(MakiType.three)]
        # case CardType.temaki:
        #     return 12*[Temaki()]
        # case CardType.uramaki:
        #     return 4*[Uramaki(UramakiType.three), Uramaki(UramakiType.four), Uramaki(UramakiType.five)]
        # # Appetisers
        # case CardType.dumpling:
        #     return 8*[Dumpling()]
        # case CardType.edamame:
        #     return 8*[Edamame()]
        # case CardType.eel:
        #     return 8*[Eel()]
        # case CardType.miso:
        #     return 8*[Miso()]
        # case CardType.onigiri:
        #     return 2*[Onigiri(OnigiriType.triangle), Onigiri(OnigiriType.circle),
        #               Onigiri(OnigiriType.square), Onigiri(OnigiriType.rectangle)]
        # case CardType.sashimi:
        #     return 8*[Sashimi()]
        # case CardType.tempura:
        #     return 8*[Tempura()]
        # case CardType.tofu:
        #     return 8*[Tofu()]
        # # Specials
        #
        # # Desserts
        # case CardType.fruit:
        #     return 2*[Fruit(FruitType.pp), Fruit(FruitType.mm), Fruit(FruitType.ww)] \
        #         + 3*[Fruit(FruitType.pm), Fruit(FruitType.pw), Fruit(FruitType.mw)]
        # case CardType.green_tea_ice_cream:
        #     return 15*[GreenTeaIceCream()]
        # case CardType.pudding:
        #     return 15*[Pudding()]
        # case _:
        #     raise Exception("No build rule for the specified CardType!")


"""
Deck class
 - build_deck method calls card_builder to build collection of cards of each CardType
 - Contains methods for dealing, shuffling, appending cards
"""


class Deck:
    # Making this inherit from List might be a much better way of doing this!
    def __init__(self,
                 card_type_dict: dict[CardCategory, list[CardType]],
                 category_count_dict: dict[CardCategory, list[int]]) -> None:
        self.card_type_dict = card_type_dict
        self.category_counts = category_count_dict
        self.cards = []

        # Builds deck:
        self.reset(1)
        return

    def reset(self,
              round_number: int):
        self.build_deck(round_number)
        self.shuffle()
        return

    """
    Build the deck from the chosen CardTypes and Counts
    """
    def build_deck(self,
                   round_number: int) -> None:
        # Takes card types and builds the requisite cards
        self.cards = []
        for category, card_types in self.card_type_dict.items():
            if category != CardCategory.dessert:
                for card_type in card_types:
                    count = self.category_counts[category][round_number - 1]
                    cards = build_cards(card_type, count)
                    self.cards += cards
            else:
                # Dessert cards have changing amounts per round
                # Ah. This might have to be fixed!!
                for card_type in card_types:
                    count = self.category_counts[category][round_number - 1]
                    cards = build_cards(card_type, count)
                    self.cards += cards
        return

    """
    Shuffling
    """
    def shuffle(self) -> None:
        random.shuffle(self.cards)
        return

    def append_and_shuffle(self,
                           cards: list[CardBase]) -> None:
        self.cards += cards
        self.shuffle()
        return

    """
    Drawing and hand creation
    """
    def draw(self,
             num_cards: int) -> list[CardBase]:
        if num_cards > len(self.cards):
            raise Exception("There are too few cards left in the deck for drawing!")
        else:
            drawn_cards = self.cards[-num_cards:]
            del self.cards[-num_cards:]
            return drawn_cards

    def deal_hands(self,
                   num_hands: int,
                   num_cards_per_hand: int) -> list[Hand]:
        if num_hands*num_cards_per_hand > len(self.cards):
            raise Exception("There are too few cards left in the deck to deal!")
        else:
            hands = []
            for i in range(num_hands):
                hand = Hand(self.draw(num_cards_per_hand))
                hands.append(hand)
            return hands


"""
Helper method for unpacking one of these special record types into a list of card types
"""


def unpack_card_types(card_type_dict: dict[CardCategory, list[CardType]]) -> list[CardType]:
    # There is probably a numpy operation for this
    unpacked_card_types = []
    for _, card_types in card_type_dict.items():
        unpacked_card_types += card_types
    return unpacked_card_types


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
        print('Final scores are {}'.format(scores)) # This error should be disabled
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
            move = int(input('Enter valid move index')) # Integer index for now
            moves.append(move)

        # Reveal and execute moves:
        for player in range(self.num_players):
            played_card = self.hands[player].cards[moves[player]]
            print('Player {} played {} with specific type {}'
                  .format(player + 1, played_card, played_card.specific_type))
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
        scores = [0]*self.num_players

        # Precalculate totals of all relevant cardtypes
        return scores

    """
    Functions for showing info
     - These should probably be factored over the objects themselves
    """
    def show_hands(self):
        for player in range(self.num_players):
            card_string_reps = list(map(lambda card: card.__str__, self.hands[player].cards))
            print('Player {}:'.format(player + 1), card_string_reps)
        return

    def show_played_cards(self):
        for player in range(self.num_players):
            print('Player {}:'.format(player + 1), self.played_cards[player].cards)
        return


"""
Helper methods
"""


def cycle_hands(hands: list) -> list:
    x = hands.pop(0)
    hands.append(x)
    return hands


# Testing
if __name__ == '__main__':
    test_card_types = {CardCategory.nigiri: [CardType.nigiri]}
    test_counts = {CardCategory.nigiri: [10],
                   CardCategory.rolls: [0],
                   CardCategory.appetizers: [0],
                   CardCategory.special: [0],
                   CardCategory.dessert: [0, 0, 0]}
    G = Gameboard(test_card_types, test_counts)
    G.game_loop()

