from tile import Tile

# board wall, belongs to player
# x row
# y column
# ROWWEIGHT helps simulate triangles

class Board:
	BOARDMAPPING = [[Tile.BLUE   , Tile.CHEESE , Tile.FIRE   , Tile.BLACK  , Tile.SNOW ],
					[Tile.SNOW   , Tile.BLUE   , Tile.CHEESE , Tile.FIRE   , Tile.BLACK ],
					[Tile.BLACK  , Tile.SNOW   , Tile.BLUE   , Tile.CHEESE , Tile.FIRE  ],
					[Tile.FIRE   , Tile.BLACK  , Tile.SNOW   , Tile.BLUE   , Tile.CHEESE],
					[Tile.CHEESE , Tile.FIRE   , Tile.BLACK  , Tile.SNOW   , Tile.BLUE] ]
	TILEMAPPING = {
		Tile.BLUE:		[(0,0), (1,1), (2,2), (3,3), (4,4)],
		Tile.CHEESE:	[(0,1), (1,2), (2,3), (3,4), (4,0)],
		Tile.FIRE:		[(0,2), (1,3), (2,4), (3,0), (4,1)],
		Tile.BLACK:		[(0,3), (1,4), (2,0), (3,1), (4,2)],
		Tile.SNOW:		[(0,4), (1,0), (2,1), (3,2), (4,3)]
	}
	ROWWEIGHT = [1,2,3,4,5]

	def __init__(self):
		self.board_container = [[0] * 5,] * 5
		self.prev_board_state = [[0] * 5,] * 5

	def board_mapping(self, x, y):
		return self.BOARDMAPPING[x][y]

	def tile_mapping(self, x, Tile):
		return self.TILEMAPPING[x]

	def set_tile(self, x, y, num_tiles):
		if num_tiles >= self.ROWWEIGHT[x]:
			self.board_container[x][y] = 1
			penalty = num_tiles - self.ROWWEIGHT[x]
		else:
			self.board_container[x][y] += num_tiles / self.ROWWEIGHT[x]
		return penalty

	def check_fullrow(self):
		game_end = False
		for r in self.board:
			i = 0
			while (game_end == False and i <= 4 and r[i] == 1):
				if i == 4:
					game_end = True
					break
				else:
					i += 1
		return game_end;



	def calculate_score(self):


