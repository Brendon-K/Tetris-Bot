import cv2
import numpy as np
import os

def create_mini_board(fname='board_raw') :
	# read the image in grayscale
	game_board = cv2.imread(f'{fname}.png', 0)
	os.remove(f'{fname}.png')
	y, x = game_board.shape

	# create the small version of the board
	# each pixel is a single block of a tetromino
	arr = []
	# range starts at half block width (to look at center of a block)
	# and advances 1 block width per loop
	y_range = range(int(y/40), y, int(y/20))
	x_range = range(int(x/20), x, int(x/10))
	for i in y_range :
		arr2 = []
		for j in x_range :
			# if pixel is not black, there is a block there
			if game_board[i][j] > 0 :
				arr2.append(255)
			else :
				arr2.append(0)
		arr.append(arr2)

	arr = np.array(arr)
	# write the new board picture to a file
	cv2.imwrite('board.png', arr)

def create_mini_next(fname='next_raw') :
	# read the image in grayscale
	next_piece = cv2.imread(f'{fname}.png', 0)
	os.remove(f'{fname}.png')
	y, x = next_piece.shape

	# Figure out which piece it is through elimination
	# check center pixel
	if next_piece[int((1/4)*y)][int(x/2)] == 0 :
		# check square
		if next_piece[int(y/2)][int((5/8)*x)] == 0 :
			arr = np.array([[255, 255], [255, 255]])
			print('square')
		# else long
		else :
			arr = np.array([[255, 255, 255, 255]])
			print('long')
	# check below center pixel
	elif next_piece[int((3/4)*y)][int(x/2)] == 0 :
		# check J
		if next_piece[int((3/4)*y)][int((1/4)*x)] == 0 :
			arr = np.array([[255, 0, 0],[255, 255, 255]])
			print('J')
		# else L
		else :
			arr = np.array([[0, 0, 255],[255, 255, 255]])
			print('L')
	# check bottom left pixel
	elif next_piece[int((3/4)*y)][int((1/4)*x)] == 0 :
		# check T
		if next_piece[int((3/4)*y)][int((3/4)*x)] == 0 :
			arr = np.array([[255, 255, 255], [0, 255, 0]])
			print('T')
		# else Z
		else :
			arr = np.array([[255, 255, 0], [0, 255, 255]])
			print('Z')
	# only thing left is S piece
	else :
		arr = np.array([[0, 255, 255],[255, 255, 0]])
		print('S')



	# create the small version of the piece
	# each pixel is a cell of a tetromino
	cv2.imwrite('next_piece.png', arr)

if __name__ == '__main__' :
	create_mini_next()
