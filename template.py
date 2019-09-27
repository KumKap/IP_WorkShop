# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 00:24:54 2019

@author: KumKap
"""


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import random



img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",0) # 0 for bw and 1 for color
cv.imshow("img",img)


#w  = img.shape[0]
#h  = img.shape[1]
crop_img = img[100:250, 100:250] #crop as y:y+h , x:x+w 
crop_imgr = img[0:150,0:150] #crop as y:y+h , x:x+w 

w, h = crop_imgr.shape[::-1]


cv.imshow("region",crop_imgr)

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

method = methods[0]
res = cv.matchTemplate(img,crop_imgr,cv.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum

#if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
top_left = min_loc
#else:
#top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img,top_left, bottom_right, 255, 2)
cv.imshow("res",img)


cv.waitKey(0)
cv.destroyAllWindows()
