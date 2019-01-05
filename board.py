from biscuit_type import BiscuitType


class Board:
    total_scores = 0
    grids = [[], [], [], [], []]

    def get_scores(self):
        return self.total_scores

    def put_into_board(self, i, new_brick_type: BiscuitType):
        self.grids[i].add(new_brick_type)

    def calculate_scores(self):
        # TODO
        self.total_scores = 9
