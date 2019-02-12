
import numpy as np

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
		move = get_valid_piece(self.go_board, self._move_generator())
		if move is not None:
			self.board.apply_move(move)
		return move

	def _move_generator(self):
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


class IdiotBot:
	#plays random move
	
	def __init__(self, model, processor):
		super(RandomizedKerasBot, self).__init__(model=model, processor=processor)



