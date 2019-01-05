from biscuit_type import BiscuitType


class TrianglePlate:
    grids = {}
    penalty_box = []
    penalty_points = 0

    def reset(self):
        self.grids = {1: (0, BiscuitType.NONE), 2: (0, BiscuitType.NONE), 3: (0, BiscuitType.NONE), 4: (0, BiscuitType.NONE),
                      5: (0, BiscuitType.NONE)}
        self.penalty_box = [3, 3, 2, 2, 2, 1, 1]
        self.penalty_points = 0

    def get_penalty_points(self):
        return self.penalty_points

    def add(self, i, new_brick_type: BiscuitType, number_of_bricks):
        step = self.grids[i]
        if step[0] < i and (step[1] == BiscuitType.NONE or step[1] == new_brick_type):
            if number_of_bricks + step[0] > i:
                number_of_bricks_exceeded = number_of_bricks + step[0] - i
                self.grids[i] = (i, new_brick_type)
                self.calculate_penalty(number_of_bricks_exceeded)
            else:
                self.grids[i] = (i, new_brick_type)
        else:
            self.calculate_penalty(number_of_bricks)

    def calculate_penalty(self, number_of_unused):
        for x in range(number_of_unused):
            if self.penalty_box:
                self.penalty_points = self.penalty_points - self.penalty_box.pop()
            else:
                break
