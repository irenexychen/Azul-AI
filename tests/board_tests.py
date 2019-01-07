from unittest import TestCase
from board import Board
from tile_type import TileType


class TestBoard(TestCase):
    game_board = Board()

    def test_put_onto_board(self):
        self.game_board.put_onto_board(3, TileType.RED)
        assert self.game_board.grids[3][0].type == TileType.RED
        assert self.game_board.grids[3][0].quantity == 1

    def test_calculate_scores(self):
        self.game_board.reset()
        self.game_board.put_onto_board(3, TileType.RED)
        self.game_board.calculate_scores()
        assert self.game_board.get_scores() == 1

        self.game_board.put_onto_board(3, TileType.BLACK)
        self.game_board.calculate_scores()
        assert self.game_board.get_scores() == 2
