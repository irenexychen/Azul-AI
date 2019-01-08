from board import Board
from triangle_plate import TrianglePlate
from tile_type import TileType
from table import Table
import uuid


class Player:
    name = "guest"
    id = ""
    scores = 0

    def __init__(self, table: Table):
        self.id = str(uuid.uuid4())
        self.az_board = Board()
        self.az_plate = TrianglePlate()
        self.az_table = table

    def round_scores(self):
        return self.scores

    def play(self):
        color = input("What color you want to choose Blue, Yellow, Red, blacK or White?")
        amount = int(input("How many you want to get?"))
        row = input("Which row you want to put?")
        switcher = {
            "B": TileType.BLUE,
            "Y": TileType.YELLOW,
            "R": TileType.RED,
            "K": TileType.BLACK,
            "W": TileType.WHITE,
            "b": TileType.BLUE,
            "y": TileType.YELLOW,
            "r": TileType.RED,
            "k": TileType.BLACK,
            "w": TileType.WHITE
        }
        self.az_plate.add(row, switcher[color], amount)
        return row, switcher[color], amount

    def is_last_round(self):
        return self.az_board.has_one_full_row()

    def move_tile_to_board(self):
        pass

    def calculate_scores_after_round(self):
        # TODO calculate scores
        self.az_plate.calculate_penalty()
