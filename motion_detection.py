import cv2
import time
import imutils

cam = cv2.VideoCapture(0)
time.sleep(1)

firstframe=None
area=500 #to detect the change in area motion detect(if in background some cloth is moving to not detect it as moving object)
count=0
while True:
    _,img = cam.read()
    text = "Normal" #initilize a variable as normal 
    img = imutils.resize(img, width=500) #resize the frame in realtime
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #in binary grayscale image only the object detection is possible so
    gaussianImg = cv2.GaussianBlur(grayImg,(21,21),0)
    if firstframe is None: #to declare it as a first frame the background image
        firstframe = gaussianImg
        continue
    imgDiff = cv2.absdiff(firstframe, gaussianImg) #to copare the current frame with the background image(absolute difference-syntax)
    threshImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1] 
    threshImg =cv2.dilate(threshImg, None,iterations=2) #applying dilation expanding th holes in thresholdimg to look clear
    cnts = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #to find the contours between each and every thing and to connect the contours
    cnts = imutils.grab_contours(cnts) #to detect and connect all counters
    for c in cnts:#if the count is less than 500 then only it draw th figure
        if cv2.contourArea(c) < area:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #to make the rectangle box on the unknown object
        text = "Moving object detected"+"[count]="+str(count)
    print(text)
    cv2.putText(img, text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2) #to represent the text on the screen(detected)
        
    
    cv2.imshow("camerafeed",img)
    key = cv2.waitKey(1)&0xFF
    count=count+1
    
    if key == ord("q"):
        break
    
    
cam.release()
cv2.destroyAllWindows()
    
