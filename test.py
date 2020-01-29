import unittest
import tictactoe as BoardClass

class Test_check_inbounds(unittest.TestCase):
	game_board = BoardClass.Board()	

	def test_both_valid_equal(self):
		self.assertTrue(self.game_board.check_inbounds(2,2))

	def test_both_valid(self):
		self.assertTrue(self.game_board.check_inbounds(2,1))

	def test_both_invalid(self):
		self.assertFalse(self.game_board.check_inbounds(4,4))

	def test_one_valid_one_invalid(self):
		self.assertFalse(self.game_board.check_inbounds(4,1))

class Test_check_unoccupied(unittest.TestCase):	
	
	board = BoardClass.Board()	

	def test_unoccupied(self):

		self.board.game_board[2][2] = '0'
		self.assertTrue(self.board.check_unoccupied(2,2))

	def test_occupied(self):
		self.board.game_board[2][2] = 'X'

		self.assertFalse(self.board.check_unoccupied(2,2))


class Test_check_valid_move(unittest.TestCase):	
	
	board = BoardClass.Board()	

	def test_valid_move(self):
		self.assertTrue(self.board.check_valid_move(2,2))

	def test_valid_occupied(self):
		self.board.game_board[2][2] = 'X'

		self.assertFalse(self.board.check_valid_move(2,2))

	def test_invalid(self):
		self.assertFalse(self.board.check_valid_move(3,3))

class Test_mark_square(unittest.TestCase):

	board = BoardClass.Board()

	def Test_mark_X(self):
		
		self.board.mark_square(2,2,'X')

		self.assertEqual(self.board.game_board[2][2], 'X')

	def Test_mark_O(self):
		
		self.board.mark_square(2,2,'O')

		self.assertEqual(self.board.game_board[2][2], 'O')

class Test_check_turn(unittest.TestCase):

	board = BoardClass.Board()

	def Test_X_Turn(self):
		
		self.count = 0
		self.assertTrue(self.board.check_turn(self.count))

	def Test_O_Turn(self):

		self.count = 3
		self.assertFalse(self.board.check_turn(self.count))




		
		


if __name__ == '__main__':
	unittest.main()
