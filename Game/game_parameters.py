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
