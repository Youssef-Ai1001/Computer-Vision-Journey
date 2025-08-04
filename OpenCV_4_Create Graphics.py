import cv2 as cv
import numpy as np

# Create img
img = np.zeros(shape=(600,900,3),dtype=np.uint8)

# Background
img = cv.rectangle(img,(0,0),(900,500),(255,255,85),-1)
img = cv.rectangle(img,(0,500),(900,600),(75,180,70),-1)

# Sun
img = cv.circle(img,(150,150),80,(0,255,255),-1)
img = cv.circle(img,(150,150),100,(220,255,255),10)

# Trees stem and leafs
# tree 1
cv.line(img, (710, 500), (710, 420), (30,65,155), 15) 
triangle1 = np.array([[640,460],[780,460], [710,200]], dtype=np.int32) 
cv.fillPoly(img,[triangle1],(75,180,70))

#tree 2
cv.line(img, (600, 500), (600, 420), (30,65,155), 25) 
triangle2 = np.array([[500,440],[700,440], [600,75]], dtype=np.int32)
cv.fillPoly(img,[triangle2],(75,200,70))

# Text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"Youssef Taha",(120,490), font, 1.5, (0,0,0), 5)


cv.imwrite("/images/Graphic_img.png",img)      # to save img
cv.imshow("tree",img)
cv.waitKey(0)
cv.destroyAllWindows()