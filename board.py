from tile_type import TileType
from title import Tile


class Board:
    total_scores = 0
    grids = [[], [], [], [], []]

    def __init__(self):
        self.reset()

    def reset(self):
        self.grids = [[Tile(TileType.BLUE, 0),
                       Tile(TileType.YELLOW, 0),
                       Tile(TileType.RED, 0),
                       Tile(TileType.BLACK, 0),
                       Tile(TileType.WHITE, 0)],
                      [Tile(TileType.WHITE, 0),
                       Tile(TileType.BLUE, 0),
                       Tile(TileType.YELLOW, 0),
                       Tile(TileType.RED, 0),
                       Tile(TileType.BLACK, 0)],
                      [Tile(TileType.BLACK, 0),
                       Tile(TileType.WHITE, 0),
                       Tile(TileType.BLUE, 0),
                       Tile(TileType.YELLOW, 0),
                       Tile(TileType.RED, 0)],
                      [Tile(TileType.RED, 0),
                       Tile(TileType.BLACK, 0),
                       Tile(TileType.WHITE, 0),
                       Tile(TileType.BLUE, 0),
                       Tile(TileType.YELLOW, 0)],
                      [Tile(TileType.YELLOW, 0),
                       Tile(TileType.RED, 0),
                       Tile(TileType.BLACK, 0),
                       Tile(TileType.WHITE, 0),
                       Tile(TileType.BLUE, 0)]]

    def get_scores(self):
        return self.total_scores

    def put_into_board(self, i, new_brick_type: TileType):
        for biscuit in self.grids[i]:
            if biscuit.type == new_brick_type and biscuit.quantity == 0:
                # TODO verify if it is by-reference
                biscuit.quantity = 1
                break

    def calculate_scores(self):
        # TODO
        self.total_scores = 9
