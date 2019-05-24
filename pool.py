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

class Pool:
	def __init__(self, num_factories, tiles_per_factory):
		global bag

		self.num_factories = num_factories
		self.tiles_per_factory = tiles_per_factory
		self.middle = [Tile.NULL]
		self.factories = []

		for f in range(self.num_factories):
			self.factories.append([])
			for t in range(self.tiles_per_factory):
				empty = set(filter(lambda tile: bag[tile] == 0, bag)).union({Tile.NULL})
				new_tile = random.choice(list(set(Tile) - {Tile.NULL}))
				self.factories[f].append(new_tile)

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
