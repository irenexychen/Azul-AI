from tile_type import TileType
from tile import Tile


class TrianglePlate:
    grids = {}
    penalty_bench = []
    PenaltyBenchSizeMax = 5
    penalty_rule = [1, 1, 2, 2, 2, 3, 3]
    penalty_points = 0

    def __init__(self):
        self.reset()

    def reset(self):
        self.grids = {1: Tile(TileType.NONE, 0), 2: Tile(TileType.NONE, 0), 3: Tile(TileType.NONE, 0),
                      4: Tile(TileType.NONE, 0),
                      5: Tile(TileType.NONE, 0)}
        self.penalty_bench = []
        self.penalty_points = 0

    def get_penalty_points(self):
        return self.penalty_points

    def add(self, row_to_add, new_tile_type: TileType, number_of_tiles):
        current_tile = self.grids[row_to_add]
        if current_tile.quantity < row_to_add and (
                current_tile.type == TileType.NONE or current_tile.type == new_tile_type):
            if number_of_tiles + current_tile.quantity > row_to_add:
                number_of_bricks_exceeded = number_of_tiles + current_tile.quantity - row_to_add
                current_tile.type = new_tile_type
                current_tile.quantity = row_to_add
                self.put_onto_penalty_bench(number_of_bricks_exceeded)
            else:
                current_tile.type = new_tile_type
                current_tile.quantity = number_of_tiles + current_tile.quantity
        else:
            self.put_onto_penalty_bench(number_of_tiles)

    def put_onto_penalty_bench(self, number_of_unused):
        for x in range(number_of_unused):
            if len(self.penalty_bench) < self.PenaltyBenchSizeMax:
                self.penalty_bench.append(1)
            else:
                break

    def calculate_penalty(self):
        self.penalty_points = 0
        for i in range(len(self.penalty_bench)):
            self.penalty_points = self.penalty_points + self.penalty_rule[i]

    def get_empty_row(self):
        for row in range(1, 6):
            if self.grids[row].quantity == 0:
                return row
        return -1

    def get_partial_filled_row(self):
        for row in range(1, 5):
            if self.grids[row].quantity < row:
                return row
        return -1

    def print_plate(self):
        for row_number in range(1, 6):
            tiles = " %d --- %s Amount: %d" % \
                    (row_number, self.grids[row_number].type, self.grids[row_number].quantity)
            print(tiles)
        print("Penalty Bench:", self.penalty_bench)
        print("------------------------------")
