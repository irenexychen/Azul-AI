from tile_type import TileType
import random
import numpy as np


class Table:
    round_boxes = np.empty([5, 4])
    round_boxes_by_number = {}
    round_boxes_by_color = {}

    pool = {}

    def __init__(self):
        self.reset()

    def reset(self):
        self.round_boxes = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]]

        self.round_boxes_by_number = [{4: [], 3: [], 2: [], 1: []},
                                      {4: [], 3: [], 2: [], 1: []},
                                      {4: [], 3: [], 2: [], 1: []},
                                      {4: [], 3: [], 2: [], 1: []},
                                      {4: [], 3: [], 2: [], 1: []}]

        self.round_boxes_by_color = [
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0, int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0,
             int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0,
             int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0,
             int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0,
             int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0}, ]

        self.pool = {TileType.BLUE: 0, TileType.BLACK: 0, TileType.RED: 0, TileType.WHITE: 0,
                     TileType.YELLOW: 0}

    def fill_boxes(self):

        for i in range(5):
            tiles = []
            #
            number_of_tiles_by_colors = {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0,
                                         int(TileType.WHITE): 0, int(TileType.YELLOW): 0}
            for k in range(4):
                tile_type = random.randrange(1, 5)
                number_of_tiles_by_colors[tile_type] += 1
                tiles.append(tile_type)
            self.round_boxes[i] = tiles
            self.round_boxes_by_color.append(number_of_tiles_by_colors)
            self.sort_tiles_by_number(number_of_tiles_by_colors)

    def sort_tiles_by_number(self, tiles_by_colors):
        for number_to_sort in range(5, 0, -1):
            sorted_number_by_color = []
            for color in tiles_by_colors.keys():
                if tiles_by_colors[color] == number_to_sort:
                    sorted_number_by_color.append(color)
            self.round_boxes_by_number.append({number_to_sort: sorted_number_by_color})

    def move_unused_tile_into_pool(self, i, tile_type_fetched: TileType, fetched_number):
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
            # TODO sort tiles again

    def has_tile(self):
        for i in range(5):
            for j in range(4):
                if self.round_boxes[i][j] != 0:
                    return True
        for tile_type, amount in self.pool.items():
            if self.pool[tile_type] > 0:
                return True
        return False
