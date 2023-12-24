import cv2
import numpy as np

img = cv2.imread("Resources/waterdrops.jpg")
kernel = np.ones((5,5),np.uint8)
'''
>Gray scale img display
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Img",imgGray)
cv2.waitKey(0)
'''
'''Gray vs Blur vs Canny vs Dilated vs Eroded imges'''
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(11,11),0)
imgCanny= cv2.Canny(img,100,100)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Blur Img",imgBlur)
cv2.imshow("Gray Img",imgGray)
cv2.imshow("Canny Img", imgCanny)
cv2.imshow("Dilation Img", imgDilation)
cv2.imshow("Eroded Img", imgEroded)
cv2.waitKey(0)

