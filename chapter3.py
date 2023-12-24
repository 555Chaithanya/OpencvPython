import cv2
import numpy as np

'''Image resizing
img = cv2.imread("Resources/waterdrops.jpg")
print(img.shape)
imgResize = cv2.resize(img,(700,200)) #(width, height)~~ (x,y)~~(East,South)
print(imgResize.shape)
cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.waitKey(0)
'''

'''Image cropping'''
img = cv2.imread("Resources/waterdrops.jpg")
imgCropped = img[0:200,200:500] #(height,width)~~(y,x)~~(South,East)

cv2.imshow("Image",img)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)

