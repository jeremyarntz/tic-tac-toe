from random import randint

# Create an empty board
board = []

wins = [['0 0', '0 1', '0 2'],
		['1 0', '1 1', '1 2'],
		['2 0', '2 1', '2 2'],
		['0 0', '1 0', '2 0'],
		['0 1', '1 1', '2 1'],
		['0 2', '1 2', '2 2'],
		['0 0', '1 1', '2 2'],
		['0 2', '1 1', '2 0']]

# Populate the Board
for i in range(0, 3):
    board.append(["-"] * 3)

def print_board(board):
    for row in board:
		print " ".join(row)

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

def check_moves(wins, board):
	moves = {}
	for win in wins:
		row_x = 0;
		row_o = 0;
		row_empty = []
		for space in win:
			space_coords = space.split(' ');
			space_row = int(space_coords[0])
			space_col = int(space_coords[1])
			space_value = board[space_row][space_col]

			if space_value == 'X':
				row_x = row_x + 1
			elif space_value == 'O':
				row_o = row_o + 1
			else: #add blank spots to list
				spot = '%s %s' % (space_coords[0],space_coords[1])
				#if spot not in row_empty:
				row_empty.append(spot)

		if len(row_empty) > 0:

			#determine the row value
			if row_o == 2:
				row_value = 1000; 	#for the win
			elif row_x == 2:
				row_value = 100 	#for the block
			elif row_o == 1 and row_x == 0:
				row_value = 10 		#a row we have square and the player doesn't
			else:
				row_value = 1 		#empty row

			for space in row_empty:
				if space in moves:
					moves[space] = moves[space] + row_value
				else:
					moves[space] = row_value

	#determine the best move
	highest_move_value = 0
	highest_move = ''
	for move in moves:
		if moves[move] > highest_move_value:
			highest_move = move
			highest_move_value = moves[move]

	move_parts = highest_move.split(' ')

	#make our move
	board[int(move_parts[0])][int(move_parts[1])] = 'O'

	return board

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
		print "That square is already taken."
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

		check_moves(wins, board)
		if is_winner(board, 'O'):
			print_board(board)
			print ""
			print "I Win!"
			break

		if is_board_full(board):
			print "It's a Tie!"
			break