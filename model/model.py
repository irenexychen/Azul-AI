
import numpy as np
import random
import copy
from itertools import chain
#load + process data TODO


#azul model: predict moves using processed data 

class AzulModel:
	''' Tracks board and middle pool'''
	
	def __init__(self):
		#init deep network
		self.model = #neural model
	
	def set_game(self, board, pool):
		self.board = copy.deepcopy(board)
		self.pool = copy.deepcopy(pool)

	def apply_move(self, board, pool, move):
		# apply human move
		return NotImplemented

	def choose_best_move(self, board, pool):
		return NotImplemented



class KerasBot:
	''' Takes top_n best predicted moves of a keras model, check in pool if move is possible
		Go down the list, if none are available, choose random move '''

	def __init__(self, model, processor, top_n=10):
		super(KerasBot, self).__init__(model=model, processor=processor)
		self.top_n = top_n

	def apply_move(self, board, pool, move):
		# apply human move
		self.board.apply_move(move)

	def choose_best_move(self, board, pool):
		move = get_valid_piece(self.board, self._move_generator())
		if move is not None:
			self.board.apply_move(move)
		return move

	def _move_generator(self):
		return chain {self._move_from_model(), self.generate_random(self.all_possible_pieces(board))}

	def _move_from_model(self):
		# Turn the board into a feature vector, then label
		vec, label = self.processor.label(self.board)
		vec = vec.reshape((1, vec.shape[0], vec.shape[1], vec.shape[2]))

		# Generate bot move.
		predicted = np.squeeze(self.model.predict(vec))
		sorted_predicteds = predicted.argsort()[-self.top_n:][::-1]

		for pred in sorted_predicteds:
			#return board coordinates of move
			prediction = int(pred)
			pred_row = prediction // 5
			pred_col = prediction % 5
			pred_move = [(pred_row, pred_col) , pred_colour]		#need to include colour/type somewhere

			yield pred_move




class RandomizedKerasBot:
	''' Keras Bot with a hint of randomization/noise, 
		takes weighted sample, or picks random if none of the samples are possible moves in the pool'''

	def __init__(self, model, processor, top_n=10):
		super(RandomizedKerasBot, self).__init__(model=model, processor=processor)

	def apply_move(self, board, pool, move):
		# apply human move
		self.board.apply_move(move)

	def choose_best_move(self, board, pool):
		move = get_valid_piece(self.board, self._move_generator(), pool)
		if move is not None:
			self.board.apply_move(move)
		return move

	def _move_generator(self):
		return self.generate_random(self.all_possible_pieces(board))

	def _move_from_model(self):
		# Turn the board into a feature vector, then label
		vec, label = self.processor.label(self.board)
		vec = vec.reshape((1, vec.shape[0], vec.shape[1], vec.shape[2]))

		# Generate n_samples of bot moves from Keras model
		n_samples = 20
		predicted = np.squeeze(self.model.predict(vec))
		# NOTE: Cube the predictions to increase the difference between the best and worst moves, as an adjustment factor
		predicted = predicted * predicted * predicted
		predicted /= predicted.sum()
		moves = np.random.choice(5 * 5, size=n_samples, replace=False, p=pred)
		
		for pred in moves:
			prediction = int(pred)
			pred_row = prediction // 5
			pred_col = prediction % 5
			pred_move = [(pred_row, pred_col) , pred_colour]		#need to include colour/type somewhere

			yield pred_move



class IdiotBot:
	'''shitty bot that plays random move'''
	
	def __init__(self, model, processor):
		super(IdiotBot, self).__init__(model=model, processor=processor)

	def apply_move(self, board, pool, move):
		# apply human move
		remove_move_from_pool(move, pool)
		self.board.apply_move(move)

	def choose_best_move(self, board, pool): # "best" move is random move
		move = get_first_valid_piece(self.board, generate_random(all_possible_pieces(board)))
		if move is not None: 
			self.board.apply_move(move)
		return move




# Other helper functions:
def remove_move_from_pool(move, pool):
	#find move in pool
	#remove 
	#TODO


def get_valid_piece(board, generated_moves, pool):
	for move in generated_moves:
		if move in pool:
			return move
	return None

def generate_random(moves_list):
	'''Yield all moves in the list in a random order.'''
	moves_list = copy.copy(moves_list)
	random.shuffle(moves_list)
	for move in moves_list:
		yield move

def all_possible_pieces(board):
	'''Return all possible position plays on the board.'''
	possible_plays = []
	for x in range(board.size()):
		for y in range(board[x]):
		if (board[x][y] < 1):
			point = [x,y]
			possible_plays.append(point)
	return possible_plays