import cv2
import numpy as np

# read the image in grayscale
img = cv2.imread('early_board.png', 0)

# isolate the game board
start_x = 780
start_y = 325
x = 400
y = 720
game_board = img[start_y:start_y+y, start_x:start_x+x]
game_board_s = cv2.resize(game_board, None, fx=.5, fy=.5)

# create the small version of the board
# each pixel is a cell of a tetromino
arr = []

for i in range(18, y, 36) :
	arr2 = []
	for j in range(20, x, 40) :
		if game_board[i, j] > 0 :
			arr2.append(255)
		else :
			arr2.append(0)
	arr.append(arr2)

arr = np.array(arr)
cv2.imwrite('board.png', arr)
cv2.imwrite('board_s.png', game_board_s)

# display the image
#cv2.imshow('image', game_board)

# write the new picture to a file
cv2.imwrite('game_board.png', game_board)

# close when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

