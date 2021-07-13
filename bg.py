import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)


while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Image",frame)

    if cv2.waitKey(5) == ord('q'):
        cv2.imwrite('image1.jpg',frame)
        break



cap.release()
cv2.destroyAllWindows()







