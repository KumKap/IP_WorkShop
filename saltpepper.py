# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:46:06 2019

@author: KumKap
"""


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import random

image = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",3) # 0 for bw and 1 for color
img = cv.cvtColor(image, cv.COLOR_BGR2RGB) #convert to greyscale

row, col, channel = img.shape
output = img

plt.imshow(img)
plt.title("Image")
plt.show()
output = np.zeros(img.shape, np.uint8)
p= 0.05

for i in range (row):
    for j in range (col):
        r= random.random() #Return the next random floating point number in the range [0.0, 1.0).

        if r < (p / 2):
            output[i][j] = [0,0,0]
        elif r < p:
            output[i][j] = [255,255,255]
        else:
            output[i][j] = img[i][j]

plt.imshow(output)
plt.title("NOISE")
plt.show()

smooth = cv.medianBlur(output,5) 
#5*5 size of aperture for kernel. it should be odd only

plt.imshow(smooth)
plt.title("SMOOTH")
plt.show()
