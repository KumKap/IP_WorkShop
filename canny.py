# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 00:50:11 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
import imutils
from matplotlib import pyplot as plt

#img = cv.imread("C:\\Users\KumKap\\opencv\\canny_input.jpg",0) # 0 for bw and 1 for color
img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",1) # 0 for bw and 1 for color

#img = cv.cvtColor(image, cv.COLOR_BGR2RGB) #convert to greyscale

cv.imshow("img",img)
rotated = imutils.rotate_bound(img, 30)
cv.imshow("Rotated (Correct)", rotated)

#blur = cv.GaussianBlur(img,(3,3),1)
edges = cv.Canny(img, 60, 60*3)

# =============================================================================
# Canny(image, edges, threshold1, threshold2)
# This method accepts the following parameters −
# 
# image − A Mat object representing the source (input image) for this operation.
# 
# edges − A Mat object representing the destination (edges) for this operation.
# 
# threshold1 − A variable of the type double representing the first threshold for the hysteresis procedure.
# 
# threshold2 − A variable of the type double representing the second threshold for the hysteresis procedure.
# 
# =============================================================================
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image') #, plt.xticks([]), plt.yticks([])
cv.imshow("Edges",edges)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()
