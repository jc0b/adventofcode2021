import re

class BingoBoard(object):
	
	board = []

	"""Creates a Bingoboard representation, and returns results of operations on that board."""
	def __init__(self, board):
		super(BingoBoard, self).__init__()
		self.board = board

	def check_diagonal(self):
		left_diag_sum = 0 #\
		right_diag_sum = 0 #/
		count = 0
		for line in self.board:
			left_diag_sum += int(line[count])
			right_diag_sum += int(line[4-count])
		if left_diag_sum == -5 or right_diag_sum == -5:
			return True
		return False

	def check_horizontal(self):
		line_sum = 0
		for i in range(len(self.board)):
			line_sum = 0
			for j in range(len(self.board)):
				line_sum += int(self.board[i][j])
			if line_sum == -5:
				return True
		return False

	def check_vertical(self):
		line_sum = 0
		for i in range(len(self.board)):
			line_sum = 0
			for j in range(len(self.board)):
				line_sum += int(self.board[j][i])
			if line_sum == -5:
				return True
		return False


	def mark(self, drawn_number):
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				if self.board[i][j] == drawn_number:
					self.board[i][j] = -1

	def calculate_sum(self):
		board_sum = 0
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				if self.board[i][j] == -1:
					continue
				else:
					board_sum += int(self.board[i][j])
		return board_sum


		


def part_one():
	input = open('input.txt', 'r')
	Lines = input.readlines()

	bingo_numbers = Lines[0].strip().split(",")
	# return bingo_numbers
	boards = []

	for i, line in enumerate(Lines):
		if i % 2 != 0 and i % 3 == 0:
			board = [] * 5
			for j in range(5):
				board.append(re.split(r"\s{1,2}", Lines[i+j-1].strip()))
			boards.append(BingoBoard(board))


	score = 0
	for number in bingo_numbers:
		for board in boards:
			board.mark(number)
			if(board.check_horizontal() or board.check_vertical()):
				score = max(score, board.calculate_sum() * int(number))
		if score != 0:
			return score

	

def part_two():
	input = open('input.txt', 'r')
	Lines = input.readlines()
	bingo_numbers = Lines[0].strip().split(",")
	boards = []

	for i, line in enumerate(Lines):
		if i % 2 != 0 and i % 3 == 0:
			board = [] * 5
			for j in range(5):
				board.append(re.split(r"\s{1,2}", Lines[i+j-1].strip()))
			boards.append(BingoBoard(board))

	score = 0
	winning_indexes = {}
	for number in bingo_numbers:
		for i, board in enumerate(boards):
			board.mark(number)
			if(board.check_horizontal() or board.check_vertical()) and str(i) not in winning_indexes:
				winning_indexes[str(i)] = board.calculate_sum() * int(number)
	return winning_indexes[list(winning_indexes)[-1]]

if __name__ == '__main__':
	print(f"Highest Possible score: {part_one()}")
	print(f"Last board to win has score: {part_two()}")