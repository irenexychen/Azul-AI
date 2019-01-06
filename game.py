from triangle_plate import TrianglePlate
from table import Table
from player import Player
from ai_player import AiPlayer


class Game:

    def __init__(self):
        self.az_player = Player()
        self.ai_player = AiPlayer()
        self.az_plate = TrianglePlate()
        self.az_table = Table()

    def play_game(self):
        pass
