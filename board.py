from tile import Tile

import math


# board wall, belongs to player
# x row
# y column
# ROWWEIGHT helps simulate triangles

class Board:
    BOARDMAPPING = [[Tile.WATER, Tile.CHEESE, Tile.FIRE, Tile.BLACK, Tile.SNOW],
                    [Tile.SNOW, Tile.WATER, Tile.CHEESE, Tile.FIRE, Tile.BLACK],
                    [Tile.BLACK, Tile.SNOW, Tile.WATER, Tile.CHEESE, Tile.FIRE],
                    [Tile.FIRE, Tile.BLACK, Tile.SNOW, Tile.WATER, Tile.CHEESE],
                    [Tile.CHEESE, Tile.FIRE, Tile.BLACK, Tile.SNOW, Tile.WATER]]

    TILEMAPPING = {
        Tile.WATER: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
        Tile.CHEESE: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)],
        Tile.FIRE: [(0, 2), (1, 3), (2, 4), (3, 0), (4, 1)],
        Tile.BLACK: [(0, 3), (1, 4), (2, 0), (3, 1), (4, 2)],
        Tile.SNOW: [(0, 4), (1, 0), (2, 1), (3, 2), (4, 3)]
    }

    ROWWEIGHT = [1, 2, 3, 4, 5]

    def __init__(self):
        self.board_container = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.completed_board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.used_rows = []

    def board_mapping(self, x, y):
        return self.BOARDMAPPING[x][y]

    def tile_mapping(self, tile_type, row):
        return self.TILEMAPPING[tile_type][row][1]

    def where_put(self, tile_type):
        avail = []
        for i in range(5):
            if i in self.used_rows:
                continue
            yes = True
            for j in range(5):
                el = self.board_container[i][j]
                if self.board_mapping(i, j) != tile_type:
                    if el > 0 and math.floor(el + 0.00001) != 1:
                        yes = False
                else:
                    if math.floor(el + 0.00001) == 1:
                        yes = False
            if yes:
                avail.append(i)
        return avail

    def set_tile(self, tile_type, num_tiles, row):
        penalty = 0
        col = self.tile_mapping(tile_type, row)
        self.used_rows.append(row)
        if num_tiles >= self.ROWWEIGHT[row]:
            self.board_container[row][col] = 1
            penalty = num_tiles - self.ROWWEIGHT[row]
        else:
            self.board_container[row][col] += (num_tiles / self.ROWWEIGHT[row])
        return penalty

    def check_fullrow(self):
        game_end = False
        for r in self.board_container:
            i = 0
            while not game_end and i <= 4 and r[i] == 1:
                if i == 4:
                    game_end = True
                    break
                else:
                    i += 1
        return game_end;

    def calculate_score(self):
        score = 0
        self.used_rows = []
        for x in range(5):
            for y in range(5):
                if math.floor(self.board_container[x][y] + 0.00001) == 1 and self.completed_board[x][y] != 1:
                    in_a_row = self._traverse_row(x, y)
                    in_a_col = self._traverse_col(x, y)
                    if in_a_row > 0 and in_a_col > 0:
                        score += 1
                    score += 1 + in_a_row + in_a_col
                    self.complete_board_at(x, y)
                    break
                elif math.floor(self.board_container[x][y] + 0.00001) != 1 and self.board_container[x][y] > 0:
                    self.used_rows.append(x)
                    break
        return score

    def calculate_bonus_score(self):
        # full rows bonus
        num_fullrows = 0
        for x in range(5):
            for y in range(5):
                if math.floor(self.board_container[x][y] + 0.00001) != 1:
                    break
                elif y == 4:
                    num_fullrows += 1

        # full cols bonus
        num_fullcols = 0
        for i in range(5):
            if self._traverse_col(0, i) == 5:
                num_fullcols += 1

        # same type bonus
        tiletype_tally = {
            Tile.WATER: 0,
            Tile.CHEESE: 0,
            Tile.FIRE: 0,
            Tile.BLACK: 0,
            Tile.SNOW: 0,
        }
        for i in range(5):
            for j in range(5):
                if math.floor(self.board_container[i][j] + 0.00001) == 1:
                    tiletype_tally[self.board_mapping(i, j)] += 1

        num_fulltypes = 0
        for v in tiletype_tally.values():
            if (v == 5):
                num_fulltypes += 1

        return num_fullrows * 2 + num_fullcols * 7 + num_fulltypes * 10

    def _traverse_row(self, x, y):
        score = 0
        i = x - 1
        while i >= 0 and self.completed_board[i][y] == 1:
            score += 1
            i -= 1
        i = x + 1
        while i < 5 and self.completed_board[i][y] == 1:
            score += 1
            i += 1
        return score

    def _traverse_col(self, x, y):
        score = 0
        j = y - 1
        while j >= 0 and self.completed_board[x][j] == 1:
            score += 1
            j -= 1
        j = y + 1
        while j < 5 and self.completed_board[x][j] == 1:
            score += 1
            j += 1
        return score

    def complete_board_at(self, row, col):
        self.completed_board[row][col] = 1
