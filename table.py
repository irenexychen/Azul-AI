from tile_type import TileType


class Table:
    round_boxes = []
    pool = []

    def __init__(self):
        self.reset()

    def reset(self):
        self.round_boxes = [[TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE],
                            [TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE],
                            [TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE],
                            [TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE],
                            [TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE, TileType.NONE]]

        self.pool = {TileType.BLUE: 0, TileType.BLACK: 0, TileType.RED: 0, TileType.WHITE: 0,
                     TileType.YELLOW: 0}

    def fill_boxes(self):
        for i in range(5):
            # TODO to fill in random
            self.round_boxes[i] = []
            pass

    def fetch_tile(self, i, tile_type_fetched: TileType, fetched_number):
        # TODO remove from bowls
        # TODO add to pool
        pass

    def has_tile(self):
        # TODO check tile both in boxes and pool
        pass
