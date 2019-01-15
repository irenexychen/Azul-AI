from unittest import TestCase
from ai_player import AiPlayer
from table import Table
from tile_type import TileType


class TestAiPlayer(TestCase):
    az_table = Table()
    ai_player = AiPlayer("TestAiPlayer", az_table)

    ai_player.az_table.round_boxes = [[int(TileType.WHITE), int(TileType.WHITE), int(TileType.BLACK),
                                       int(TileType.YELLOW)],
                                      [0, 0, 0, 0],
                                      [int(TileType.RED), int(TileType.YELLOW), int(TileType.YELLOW),
                                       int(TileType.YELLOW)],
                                      [int(TileType.BLUE), int(TileType.YELLOW), int(TileType.BLUE),
                                       int(TileType.RED)],
                                      [int(TileType.BLACK), int(TileType.BLACK), int(TileType.BLUE),
                                       int(TileType.RED)]]

    ai_player.az_table.round_boxes_by_number = [
        {4: [], 3: [], 2: [int(TileType.WHITE)], 1: [int(TileType.BLACK), int(TileType.YELLOW)]},
        {4: [], 3: [], 2: [], 1: []},
        {4: [], 3: [int(TileType.YELLOW)], 2: [], 1: [int(TileType.RED)]},
        {4: [], 3: [], 2: [int(TileType.BLUE)],
         1: [int(TileType.YELLOW), int(TileType.RED)]},
        {4: [], 3: [], 2: [int(TileType.BLACK)],
         1: [int(TileType.RED), int(TileType.BLUE)]}]

    ai_player.az_table.round_boxes_by_color = [
        {int(TileType.BLUE): 0, int(TileType.BLACK): 1, int(TileType.RED): 0, int(TileType.WHITE): 2,
         int(TileType.YELLOW): 1},
        {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 0, int(TileType.WHITE): 0,
         int(TileType.YELLOW): 0},
        {int(TileType.BLUE): 0, int(TileType.BLACK): 0, int(TileType.RED): 1, int(TileType.WHITE): 0,
         int(TileType.YELLOW): 3},
        {int(TileType.BLUE): 2, int(TileType.BLACK): 0, int(TileType.RED): 1, int(TileType.WHITE): 0,
         int(TileType.YELLOW): 1},
        {int(TileType.BLUE): 1, int(TileType.BLACK): 2, int(TileType.RED): 1, int(TileType.WHITE): 0,
         int(TileType.YELLOW): 0}, ]

    def test_find_next_move(self):
        result = self.ai_player.find_next_move()
        result.print_tiles()

        self.assertEqual(result.source_box, 2)
        self.assertEqual(result.destination_row, 1)
        self.assertEqual(result.type, int(TileType.YELLOW))
        self.assertEqual(result.quantity, 3)

    def test_get_most_tiles(self):
        result = self.ai_player.get_most_tiles_from_box()
        result.print_tiles()

        self.assertEqual(result.source_box, 2)
        self.assertEqual(result.type, int(TileType.YELLOW))
        self.assertEqual(result.quantity, 3)
