import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep
# constants because the tetris board is always 20x10
ROWS = 20
COLS = 10

def data() :
	'''
	Calculates area and perimeter of the current tetris board
	area : number of blocks there are (1 unit = 1 block)
	perimeter : line measurement of main board shape, only counting the inside of the board
	            does not take into account the edges of the board
	            should not take into account the falling piece, but currently does if said piece is at the same level or below the highest block of the board
	'''
	# get small board in grayscale
	img = cv2.imread('board.png', 0)
	area = 0
	perimeter = 0
	for i, row in enumerate(img) :
		# clear area and perimeter if there are no blocks on the current row
		# this is to attempt to remove the falling piece from the equation
		# probably a better way to do this
		if sum(row) < 255 : 
			area = 0
			perimeter = 0
		for j, col in enumerate(row) :
			# if current cell has a block
			if col == 255 : 
				area += 1
				# look at orthogonally adjacent blocks 
				# and increment perimeter if empty
				if i > 0 and img[i-1][j] != 255 :
					img[i-1][j] += 1
					perimeter += 1
				if i < ROWS-1 and img[i+1][j] != 255 :
					img[i+1][j] += 1
					perimeter += 1
				if j > 0 and img[i][j-1] != 255 :
					img[i][j-1] += 1
					perimeter += 1
				if j < COLS-1 and img[i][j+1] != 255 :
					img[i][j+1] += 1
					perimeter += 1

	print('Area:', area)
	print('Perimeter:', perimeter)