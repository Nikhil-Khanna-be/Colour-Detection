# import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Camera intialize
cam=cv2.VideoCapture(0)

# loop to run camera,read frames
while True:
    success,frame=cam.read()
    # stop camera if fails
    if not success:
        break
    img=frame.copy()
    # convert to hsv
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # range of red colour,taking or of two ranges for better detection
    red_L1=np.array([0,120,70],np.uint8)
    red_U1=np.array([10,255,255],np.uint8)
    red_L2=np.array([170,120,70],np.uint8)
    red_U2=np.array([180,255,255],np.uint8)
    mask_red1=cv2.inRange(hsv,red_L1,red_U1)
    mask_red2=cv2.inRange(hsv,red_L2,red_U2)
    redM=cv2.bitwise_or(mask_red1,mask_red2)

    kernel=np.ones((5,5),'uint8')
    redM=cv2.dilate(redM,kernel)
    # taking cordinates of detected point
    cont,heir=cv2.findContours(redM,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,cont in enumerate(cont):
        area=cv2.contourArea(cont)
        # making boundaries
        if(area>300):
            x,y,w,h=cv2.boundingRect(cont)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=2) 
            cv2.putText(frame,"Red Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255),2)     

    
    # range of green colour
    green_L=np.array([40,40,40],np.uint8)
    green_U=np.array([80,255,255],np.uint8)
    greenM=cv2.inRange(hsv,green_L,green_U)

    kernel=np.ones((5,5),'uint8')
    greenM=cv2.dilate(greenM,kernel)
    # taking cordinates of detected point
    cont,heir=cv2.findContours(greenM,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,cont in enumerate(cont):
        area=cv2.contourArea(cont)
        # making boundaries
        if(area>300):
            x,y,w,h=cv2.boundingRect(cont)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2) 
            cv2.putText(frame,"Green Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)     


    # range of blue colour
    blue_L=np.array([95,100,100],np.uint8)
    blue_U=np.array([140,255,255],np.uint8)
    blueM=cv2.inRange(hsv,blue_L,blue_U)

    kernel=np.ones((5,5),'uint8')
    blueM=cv2.dilate(blueM,kernel)
    # taking cordinates of detected point
    cont,heir=cv2.findContours(blueM,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic,cont in enumerate(cont):
        area=cv2.contourArea(cont)
        # making boundaries
        if(area>300):
            x,y,w,h=cv2.boundingRect(cont)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=2) 
            cv2.putText(frame,"Blue Colour",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0),2)     


    cv2.imshow("Colour Detection",frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
cv2.destroyAllWindows() 