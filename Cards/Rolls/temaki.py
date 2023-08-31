from Cards.card_base import CardBase, CardType


class Temaki(CardBase):
    def __init__(self):
        super().__init__(CardType.temaki)
        return

    def __str__(self):
        return 'Temaki'
