

# convert saved data to usable board and pool structure for training

# may possibly be not needed

class Node:

''' note: Node doesn't know the game it belongs to, but knows its board properties '''


class TreeNode: 

''' note: Node that knows its position in the Game sequence.
		  list-like container

		  properties: need to be indexed, sliced, and iterated over like a list
'''

	def __init__(self, parent, properties):
		self.owner = #game owner
		self.parent = #previous board state
		self._children = #next possible moves/states of game
		Node.__init__(self, properties) #does it need parent._presenter private data???? idk




class GameFormat:

''' Game tree made of TreeNodes '''