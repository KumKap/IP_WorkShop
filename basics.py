# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:30:57 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import random

img= cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",1) # 0 for bw and 1 for color

# =============================================================================
# m  	cv::ImreadModes {
#   cv::IMREAD_UNCHANGED = -1,
#   cv::IMREAD_GRAYSCALE = 0,
#   cv::IMREAD_COLOR = 1,
#   cv::IMREAD_ANYDEPTH = 2,
#   cv::IMREAD_ANYCOLOR = 4,
#   cv::IMREAD_LOAD_GDAL = 8,
#   cv::IMREAD_REDUCED_GRAYSCALE_2 = 16,
#   cv::IMREAD_REDUCED_COLOR_2 = 17,
#   cv::IMREAD_REDUCED_GRAYSCALE_4 = 32,
#   cv::IMREAD_REDUCED_COLOR_4 = 33,
#   cv::IMREAD_REDUCED_GRAYSCALE_8 = 64,
#   cv::IMREAD_REDUCED_COLOR_8 = 65,
#   cv::IMREAD_IGNORE_ORIENTATION = 128
# }
# 
# =========  ====================================================================
# 
# cv.waitKey(0)
# cv.destroyAllWindows()
# # =============================================================================
# =============================================================================
# =============================================================================
# 
row, col, channel = img.shape #get image dimensions
# print(row,"or",img.shape[0])
# 
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) #convert to RGB
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert to greyscale
# bw = cv.threshold(gray, 127, 255, cv.THRESH_BINARY) # returns [0] as float of 1st value and [1] as bw image
# bwi = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV) # returns [0] as float of 1st value and [1] as bw image
# 
# cv.imshow("rgb",rgb)
# cv.imshow("og",img)
# cv.imshow("gray",gray)
# cv.imshow("bw",bw[1])
# cv.imshow("bwi",bwi[1])
# 
# horizontal_img = cv.flip( img, 0 )
# vertical_img = cv.flip( img, 1 )
# both_img = cv.flip( img, -1 )
# 
# cv.imshow( "Original", img )
# cv.imshow( "Horizontal flip", horizontal_img )
# cv.imshow( "Vertical flip", vertical_img )
# cv.imshow( "Both flip", both_img )
# =============================================================================
 
#scaling
#cv.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) 
#dsize = output size, fx is horizontal scaling factor, fy is vertical scaling factor

# =============================================================================
# 
# #res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
# res = cv.resize(img,(col // 2, row // 2 ))
# #res = cv.resize(img,(col  * 2, row * 2 ))
# #cv.imshow( "Ninety", res)
# 
# retval=cv.getRotationMatrix2D(( col // 2, row // 2), -90 , 1.0)
# rotated_image=cv.warpAffine(img,retval,(col,row))
# cv.imshow('New image', rotated_image)
# #retval=cv.getRotationMatrix2D(center, angle, scale)
# 
# 
# (h, w) = img.shape[:2]
# (cX, cY) = (w // 2, h // 2)
# 
# # grab the rotation matrix (applying the negative of the
# # angle to rotate clockwise), then grab the sine and cosine
# # (i.e., the rotation components of the matrix)
# M = cv.getRotationMatrix2D((cX, cY), -90, 1.0)
# cos = np.abs(M[0, 0])
# sin = np.abs(M[0, 1])
#  
# # compute the new bounding dimensions of the image
# nW = int((h * sin) + (w * cos))
# nH = int((h * cos) + (w * sin))
#  
# # adjust the rotation matrix to take into account translation
# M[0, 2] += (nW / 2) - cX
# M[1, 2] += (nH / 2) - cY
#  
# # perform the actual rotation and return the image
# cor_rot = cv.warpAffine(img, M, (nW, nH))
# cv.imshow("rotate",cor_rot)
# 
# 
# =============================================================================

# =============================================================================
# 
# #translation
# rows,cols,chan = img.shape
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv.warpAffine(img,M,(cols,rows))
# cv.imshow('img',dst)
# 
# 
# =============================================================================


cv.waitKey(0)
cv.destroyAllWindows()