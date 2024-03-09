import cv2  #importing cam lib
import time #importing time function library

cam = cv2.VideoCapture(0) #enabling the camera and save funv in a variable
time.sleep(1) #wait for one sec and execute
while True: #for infinite loop to display
    _,img = cam.read() #read of cam varible returns two values
    cv2.imshow("cam_stream",img) #to show or display the capture
    key = cv2.waitKey(1)&0XFF #to get the keyboard values
    if key == ord("e"): #to set the key to exit 
        break
    
cam.release() #to release the camera after the execution of the program
cv2.destroyAllWindows() #to destroy all the windows opened
