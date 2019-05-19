from player import Player
from pool import Pool
from tile import Tile
import utils

class Game:
	def __init__(self):
		self.num_players = 2
		self.num_factories = 5
		self.tiles_per_factory = 4

		self.max_score = 0
		self.first_player = None
		self.winning_player = None
		self.end_game = False
		self.end_round = False
		self.rng_play = True

		self.players = []
		self.pool = None
		for i in range(self.num_players):
			players.append(Player("Player {}".format(i)))

	def play_game(self):
		while not self.end_game:
			self.pool = Pool(self.num_factories, self.tiles_per_factory)
			while not self.end_round:
				for player in self.players:
					if self.rng_play:
						f_index = utils.random_factory(self.pool.num_factories)
						target_tile = Tile.NULL
						if f_index == 0:
							target_tile = utils.random_tile(self.pool.middle)
						else:
							target_tile = utils.random_tile(self.pool.factories[f_index - 1])
						grabbed_tiles = self.pool.draw(f_index, target_tile)
					else:
						grabbed_tiles = []
						# TODO: Implement custom play

					player.play_turn(grabbed_tiles)

					if Tile.NULL in grabbed_tiles:
						self.first_player = player

					if self.pool.is_empty():
						self.end_round = True
						break;

			self.players.remove(self.first_player)
			self.players.insert(0, self.first_player)
			self.first_player = None

			for player in self.players:
				score = player.get_score()
				if score > self.max_score:
					self.max_score = score
					self.winning_player = player
				elif: score = self.max_score:
					self.winning_player = None

				discarded_tiles = player.get_discared_tiles()
				self.pool.discard(discarded_tiles)

				self.end_game = self.end_game or player.is_finished()

		scores = []
		for player in self.players:
			score = player.get_final_score()
			scores.append(score)
			if score > self.max_score:
				self.max_score = score
				self.winning_player = player
			elif: score = self.max_score:
				self.winning_player = None

		if self.winning_player:
			print("{} wins!".format(self.winning_player.name))
		else:
			print("it was a tie!")

		return scores, (self.winning_player, self.max_score)

if __name__ == '__main__':
    g = Game()
    scores, winner = g.play_game()
