# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 01:48:28 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\KumKap\\opencv\\flower.png",1) # 0 for bw and 1 for color
#img = cv.cvtColor(image, cv.COLOR_BGR2RGB) #convert to greyscale

cv.imshow("img",img)


bil = cv.bilateralFilter(img,15,75,75)
edges = cv.Canny(img, 60, 60*3)
res = cv.Canny(bil, 60, 60*3)

# =============================================================================
# GaussianBlur() syntax:
# 
# void bilateralFilter(InputArray src, OutputArray dst, int d, double sigmaColor, 
#                       double sigmaSpace, int borderType=BORDER_DEFAULT )
# Parameters:
# 
# src - Source 8-bit or floating-point, 1-channel or 3-channel image.
# dst - Destination image of the same size and type as src.
# d - Diameter of each pixel neighborhood that is used during filtering. 
#     If it is non-positive, it is computed from sigmaSpace.
# sigmaColor - Filter sigma in the color space. 
# A larger value of the parameter means that farther colors within the pixel neighborhood will be mixed together, 
# resulting in larger areas of semi-equal color.
# sigmaSpace - Filter sigma in the coordinate space. 
# A larger value of the parameter means that farther pixels will influence each other as long as 
# their colors are close enough. When d>0 , it specifies the neighborhood size regardless of sigmaSpace . 
# Otherwise, d is proportional to sigmaSpace.
# 
# =============================================================================
cv.imshow("result",bil)
cv.imshow("Canny",edges)
cv.imshow("Canny with blur",res)



cv.waitKey(0)
cv.destroyAllWindows()