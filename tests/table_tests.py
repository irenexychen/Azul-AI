from unittest import TestCase
from table import Table
from tile_type import TileType


class TestTable(TestCase):
    game_table = Table()

    def test_flush_tile(self):
        self.game_table.round_boxes = [[0, 0, 0, 0],
                                       [0, 0, 0, 0],
                                       [0, int(TileType.YELLOW), int(TileType.YELLOW), int(TileType.YELLOW)],
                                       [0, 0, 0, 0],
                                       [0, 0, 0, 0]]

        self.game_table.move_tile_to_pool(2, TileType.YELLOW, 2)

        assert self.game_table.round_boxes[2][1] == int(TileType.NONE)
        assert self.game_table.round_boxes[2][2] == int(TileType.NONE)
        assert self.game_table.round_boxes[2][3] == int(TileType.NONE)
        assert self.game_table.pool[TileType.YELLOW] == 1
        assert not self.game_table.has_tile()


def test_fill_boxes(self):
    self.game_table.fill_boxes()
    assert self.game_table.has_tile()
