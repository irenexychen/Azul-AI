from board import Board
from triangle_plate import TrianglePlate
from tile_type import TileType
from table import Table
import uuid


class Player:
    name = "guest"
    id = ""
    scores = 0

    def __init__(self, name, table: Table):
        self.name = name
        self.id = str(uuid.uuid4())
        self.az_board = Board()
        self.az_plate = TrianglePlate()
        self.az_table = table

    def round_scores(self):
        return self.scores

    def play(self):
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
        source_row = int(input("From which round box you want to take tiles?"))
        color = input("What color you want to choose, Blue, Yellow, Red, blacK or White?")
        print("Box by color:", self.az_table.round_boxes_by_color[source_row])
        amount = self.az_table.round_boxes_by_color[source_row][int(switcher[color])]
        print("You toke %d %s" % (amount, switcher[color]))
        destination_row = int(input("Which row you want to put into?"))

        self.az_plate.add(destination_row, switcher[color], amount)
        self.az_table.adjust_fetched_tiles(source_row, switcher[color], amount)
        self.az_plate.print_plate()

    def is_last_round(self):
        return self.az_board.has_one_full_row()

    def move_tiles_to_board(self):
        pass

    def calculate_scores_after_round(self):
        # TODO calculate scores
        self.az_plate.calculate_penalty()
