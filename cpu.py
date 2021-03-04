import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.circle(img, (330, 250), 180, (0, 255, 5), 3) #center circle
    cv2.rectangle(img, (0, 0), (img.shape[1], 50), (0, 0, 0), -1) #filled textline
    cv2.putText(img, "Please fit your face to the green circle for temperature measurement", (0, 30), cv2.FONT_ITALIC, 0.55, (0, 255, 0), 1) #font
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.putText(img, "Temperature: 36.5C", (5, 120), cv2.FONT_ITALIC, 0.6, (0, 255, 0), 2)  # font
    else:
        cv2.putText(img, "Temperature: 39.3C", (5, 120), cv2.FONT_ITALIC, 0.6, (0, 0, 255), 2)  # font


    cv2.imshow("display", img)
    #
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

