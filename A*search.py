board = []

#Generate rows with length of 3
for row in range(10):
	#Appen a blank list to each row cell
	board.append([])
	for column in range(10):
		#Assign x to each row
		board[row].append('x')

#Function will print board like an actual board
def print_board(board):
	for row in board:
		print " ".join(row)

print_board(board)