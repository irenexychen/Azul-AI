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
            number_of_tiles_by_colors = {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0,
                                         int(TileType.WHITE): 0, int(TileType.YELLOW): 0}
            for k in range(4):
                tile_type = random.randrange(1, 5)
                number_of_tiles_by_colors[tile_type] += 1
                tiles.append(tile_type)
            self.round_boxes[i] = tiles
            self.round_boxes_by_color[i] = number_of_tiles_by_colors
            self.sort_tiles_by_number(i, number_of_tiles_by_colors)

    def sort_tiles_by_number(self, row, tiles_by_colors):
        for color in tiles_by_colors.keys():
            if tiles_by_colors[color] > 0:
                number_to_sort = tiles_by_colors[color]
                self.round_boxes_by_number[row][number_to_sort].append(color)

    def adjust_fetched_tiles(self, box_fetched, tile_type_fetched: TileType, number_fetched):
        if box_fetched == -1:
            self.adjust_fetched_from_pool(tile_type_fetched)
        else:
            self.adjust_fetched_from_box(box_fetched, tile_type_fetched, number_fetched)

    def adjust_fetched_from_box(self, box_fetched, tile_type_fetched: TileType, number_fetched):
        number_in_round_box = self.round_boxes_by_color[box_fetched][int(tile_type_fetched)]
        for j in range(4):
            self.round_boxes[box_fetched][j] = int(TileType.NONE)

        self.round_boxes_by_color[box_fetched] = {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0,
                                                  int(TileType.WHITE): 0, int(TileType.YELLOW): 0}

        self.round_boxes_by_number[box_fetched] = {4: [], 3: [], 2: [], 1: []}

        self.pool[tile_type_fetched] += number_in_round_box - number_fetched

    def adjust_fetched_from_pool(self, tile_type_fetched: TileType):
        self.pool[tile_type_fetched] = 0

    def has_tile(self):
        for i in range(5):
            for j in range(4):
                if self.round_boxes[i][j] != 0:
                    return True
        for tile_type, amount in self.pool.items():
            if self.pool[tile_type] > 0:
                return True
        return False

    def print_table(self):
        self.print_round_box()
        self.print_pool()

    def print_round_box(self):
        print("Round box:", self.round_boxes)
        switcher = {
            0: " ",
            1: "B",
            2: "Y",
            3: "R",
            4: "K",
            5: "W",
        }
        for box_number in range(5):
            tiles = " %d --- " % box_number
            for tile_number in range(4):
                tiles += " %s" % switcher[self.round_boxes[box_number][tile_number]]
            print(tiles)

    def print_pool(self):
        print("Pool:", self.pool)
