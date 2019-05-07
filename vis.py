import cv2
import numpy as np

def create_mini_board(fname='board_raw') :
	# read the image in grayscale
	game_board = cv2.imread(f'{fname}.png', 0)
	y, x = game_board.shape
	#x, y = game_board.shape
	# create the small version of the board
	# each pixel is a cell of a tetromino
	arr = []
	y_range = range(int(y/40), y, int(y/20))
	x_range = range(int(x/20), x, int(x/10))
	for i in y_range :
		arr2 = []
		for j in x_range :
			if game_board[i][j] > 0 :
				arr2.append(255)
			else :
				arr2.append(0)
		arr.append(arr2)

	arr = np.array(arr)
	cv2.imwrite('board.png', arr)

	# write the new picture to a file
	cv2.imwrite('game_board.png', game_board)

def create_mini_next(fname='next_raw') :
	# read the image in grayscale
	next_piece = cv2.imread(f'{fname}.png', 0)
	y, x = next_piece.shape

	# Figure out which piece it is through elimination
	# check center pixel
	if next_piece[int((1/4)*y)][int(x/2)] == 0 :
		# check square
		if next_piece[int(y/2)][int((5/8)*x)] == 0 :
			print('square')
		# else long
		else :
			print('long')
	# check below center pixel
	elif next_piece[int((3/4)*y)][int(x/2)] == 0 :
		# check J
		if next_piece[int((3/4)*y)][int((1/4)*x)] == 0 :
			print('J')
		# else L
		else :
			print('L')
	# check bottom left pixel
	elif next_piece[int((3/4)*y)][int((1/4)*x)] == 0 :
		# check T
		if next_piece[int((3/4)*y)][int((3/4)*x)] == 0 :
			print('T')
		# else Z
		else :
			print('Z')
	# only thing left is S piece
	else :
		print('S')

	# create the small version of the piece
	# each pixel is a cell of a tetromino
	cv2.imwrite('next_piece.png', next_piece)

if __name__ == '__main__' :
	create_mini_next()
