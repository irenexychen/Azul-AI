from tile_type import TileType


class Tile:
    type = TileType.NONE
    quantity = 0

    def __init__(self, tile_type, amount):
        self.type = tile_type
        self.quantity = amount
