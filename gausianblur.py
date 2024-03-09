import cv2
import imutils
img = cv2.imread("sample1.png")
gausian_Blur=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("blur.png",gausian_Blur)
