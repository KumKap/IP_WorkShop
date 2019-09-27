# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 00:22:27 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#difference
img1 = cv.imread("C:\\Users\KumKap\\opencv\\fg.png",1) # 0 for bw and 1 for color without hand
img2 = cv.imread("C:\\Users\KumKap\\opencv\\bg.png",1) # 0 for bw and 1 for color with hand
diff = cv.absdiff(img2, img1) #difference in pixel values..if same then 0 if unequal then retained
mask = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

th = 1
imask =  mask>th #create boolean matrix to mark true wherever difference is present 

canvas = np.zeros_like(img2, np.uint8)
canvas[imask] = img2[imask]

cv.imshow("diff",diff)
cv.imshow("drf",canvas)

cv.waitKey(0)
cv.destroyAllWindows()
