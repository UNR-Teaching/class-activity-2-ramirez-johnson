""" Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
          and you make use of relevant object-oriented design principles.
"""


class Board(object):

	def __init__(self):
		"""
        Initializes the Board of size 3x3
        """
		self.game_board = [['0','0','0'],['0','0','0'],['0','0','0']]
		self.count = 0
		self.x_turn = True
	

		pass

	def mark_square(self, column, row, player):
		"""
		Marks a square at coordinate (column, row) for player

		:param column: (int) the 0-indexed column of the Board to mark
		:param row: (int) the 0-indexed row of the Board to mark
		:param player: (str) the X or O representation of which player to mark in square

		:return: ????
		"""
		
		if self.check_valid_move(row, column):
			self.game_board[row][column] = player
	

		pass

	def has_winner(self):
		"""
		Checks to see if there is a current winner of the game

		:return: ????
		"""

		pass

	def play_game(self):
		"""
	 	Takes moves from raw_input as comma-separated list in form (column, row, player)
		and makes a move. When a winner has been determined, the game ends
		    
		:return: (str) the letter representing the player who won
		"""
        
		pass

	def check_turn(self, count):
	
		if self.count % 2 == 0:
			return True
		else:
			return False
		
		pass

	def check_inbounds(self, row, column):

		if row < 3 and column < 3:
			return True
		else:
			return False

		pass

	def check_unoccupied(self, row, column):

		if self.game_board[row][column] == '0':
			return True
		else:
			return False

		pass

	def check_valid_move(self, row, column):

		inbounds = self.check_inbounds(row, column)
		

		if inbounds:
		
			unoccupied = self.check_unoccupied(row, column)
			if unoccupied:
				return True
			else:
				return False			
		else:
			return False


        
if __name__ == '__main__':
	board = Board()
	winner = board.play_game()
	print("{} has won!".format(winner))
