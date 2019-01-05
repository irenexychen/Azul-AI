from biscuit_type import BiscuitType


class BiscuitBox:
    type = BiscuitType.NONE
    quantity = 0

    def __init__(self, biscuit_type, amount):
        self.type = biscuit_type
        self.quantity = amount
