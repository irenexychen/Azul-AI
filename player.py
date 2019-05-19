from tile import Tile
from board import Board
from pool import Pool

class Player:

	def __init__(self, name):
		self.name = name
		self.board = Board()
		self.score = 0




	def play_turn(self, grabbed_tiles, row):
		# list of grabbed tiles to set
		num_tiles = len(grabbed_tiles)
		x = row
		y = self.board.board_mapping()

		self.board.set_tile()


