from random import randint

# Create an empty board
board = []

# Populate the Board
for i in range(0, 3):
    board.append(["-"] * 3)

def print_board(board):
    for row in board:
		print " ".join(row)

def pick_random(board):
	row = randint(0, len(board) - 1)
	col = randint(0, len(board[0]) - 1)
	if board[row][col] == '-':
		board[row][col] = 'O'
	else:
		pick_random(board)

	return board

def is_winner(board, player):
	return ((board[0][0] == player and board[0][1] == player and board[0][2] == player) or #Top Row
		(board[1][0] == player and board[1][1] == player and board[1][2] == player) or #Middle Row
		(board[2][0] == player and board[2][1] == player and board[2][2] == player) or #Bottom Row
		(board[0][0] == player and board[1][0] == player and board[2][0] == player) or #Left Col
		(board[0][1] == player and board[1][1] == player and board[2][1] == player) or #Middle Col
		(board[2][0] == player and board[2][1] == player and board[2][2] == player) or #Left Col
		(board[0][0] == player and board[1][1] == player and board[2][2] == player) or #Left Right Diag
		(board[0][2] == player and board[1][1] == player and board[2][0] == player)) #Right Left Diag

def is_board_full(board):
	free_spots = 0;
	for r in range(0, 3):
		for c in range(0, 3):
			if board[r][c] == '-':
				free_spots = free_spots + 1

	if free_spots == 0:
		return True
	else:
		return False

while True:
	print_board(board)
	print ""

	# Prompt Player for input
	pick_row = int(raw_input("Pick Row (1-3):"))
	pick_col = int(raw_input("Pick Col (1-3):"))
	print ""
	skip = False

	if pick_row-1 not in range(3) or pick_col-1 not in range(3): #check to see if move is in range
		print "Oops, that's not even on the board."
		skip = True
	elif board[pick_row-1][pick_col-1] != '-': #check to see if position is already filled on board
		print "You guessed that one already."
		skip = True
	else:
		board[pick_row-1][pick_col-1] = "X"

	if skip == False:

		print_board(board)
		print ""
		if is_winner(board, 'X'):
			print "You Win!"
			break
		if is_board_full(board):
			print "It's a Tie!"
			break

		pick_random(board)
		if is_winner(board, 'O'):
			print_board(board)
			print ""
			print "I Win!"
			break

		if is_board_full(board):
			print "It's a Tie!"
			break