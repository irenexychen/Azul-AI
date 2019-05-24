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
			self.players.append(Player("Player {}".format(i + 1)))

	def play_game(self):
		round_num = 1
		while not self.end_game:
			taken = set()
			cycle = 1

			print("#################### ROUND {} #####################\n".format(round_num))
			self.pool = Pool(self.num_factories, self.tiles_per_factory)
			while not self.end_round:
				cycle += 1
				print("#################### CYCLE {} #####################\n".format(cycle))
				for factory in self.pool.factories:
					print(factory)
				print(self.pool.middle)
				print("#################### CYCLE {} #####################\n\n".format(cycle))

				for player in self.players:
					while not self.pool.is_empty():
						try:
							remaining_factories = list(set(range(self.num_factories + 1)) - taken)
							if self.rng_play:
								f_index = utils.random_factory(remaining_factories)
								target_tile = Tile.NULL
								if f_index == 0:
									target_tile = utils.random_tile(self.pool.middle)
								else:
									target_tile = utils.random_tile(self.pool.factories[f_index - 1])
								grabbed_tiles = self.pool.draw(f_index, target_tile)
							else:
								f_index = 0
								target_tile = Tile.NULL
								grabbed_tiles = []
								# TODO: Implement custom play
							break
						except IndexError:
							pass

					print("{} took {} from factory {}".format(player.name, target_tile, f_index))

					if Tile.NULL in grabbed_tiles:
						print("{} is going first next round".format(player.name))
						self.first_player = player

					player.play_turn(grabbed_tiles, self.rng_play)

					if self.pool.is_empty():
						self.end_round = True
						break;

			print("#################### ROUND {} #####################\n".format(round_num))
			round_num += 1

			self.players.pop(self.players.index(self.first_player))
			self.players.insert(0, self.first_player)
			self.first_player = None
			self.end_round = False

			for player in self.players:
				score = player.get_score()
				print("{} has {} points".format(player.name, score))
				if score > self.max_score:
					self.max_score = score
					self.winning_player = player
				elif score == self.max_score:
					self.winning_player = None

				self.end_game = self.end_game or player.is_finished()

		print("#################### END OF GAME #####################\n")
		scores = []
		for player in self.players:
			score = player.get_final_score()
			print("{} has {} points".format(player.name, score))
			scores.append(score)
			if score > self.max_score:
				self.max_score = score
				self.winning_player = player
			elif score == self.max_score:
				self.winning_player = None

		if self.winning_player:
			print("{} wins!".format(self.winning_player.name))
		else:
			print("it was a tie!")

		return scores, (self.winning_player, self.max_score)

if __name__ == '__main__':
    g = Game()
    scores, winner = g.play_game()
