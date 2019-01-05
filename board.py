from biscuit_type import BiscuitType
from biscuit_box import BiscuitBox


class Board:
    total_scores = 0
    grids = [[], [], [], [], []]

    def __init__(self):
        self.reset()

    def reset(self):
        self.grids = [[BiscuitBox(BiscuitType.BLUE, 0),
                       BiscuitBox(BiscuitType.YELLOW, 0),
                       BiscuitBox(BiscuitType.RED, 0),
                       BiscuitBox(BiscuitType.BLACK, 0),
                       BiscuitBox(BiscuitType.WHITE, 0)],
                      [BiscuitBox(BiscuitType.WHITE, 0),
                       BiscuitBox(BiscuitType.BLUE, 0),
                       BiscuitBox(BiscuitType.YELLOW, 0),
                       BiscuitBox(BiscuitType.RED, 0),
                       BiscuitBox(BiscuitType.BLACK, 0)],
                      [BiscuitBox(BiscuitType.BLACK, 0),
                       BiscuitBox(BiscuitType.WHITE, 0),
                       BiscuitBox(BiscuitType.BLUE, 0),
                       BiscuitBox(BiscuitType.YELLOW, 0),
                       BiscuitBox(BiscuitType.RED, 0)],
                      [BiscuitBox(BiscuitType.RED, 0),
                       BiscuitBox(BiscuitType.BLACK, 0),
                       BiscuitBox(BiscuitType.WHITE, 0),
                       BiscuitBox(BiscuitType.BLUE, 0),
                       BiscuitBox(BiscuitType.YELLOW, 0)],
                      [BiscuitBox(BiscuitType.YELLOW, 0),
                       BiscuitBox(BiscuitType.RED, 0),
                       BiscuitBox(BiscuitType.BLACK, 0),
                       BiscuitBox(BiscuitType.WHITE, 0),
                       BiscuitBox(BiscuitType.BLUE, 0)]]

    def get_scores(self):
        return self.total_scores

    def put_into_board(self, i, new_brick_type: BiscuitType):
        for biscuit in self.grids[i]:
            if biscuit.type == new_brick_type and biscuit.quantity == 0:
                # TODO verify if it is by-reference
                biscuit.quantity = 1
                break

    def calculate_scores(self):
        # TODO
        self.total_scores = 9
