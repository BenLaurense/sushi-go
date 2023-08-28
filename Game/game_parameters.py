from Cards.card_base import CardCategory, CardType

"""
Default Game parameters
"""

# This needs to be some special record class, indexed by enum - another design pattern I don't know
default_card_types = {CardCategory.nigiri: [CardType.nigiri],
                      # The rest
                      }

default_counts = {CardCategory.nigiri: 12,
                  CardCategory.rolls: 12,
                  CardCategory.appetizers: 8,
                  CardCategory.specials: 3,
                  CardCategory.dessert: [5, 3, 2]}

test_card_types = {CardCategory.nigiri: [CardType.nigiri]}
test_counts = {CardCategory.nigiri: 3,
               CardCategory.rolls: 0,
               CardCategory.appetizers: 0,
               CardCategory.specials: 0,
               CardCategory.dessert: [0, 0, 0]}
