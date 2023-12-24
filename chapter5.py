#print("continue from chapter5 45:51")
import cv2
import numpy as np
img = cv2.imread("Resources/cards.jpg")
#Image perspective
width, height = 250, 350
pts1 = np.float32([[334,49],[490,146],[184,287],[345,384]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output Img", imgOutput)
cv2.waitKey(0)
'''lefttop:334,49
   righttop:490,146
   leftbottom:184,287
   rightbottom:345,384'''