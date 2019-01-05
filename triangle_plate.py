from biscuit_type import BiscuitType
from biscuit_box import BiscuitBox


class TrianglePlate:
    grids = {}
    penalty_bench = []
    penalty_points = 0

    def reset(self):
        self.grids = {1: BiscuitBox(), 2: BiscuitBox(), 3: BiscuitBox(), 4: BiscuitBox(),
                      5: BiscuitBox()}
        self.penalty_bench = [3, 3, 2, 2, 2, 1, 1]
        self.penalty_points = 0

    def get_penalty_points(self):
        return self.penalty_points

    def add(self, i, new_brick_type: BiscuitType, number_of_biscuit):
        current_biscuit_box = self.grids[i]
        if current_biscuit_box.quantity < i and (
                current_biscuit_box.type == BiscuitType.NONE or current_biscuit_box.type == new_brick_type):
            if number_of_biscuit + current_biscuit_box[0] > i:
                number_of_bricks_exceeded = number_of_biscuit + current_biscuit_box.quantity - i
                current_biscuit_box.type = new_brick_type
                current_biscuit_box.quantity = i
                # TODO is this value reference? if no, do not need to assign back
                self.grids[i] = current_biscuit_box
                self.calculate_penalty(number_of_bricks_exceeded)
            else:
                current_biscuit_box.quantity = number_of_biscuit + current_biscuit_box.quantity
                # TODO is this value reference? if no, do not need to assign back
                self.grids[i] = current_biscuit_box
        else:
            self.calculate_penalty(number_of_biscuit)

    def calculate_penalty(self, number_of_unused):
        for x in range(number_of_unused):
            if self.penalty_bench:
                self.penalty_points = self.penalty_points - self.penalty_bench.pop()
            else:
                break
