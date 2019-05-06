import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep

# Take a screengrab of the Tetris board and save it
x_start,y_start,x_end,y_end = 280*2+655, 2*59+283, 280*2+655+553, 2*779-195
sleep(2)
printscreen_pil = ImageGrab.grab(bbox = (x_start,y_start,x_end,y_end))
img = np.array(printscreen_pil)
cv2.imwrite('test.png', img)