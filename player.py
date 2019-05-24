from tile import Tile
from board import Board
from pool import Pool
import utils

class Player:
	def __init__(self, name):
		self.num_rows = 5

		self.name = name
		self.board = Board()
		self.score = 0
		self.penalty = 0

	def play_turn(self, grabbed_tiles, rng_play):
		if (Tile.NULL in grabbed_tiles):
			self.penalty += 1
			grabbed_tiles.remove(Tile.NULL)
		if grabbed_tiles:
			num_tiles = len(grabbed_tiles)
			tile_type = grabbed_tiles[0]
			if rng_play:
				row = utils.random_row(self.num_rows)
			else:
				row = 0
				# TODO: Implement custom play
			self.penalty += self.board.set_tile(tile_type, num_tiles, row)

	def is_finished(self):
		return self.board.check_fullrow()

	def get_score(self):
		penalty_score = 0
		for i in range(self.penalty):
			if i < 2:
				penalty_score += 1
			elif i < 5:
				penalty_score += 2
			else:
				penalty_score += 3
		self.penalty = 0
		self.score += round(self.board.calculate_score() - penalty_score)
		return self.score

	def get_final_score(self):
		return round(self.get_score() + self.board.calculate_bonus_score())
