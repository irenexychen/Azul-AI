from tile_type import TileType
from tile import Tile


class TrianglePlate:
    grids = {}
    penalty_bench = []
    penalty_points = 0

    def reset(self):
        self.grids = {1: Tile(), 2: Tile(), 3: Tile(), 4: Tile(),
                      5: Tile()}
        self.penalty_bench = [3, 3, 2, 2, 2, 1, 1]
        self.penalty_points = 0

    def get_penalty_points(self):
        return self.penalty_points

    def add(self, i, new_tile_type: TileType, number_of_tiles):
        current_tile = self.grids[i]
        if current_tile.quantity < i and (
                current_tile.type == TileType.NONE or current_tile.type == new_tile_type):
            if number_of_tiles + current_tile[0] > i:
                number_of_bricks_exceeded = number_of_tiles + current_tile.quantity - i
                current_tile.type = new_tile_type
                current_tile.quantity = i
                # TODO is this value reference? if no, do not need to assign back
                self.grids[i] = current_tile
                self.calculate_penalty(number_of_bricks_exceeded)
            else:
                current_tile.quantity = number_of_tiles + current_tile.quantity
                # TODO is this value reference? if no, do not need to assign back
                self.grids[i] = current_tile
        else:
            self.calculate_penalty(number_of_tiles)

    def calculate_penalty(self, number_of_unused):
        for x in range(number_of_unused):
            if self.penalty_bench:
                self.penalty_points = self.penalty_points - self.penalty_bench.pop()
            else:
                break
