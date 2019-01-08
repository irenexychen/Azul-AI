from tile_type import TileType
import random
import numpy as np


class Table:
    round_boxes = np.empty([5, 4])
    pool = {}

    def __init__(self):
        self.reset()

    def reset(self):
        self.round_boxes = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]]

        self.pool = {TileType.BLUE: 0, TileType.BLACK: 0, TileType.RED: 0, TileType.WHITE: 0,
                     TileType.YELLOW: 0}

    def fill_boxes(self):
        for i in range(5):
            tiles = []
            for k in range(4):
                tile_type = random.randrange(1, 5)
            tiles.append(tile_type)
            self.round_boxes[i] = tiles

    def move_tile_to_pool(self, i, tile_type_fetched: TileType, fetched_number):
        tiles_to_be_flushed = 0
        for j in range(4):
            if self.round_boxes[i][j] == int(tile_type_fetched):
                if tiles_to_be_flushed < fetched_number:
                    tiles_to_be_flushed += 1
                else:
                    tiles_to_be_flushed = 0
                # TODO throw exception
        if tiles_to_be_flushed > 0:
            for j in range(4):
                self.round_boxes[i][j] = int(TileType.NONE)
            self.pool[tile_type_fetched] += fetched_number - tiles_to_be_flushed

    def has_tile(self):
        for i in range(5):
            for j in range(4):
                if self.round_boxes[i][j] != 0:
                    return True
        for tile_type, amount in self.pool.items():
            if self.pool[tile_type] > 0:
                return True
        return False
