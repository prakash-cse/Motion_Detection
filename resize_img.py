import cv2
import imutils
img = cv2.imread("sample1.png")
resize = imutils.resize(img,width=20)
cv2.imwrite("resized_image.png",resize)
