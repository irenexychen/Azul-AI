from unittest import TestCase
from player import Player
from table import Table


class TestPlayer(TestCase):
    test_table = Table()
    guest_player = Player("TestUser",test_table)

    def test_is_last_round(self):
        self.fail()

    def test_move_tile_to_board(self):
        self.fail()

    def test_calculate_score_after_round(self):
        self.fail()
