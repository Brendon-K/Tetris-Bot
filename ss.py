import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep

def ss_board(fname='board_raw.png') :
	# Take a screenshot of the Tetris board and save it as fname
	x_start, y_start, x_end, y_end = 280*2+655, 2*59+283, 280*2+655+553, 2*779-195
	# get screenshot
	printscreen_pil = ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end))
	# convert screenshot to array
	img = np.array(printscreen_pil)
	# write screenshot to file
	cv2.imwrite(fname, img)

def ss_next(fname='next_raw.png') :
	# Take a screenshot of the next piece and save it
	x_start, y_start, x_end, y_end = 1872+5, 785+52, 2096-5, 987-59
	printscreen_pil = ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end))
	img = np.array(printscreen_pil)
	cv2.imwrite(fname, img)

if __name__ == '__main__' :
	ss_next()