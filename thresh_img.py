import cv2
import imutils
img = cv2.imread("sample1.png")
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(grayscale,200,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("threshold_image3.png",thresh)
