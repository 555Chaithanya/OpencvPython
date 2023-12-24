import cv2
import numpy as np

'''#Understanding of Img dimenctions
img=np.zeros((1,1,1),np.uint8)
img2=np.zeros((2,1,1),np.uint8)
img3=np.zeros((1,2,1),np.uint8)
img4=np.zeros((1,1,2),np.uint8)
print(img.shape)
print(img)
print(img2.shape)
print(img2)
print(img3.shape)
print(img3)
print(img4.shape)
print(img4)
'''
#Colouring window with custom sizes
img=np.zeros((512,512,3),np.uint8)
'''img[:] = 255,0,0 #Experiment with value changes'''
'''img[200:300,100:300] = 200,250,0  #(y,x)'''
#Drawing lines on window
'''cv2.line(img,(0,0),(300,300),(200,0,0),3)'''
'''cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(200,0,0),3)#(width,height)'''
#Drawing rectangles:
'''cv2.rectangle(img,(100,150),(220,400),(0,255,0),12)
cv2.rectangle(img,(0,0),(220,400),(0,255,0),cv2.FILLED)'''
#Drawing Circles:
'''cv2.circle(img,(400,200),100,(255,255,100),5)'''
#Placing Text on Images
cv2.putText(img,"Open CV ",(100,200),cv2.FONT_HERSHEY_COMPLEX, 0.5,(150,150,0),2)
cv2.imshow("Img",img)
cv2.waitKey(0)
