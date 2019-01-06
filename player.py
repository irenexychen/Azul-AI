from board import Board
from triangle_plate import TrianglePlate


class Player:
    name = "guest"
    scores = 0

    def __init__(self):
        self.az_board = Board()
        self.az_plate = TrianglePlate()

    def round_scores(self):
        return self.scores

    def play(self):
        color = input("What color you want to choose?")
        amount = input("How many you want to get?")
        row = input("Which row you want to put?")
        # TODO change color to enum TileType

        self.az_plate.add(row, color, amount)
        return row, color, amount

    def is_last_round(self):
        return self.az_board.has_one_full_row()

    def move_tile_to_board(self):
        pass

    def calculate_score_after_round(self):
        pass
