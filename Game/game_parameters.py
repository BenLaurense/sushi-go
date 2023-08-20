from Cards.card_base import CardCategory

"""
Default Game parameters
"""

# This needs to be some special record class, indexed by enum - another design pattern I don't know
default_card_types = {}

default_counts = {CardCategory.nigiri: 12,
                  CardCategory.rolls: 12,
                  CardCategory.appetizers: 8,
                  CardCategory.specials: 3,
                  CardCategory.dessert: [5, 3, 2]}

"""
Eventually should have a record class storing game params and a factory object
making the gameboards
"""
