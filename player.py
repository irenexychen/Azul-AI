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

	def is_finished():
		return self.board.check_fullrow()

	def get_score():
		return self.board.calculate_score()

	def get_final_score():
		return self.board.calculate_score() + self.board.calculate_bonus_score()
