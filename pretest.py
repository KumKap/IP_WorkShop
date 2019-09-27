# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:53:10 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\KumKap\\opencv\\flower.png",1) # 0 for bw and 1 for color
#img = cv.cvtColor(image, cv.COLOR_BGR2RGB) #convert to greyscale

cv.imshow("img",img)
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
# =============================================================================


bw = img[0:100,0:200,0:3] # returns [0] as float of 1st value and [1] as bw image

cv.imshow("bw",bw)
cv.imwrite('saved1.png',bw)
# =============================================================================
# 
#   cv::IMWRITE_JPEG_QUALITY = 1,
#   cv::IMWRITE_JPEG_PROGRESSIVE = 2,
#   cv::IMWRITE_JPEG_OPTIMIZE = 3,
#   cv::IMWRITE_JPEG_RST_INTERVAL = 4,
#   cv::IMWRITE_JPEG_LUMA_QUALITY = 5,
#   cv::IMWRITE_JPEG_CHROMA_QUALITY = 6,
#   cv::IMWRITE_PNG_COMPRESSION = 16,
#   cv::IMWRITE_PNG_STRATEGY = 17,
#   cv::IMWRITE_PNG_BILEVEL = 18,
#   cv::IMWRITE_PXM_BINARY = 32,
#   cv::IMWRITE_EXR_TYPE = (3 << 4) + 0,
#   cv::IMWRITE_WEBP_QUALITY = 64,
#   cv::IMWRITE_PAM_TUPLETYPE = 128,
#   cv::IMWRITE_TIFF_RESUNIT = 256,
#   cv::IMWRITE_TIFF_XDPI = 257,
#   cv::IMWRITE_TIFF_YDPI = 258,
#   cv::IMWRITE_TIFF_COMPRESSION = 259
# 
# =============================================================================

cv.waitKey(0)
cv.destroyAllWindows()