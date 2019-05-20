from tile import Tile

# board wall, belongs to player
# x row
# y column
# ROWWEIGHT helps simulate triangles

class Board:
	BOARDMAPPING = [[Tile.WATER   , Tile.CHEESE , Tile.FIRE   , Tile.BLACK  , Tile.SNOW ],
					[Tile.SNOW   , Tile.WATER   , Tile.CHEESE , Tile.FIRE   , Tile.BLACK ],
					[Tile.BLACK  , Tile.SNOW   , Tile.WATER   , Tile.CHEESE , Tile.FIRE  ],
					[Tile.FIRE   , Tile.BLACK  , Tile.SNOW   , Tile.WATER   , Tile.CHEESE],
					[Tile.CHEESE , Tile.FIRE   , Tile.BLACK  , Tile.SNOW   , Tile.WATER] ]
	TILEMAPPING = {
		Tile.WATER:		[(0,0), (1,1), (2,2), (3,3), (4,4)],
		Tile.CHEESE:	[(0,1), (1,2), (2,3), (3,4), (4,0)],
		Tile.FIRE:		[(0,2), (1,3), (2,4), (3,0), (4,1)],
		Tile.BLACK:		[(0,3), (1,4), (2,0), (3,1), (4,2)],
		Tile.SNOW:		[(0,4), (1,0), (2,1), (3,2), (4,3)]
	}
	ROWWEIGHT = [1,2,3,4,5]

	def __init__(self):
		self.board_container = [[0] * 5,] * 5
		self.prev_board_state = [[0] * 5,] * 5
		self.score = 0

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
		for x in range(5):
			for y in range(5):
				if self.board_container[x][y] != self.prev_board_state[x][y]:
					self.score += self._traverse_row(x,y)
					self.score += self._traverse_col(x,y)
		self.save_to_prev_board_state()
		return self.score

	def calculate_bonus_score(self):
		# full rows bonus
		num_fullrows = 0
		for r in self.board_container:
			for y in range(5):
				if (r[y] != 1):
					break
				elif (y == 4):
					num_fullrows += 1
		
		# full cols bonus
		num_fullcols = 0
		for i in range(5):
			if _traverse_col(0,i) == 5:
				num_fullcols += 1

		# same type bonus
		tiletype_tally = {
				Tile.WATER: 0,
				Tile.CHEESE: 0,
				Tile.FIRE: 0,
				Tile.BLACK:	0,
				Tile.SNOW: 0,
		}
		for i in range(5):
			for j in range(5):
				tiletype_tally[self.board_mapping(i,j)] += 1
		num_fulltypes = 0
		for k, v in tiletype_tally:
			if (v == 5):
				num_fulltypes += 1

		return num_fullrows * 2 + num_fullcols * 7 + num_fulltypes * 10

	def _traverse_row(self, x, y):
		score = 1
		i = x - 1
		while (i >= 0 and self.board_container[i][y] == 1): 
			score += self.board_container[i][y]
			i -= 1
		i = x + 1
		while (i <= 4 and self.board_container[i][y] == 1):
			score += self.board_container[i][y]
			i += 1
		return score

	def _traverse_col(self, x, y):
		score = 1
		j = y - 1
		while (i >= 0 and self.board_container[x][j] == 1): 
			score += self.board_container[x][j]
			j -= 1
		j = y + 1
		while (j <= 4 and self.board_container[x][j] == 1):
			score += self.board_container[x][j]
			j += 1
		return score

	def save_to_prev_board_state(self):
		self.prev_board_state = self.board_container
