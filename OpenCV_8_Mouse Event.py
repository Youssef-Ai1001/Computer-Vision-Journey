import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'Event' in i]
# print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        points.append((x,y))
        if len(points) >=2:
            cv2.line(img,points[-1],points[-2],(255,0,0),5)
            
        cv2.imshow("image",img)
        
points = []

img = np.zeros((700,700,3),dtype=np.uint8)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()