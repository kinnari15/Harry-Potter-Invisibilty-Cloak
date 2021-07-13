import cv2
import numpy as np

cap = cv2.VideoCapture(0)
bg = cv2.imread("image1.jpg")


while cap.isOpened():
    ret, frame = cap.read()    

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("HSV", hsv)

        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        print(hsv_red)

        lower_red = np.array([0,100,100])
        upper_red = np.array([10,255,255])

        #red color is highited in white.
        mask = cv2.inRange(hsv,lower_red,upper_red)
        #cv2.imshow("Part1", mask)

        #all things red.
        p1 = cv2.bitwise_and(bg,bg,mask= mask)
        #cv2.imshow("Part1", p1)

        mask = cv2.bitwise_not(mask)
        #previously it was black fully. But now, we need the entire background and ignore red
        
        p2 = cv2.bitwise_and(frame,frame,mask = mask)
        #cv2.imshow("Part2",p2)
        
        p = p1+p2
        cv2.imshow("Final",p)
    
        if cv2.waitKey(5) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
