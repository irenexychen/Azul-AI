import unittest
from triangle_plate import TrianglePlate
from tile_type import TileType


class TrianglePlateTest(unittest.TestCase):
    plate = TrianglePlate()

    def test_add_red_tiles_should_be_put_into_board(self):
        self.plate.add(3, TileType.RED, 2)
        assert self.plate.grids[3].quantity == 2 and self.plate.grids[3].type == TileType.RED

        self.plate.add(3, TileType.RED, 3)
        assert self.plate.grids[3].quantity == 3 and self.plate.grids[3].type == TileType.RED

    def test_calculate_penalty(self):
        self.plate.reset()
        self.plate.add(3, TileType.RED, 2)
        self.plate.calculate_penalty()
        assert self.plate.get_penalty_points() == 0

        self.plate.add(3, TileType.RED, 5)
        self.plate.calculate_penalty()

        assert self.plate.get_penalty_points() == 6


if __name__ == '__main__':
    unittest.main()
