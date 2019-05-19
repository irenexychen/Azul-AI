import random

from tile import Tile
from exceptions import InvalidMoveException

bag = {
	Tile.FIRE:		20,
	Tile.WATER:		20,
	Tile.CHEESE:	20,
	Tile.BLACK:		20,
	Tile.SNOW:		20
}

discard = {
	Tile.FIRE:		0,
	Tile.WATER:		0,
	Tile.CHEESE:	0,
	Tile.BLACK:		0,
	Tile.SNOW:		0
}

class Pool:
	def __init__(self):
		global bag
		global discard

		self.num_factories = 5
		self.tiles_per_factory = 4
		self.middle = [Tile.NULL]
		self.factories = []

		for f in range(self.num_factories):
			self.factories.append([])
			for t in range(self.tiles_per_factory):
				# replace bag with discard if empty
				if (sum(bag.values()) == 0):
					temp = bag
					bag = discard
					discard = temp
				empty = set(filter(lambda tile: bag[tile] == 0, bag)).union({Tile.NULL})
				new_tile = random.choice(list(set(Tile) - empty))
				self.factories[f].append(new_tile)
				bag[new_tile] -= 1


	# loc = 0 -> draw from middle
	# loc = 1 - 5 -> draw from factories
	def draw(self, loc, tile):
		if loc < 0 or loc > self.num_factories + 1:
			raise InvalidMoveException
		if loc == 0:
			grabbed_tiles = list(filter(lambda test: test == tile, self.middle))
			if not grabbed_tiles:
				raise InvalidMoveException
			if tile != Tile.NULL and Tile.NULL in self.middle:
				grabbed_tiles.append(Tile.NULL)
			for t in grabbed_tiles:
				self.middle.remove(t)
		else:
			grabbed_tiles = list(filter(lambda test: test == tile, self.factories[loc - 1]))
			if not grabbed_tiles:
				raise InvalidMoveException
			for t in grabbed_tiles:
				self.factories[loc - 1].remove(t)
			self.middle.extend(self.factories[loc - 1])
			self.factories[loc - 1] = []

		return grabbed_tiles

	# determines if the pool is empty
	def is_empty(self):
		for factory in self.factories:
			if factory:
				return False
		if self.middle:
			return False
		return True
