import numpy as np
import cv2  #importing package

cap = cv2.VideoCapture('vtest.avi') #taking video from stroage or you can take input from webcam by replacing name to 0

ret,frame1 = cap.read()
ret,frame2 = cap.read()

while cap.isOpened(): #checking if cap is open or not
    diff = cv2.absdiff(frame1,frame2)     #finding difference or you can say detecting motion
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)   #converting BGR to gray
    blur = cv2.GaussianBlur(gray,(5,5),0)    #smoothing the image
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)   #setting threshold of binary image
    dilated = cv2.dilate(thresh,None,iterations=3)    #dilating the blurred image
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #finding contour

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)       #taking the co-ordinate axis of the contour

        if cv2.contourArea(contour) < 900:      #checking the area of contour
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)    #framing a rectangle of the detected contour
        cv2.putText(frame1,"Status: {}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX
                    ,1,(0,0,255),3)     #putting up the text at the top left
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)

    cv2.imshow('feed',frame1)
    frame1 = frame2
    ret,frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()