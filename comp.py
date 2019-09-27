import numpy as np
import cv2

while True:
 src= cv2.imread('4.jpg', 1)
 #blurred = cv2.GaussianBlur(src, (5, 5),10)

 #structured forest ml approach
 blurred_float = src.astype(np.float32) / 255.0
 edgeDetector = cv2.ximgproc.createStructuredEdgeDetection("model.yml")
 edges = edgeDetector.detectEdges(blurred_float) * 255.0
 cv2.imwrite('edge-raw.jpg', edges)

 hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
 l_b=np.array([123,0,0])
 u_b=np.array([223,255,255])

 mask=cv2.inRange(hsv,l_b,u_b)

 res=cv2.bitwise_or(edges,edges,mask=mask)
 cv2.imshow("res",res)
 
 

 res1=cv2.bitwise_and(src,src,mask=mask)
 cv2.imshow("res1",res1)


 key= cv2.waitKey(1)
 if key==27:
    break
