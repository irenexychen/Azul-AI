from biscuit_type import BiscuitType


class Table:
    bowls = []
    pan = []

    def reset(self):
        self.bowls = [[], [], [], [], []]
        self.pan = {BiscuitType.BLUE: 0, BiscuitType.BLACK: 0, BiscuitType.RED: 0, BiscuitType.WHITE: 0,
                    BiscuitType.YELLOW: 0}

    def fetch_biscuit(self, i, biscuit_type_to_fetch: BiscuitType, number_to_fetch):
        # TODO remove from bowls
        # TODO add to pan
        pass
