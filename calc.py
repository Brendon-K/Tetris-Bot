import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep
# constants because the tetris board is always 20x10
ROWS = 20
COLS = 10

# (x_start,y_start,x_end,y_end)
#sleep(2)
#printscreen_pil = ImageGrab.grab(bbox = (280*2+655, 2*59+283, 280*2+655+553, 2*779-195))
#img = np.array(printscreen_pil)
#cv2.imwrite('test.png', img)

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