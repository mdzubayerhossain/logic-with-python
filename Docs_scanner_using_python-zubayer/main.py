import cv2
import numpy as np
import mapper

image = cv2.imread("test.jpg")
image = cv2.resize(image,(1300,880))
orig = image.copy()

#here we gray the image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Title-gray",gray)


#here we blur the image using gaussian blur system
blurred = cv2.GaussianBlur(gray,(5,5),0)
#cv2.imshow("GaussianBlur",blurred)


#here is the edge detection system
edged = cv2.Canny(blurred,30,50)
#cv2.imshow("Canny",edged)

image,contours,hierarchy = cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours = sorted(contours,key=cv2.contourArea,reverse=True)

for c in contours:
    p = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.02*p,True)

    if len(approx) == 4:
        target = approx
        break
approx = mapper.mapp(target)

pts= np.float32([[0,0],[800,0],[800,800],[0,800]])
op = cv2.getPerspectiveTransform(approx,pts)
dst = cv2.warpPerspective(orig,op,(800,800))
cv2.imshow("Scanned final",dst)
