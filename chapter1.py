import cv2

'''
>Image Extraction
img = cv2.imread("Resources/waterdrops.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)
'''
'''
>Video Capturing 
cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
'''
'''Web-cam caturing'''
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
