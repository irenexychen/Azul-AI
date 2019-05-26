from tile import Tile
from board import Board
import utils

class Player:
	def __init__(self, name):
		self.name = name
		self.board = Board()
		self.score = 0
		self.penalty = 0

	def play_turn(self, grabbed_tiles, rng_play):
		if Tile.NULL in grabbed_tiles:
			self.penalty += 1
			grabbed_tiles.remove(Tile.NULL)
			print("{} grabbed the null tile and will be going first next round".format(self.name))
		if grabbed_tiles:
			num_tiles = len(grabbed_tiles)
			tile_type = grabbed_tiles[0]
			available_rows = self.board.where_put(tile_type)

			if available_rows:
				if rng_play:
					row = utils.random_row(available_rows)
				else:
					row = 0
					# TODO: Implement custom play
				self.penalty += self.board.set_tile(tile_type, num_tiles, row)
				print("{} placed {} {} tiles in row {} and now has {} penalty tiles".format(self.name, num_tiles, tile_type.value, row, self.penalty))
			else:
				self.penalty += num_tiles
				print("{} placed {} {} tiles in the penalty row and now has {} penalty tiles".format(self.name, num_tiles, tile_type.value,	self.penalty))

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
		print("{} took {} penalty tiles resulting in {} points penalty".format(self.name, self.penalty, penalty_score))
		self.penalty = 0
		self.score += round(self.board.calculate_score()) - penalty_score
		return self.score

	def get_final_score(self):
		self.score += round(self.board.calculate_bonus_score())
		return self.score
