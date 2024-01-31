#a script to gather images that are labeled as we have a fish and no fish
import time
import numpy as np
import pyautogui
import imutils
import cv2
print("TABBB")
time.sleep(5)
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
x = image.shape[0]
y = image.shape[1]
width = 0.05 #width percentage of the picture we wana use
height = 0.4 #height percentage of the picture we wana use
dx = round(x * height / 2)
dy = round(y * width / 2)
xm = round(0.5 * x)
ym = round(0.5 * y)
image = image[(xm - dx):(xm + dx),(ym - dy):(ym + dy),:]
cv2.imwrite("in_memory_to_disk.png", image)

