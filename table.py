from biscuit_type import BiscuitType


class Table:
    bowls = []
    pan = []

    def __init__(self):
        self.reset()

    def reset(self):
        self.bowls = [[BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE],
                      [BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE],
                      [BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE],
                      [BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE],
                      [BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE, BiscuitType.NONE]]

        self.pan = {BiscuitType.BLUE: 0, BiscuitType.BLACK: 0, BiscuitType.RED: 0, BiscuitType.WHITE: 0,
                    BiscuitType.YELLOW: 0}

    def fill_bowls(self):
        for i in range(5):
            # TODO to fill in random
            self.bowls[i] = []
            pass

    def fetch_biscuit(self, i, biscuit_type_to_fetch: BiscuitType, number_to_fetch):
        # TODO remove from bowls
        # TODO add to pan
        pass
