import unittest
from triangle_plate import TrianglePlate
from tile_type import TileType


class TrianglePlateTest(unittest.TestCase):
    plate = TrianglePlate()

    def add_two_red_tiles_should_be_put_into_board(self):
        self.plate.add(3, TileType.RED, 2)
        print(self.plate.grids[1])
        assert self.plate.grids[1].quantity == 2 and self.plate.grids[1].type == TileType.RED


if __name__ == '__main__':
    unittest.main()
