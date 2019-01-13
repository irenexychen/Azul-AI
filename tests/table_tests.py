from unittest import TestCase
from table import Table
from tile_type import TileType


class TestTable(TestCase):

    def test_fetch_tile(self):
        game_table = Table()
        game_table.round_boxes = [[0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [int(TileType.RED), int(TileType.YELLOW), int(TileType.YELLOW),
                                   int(TileType.YELLOW)],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]]

        game_table.round_boxes_by_number = [{4: [], 3: [], 2: [], 1: []},
                                            {4: [], 3: [], 2: [], 1: []},
                                            {4: [], 3: [int(TileType.YELLOW)], 2: [], 1: [int(TileType.RED)]},
                                            {4: [], 3: [], 2: [], 1: []},
                                            {4: [], 3: [], 2: [], 1: []}]

        game_table.round_boxes_by_color = [
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0, int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0, int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 1, int(TileType.WHITE): 0,
             int(TileType.YELLOW): 3},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0, int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0},
            {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0, int(TileType.WHITE): 0,
             int(TileType.YELLOW): 0}, ]

        game_table.adjust_fetched_tiles(2, TileType.YELLOW, 2)

        self.assertEqual(game_table.round_boxes[2][0], int(TileType.NONE))
        self.assertEqual(game_table.round_boxes[2][1], int(TileType.NONE))
        self.assertEqual(game_table.round_boxes[2][2], int(TileType.NONE))
        self.assertEqual(game_table.round_boxes[2][3], int(TileType.NONE))

        self.assertLess(len(game_table.round_boxes_by_number[2][1]), 1)
        self.assertEqual(game_table.round_boxes_by_color[2][int(TileType.RED)], 0)

        self.assertEqual(game_table.pool[TileType.YELLOW], 1)

        self.assertIs(game_table.has_tile(), True)

    def test_fill_boxes(self):
        game_table = Table()
        game_table.fill_boxes()
        self.assertIs(game_table.has_tile(), True)
