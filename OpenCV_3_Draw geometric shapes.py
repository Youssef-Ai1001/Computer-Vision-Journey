import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

# img = cv2.line(img,(0,256),(512,256),(255,255,255),10)

# img = cv2.circle(img,(256,256),100,(255,255,255),10)

# img = cv2.rectangle(img,(0,0),(125,125),(0.255,255),-1)

# img = cv2.arrowedLine(img,(512,0),(256,256),(0,0,255),5)

# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img,"Youssef",(46,375),font,3,(255,255,42))

# pts = np.array([[13,13],[256,8],[75,57],[512,256],[100,89]],np.int32)
# img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()