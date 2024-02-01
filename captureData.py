#a script to gather images that are labeled as we have a fish and no fish
import time
import numpy as np
import pyautogui
import imutils
import cv2
from datetime import datetime
import pydirectinput
import win32api
import win32con
import os
import sys
import random

#config
checkClickFrequ = 500 #frequenzy at which we check button clicks
frequency = 4 #frequenzy in Hz at which NN will run -> we add a random delay to taking the screenshot
delayFishing = 4 #re throw rod after ... seconds
picTime = 5 #indicator for how long it should take on average to take the dont reel picture

print("Tab into Minecraft, make sure its windowed on full size")
print("Aim reel 4 blocks away")

#set up folder paths for pictures
_path = os.path.dirname(os.path.realpath(sys.argv[0]))
folder_reel = _path + "/Reel/"
folder_dont = _path + "/DontReel/"
print("Path for positive: " + folder_reel)
print("Path for negative: " + folder_dont)

def savePicture(dirname):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    x = image.shape[0]
    y = image.shape[1]
    width = 0.05 #width percentage of the picture we wana use
    heightUp = 0.1 #height percentage of the picture we wana use upwards of cursor
    heightDown = 0.03 #height percentage below cursor
    dxu = round(x * heightUp)
    dxl = round(x * heightDown)
    dy = round(y * width / 2)
    xm = round(0.5 * x)
    ym = round(0.5 * y)
    image = image[(xm - dxu):(xm + dxl),(ym - dy):(ym + dy),:]
    filename = f'{datetime.now():%Y_%m_%d_%H_%M_%S%z}'
    filename =  dirname + filename + ".png"
    cv2.imwrite(filename, image)

run = True
ds = 1/checkClickFrequ 
reeled = False
rand_pic = True
rand_lim = 1 / (picTime * checkClickFrequ)
t = time.time()
while(run):
    if(not reeled):
        #throw reel
        time.sleep(delayFishing)
        pydirectinput.click(button='right')
        print("Threw Reel")
        reeled = True
        rand_pic = True
    else:
        #check for button presses
        state_right = win32api.GetKeyState(0x02)
        state_left = win32api.GetKeyState(0x01)
        if state_right < 0:
            print("reeled in .. taking picture")
            reeled = False
            savePicture(folder_reel)
        elif(state_left < 0):
            run = False
            print("Terminating ...")
        elif(rand_pic):
            if(random.random() < rand_lim):
                rand_pic = False
                print("Dont reel picture taken")
                savePicture(folder_dont)
        #achieve target frequenzy
        time.sleep(ds)


print("Well done")
    









