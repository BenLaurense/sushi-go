from enum import Enum
from Cards.Card_Objects.card_base import CardBase, CardType


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
