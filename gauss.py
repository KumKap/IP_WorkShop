# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:46:48 2019

@author: KumKap
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("C:\\Users\KumKap\\opencv\\minion.jpg",1) # 0 for bw and 1 for color

imgb = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert to greyscale
image = imgb.astype(np.float) #typecast to float for addition
#cv.imshow("img",imgb)
x,y = imgb.shape
print(x)
print(y)

gauss1 = np.random.normal(0,10,(x,y))
gauss2 = np.random.normal(0,20,(x,y))
#plt.hist(gauss,np.linspace(start = -30, stop = +30, num = 100)) 
gauss3 = np.random.normal(0,1,(x,y))
gauss4 = np.random.normal(0,3,(x,y))
gauss5 = np.random.normal(0,0.5,(x,y))
#plt.hist(gauss,np.linspace(start = -30, stop = +30, num = 100)) 
#plt.title("histogram") 
#plt.show()
gaussf1 = gauss1.astype(np.uint8)
gaussf2 = gauss2.astype(np.uint8)
gaussf3 = gauss3.astype(np.uint8)
gaussf4 = gauss4.astype(np.uint8)
gaussf5 = gauss5.astype(np.uint8)
noisy1 = image + gaussf1
noisy2 = image + gaussf2
noisy3 = image + gaussf3
noisy4 = image + gaussf4
noisy5 = image + gaussf5
noisy_img1 = noisy1.astype(np.uint8)
noisy_img2 = noisy2.astype(np.uint8)
noisy_img3 = noisy3.astype(np.uint8)
noisy_img4 = noisy4.astype(np.uint8)
noisy_img5 = noisy5.astype(np.uint8)

#cv.imshow("gauss2",gauss2)
cv.imshow("gauss1",gaussf1)
#cv.imshow("gauss3",gauss3)
#cv.imshow("gauss4",gauss4)
#cv.imshow("gauss5",gauss5)
#cv.namedWindow('Window',cv.WINDOW_NORMAL)
#cv.resizeWindow('Window',200,300)
#cv.imshow("Window",noisy_img2)
#cv.imshow("img_n2",noisy_img2)
#cv.imshow("img_n3",noisy_img3)
#cv.imshow("img_n4",noisy_img4)
#cv.imshow("img_n5",noisy_img5)


blur1 = cv.GaussianBlur(noisy_img2,(5,5),0)
blur2 = cv.GaussianBlur(noisy_img2,(11,11),5)
blur3 = cv.GaussianBlur(noisy_img2,(31,31),10)
blur4 = cv.GaussianBlur(noisy_img2,(63,63),11)
cv.imshow("blur1",blur1)
#cv.imshow("blur2",blur2)
#cv.imshow("blur3",blur3)
#cv.imshow("blur4",blur4)

cv.waitKey(0)
cv.destroyAllWindows()
