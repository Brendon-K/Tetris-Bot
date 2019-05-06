import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep
# constants because the tetris board is always 20x10
ROWS = 20
COLS = 10

# get small board in grayscale
img = cv2.imread('board.png', 0)
area = 0
perimeter = 0
for i, row in enumerate(img) :
	if sum(row) < 255 : 
		area = 0
		perimeter = 0
	for j, col in enumerate(row) :
		if col == 255 : 
			area += 1
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

print(img)
print('Area:', area)
print('Perimeter:', perimeter)