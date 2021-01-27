import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
catCascade = cv2.CascadeClassifier("cascades/haarcascade_frontalcatface_extended.xml")

img = cv2.imread("images/family.PNG")

# cap = cv2.VideoCapture(0)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)
catface = catCascade.detectMultiScale(imgGray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(img,"Human",(x+w+5,y+h),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))

for (x,y,w,h) in catface:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(img,"Cat",(x+w+5,y+h),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))

cv2.imshow("Result", img)
cv2.waitKey(0)
