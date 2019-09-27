# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:15:27 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import random

img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",0) # 0 for bw and 1 for color
#img2 = cv.cvtColor(image, cv.COLOR_BGR2RGB) #convert to greyscale
#img = cv.cvtColor(img2, cv.COLOR_BGR2GRAY) #convert to greyscale

#row, col, channel = img.shape
k1 = np.array(([0,0,0],[0,1,0],[0,0,0]), np.float32) #identity
k2 = np.array(([1,0,-1],[0,0,0],[-1,0,1]), np.float32) #edge detection1
sobely = np.array(([-1,-2,-1],[0,0,0],[1,2,1]), np.float32) #edge detection1
sobelx = np.array(([-1,0,1],[-2,0,2],[-1,0,1]), np.float32) #edge detection1

k3 = np.array(([0,1,0],[1,-4,1],[0,1,0]), np.float32)  #edge detection2
k4 = np.array(([-1,-1,-1],[-1,8,-1],[-1,-1,-1]), np.float32) #edge detection3
k5 = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), np.float32) #sharpen
k6 = np.array(np.ones((3,3), np.float32))/9 #box blur

output = cv.filter2D(img, -1, sobelx)
output2 = cv.filter2D(img, -1, sobely) 

cv.imshow("img",img)

cv.imshow("Gx",output)

cv.imshow("Edges",output2)



cv.waitKey(0)
cv.destroyAllWindows()


plt.imshow(img)
plt.title("Image")
plt.show()

plt.imshow(output2)
plt.title("Process")
plt.show()


plt.imshow(output)
plt.title("Gx")
plt.show()