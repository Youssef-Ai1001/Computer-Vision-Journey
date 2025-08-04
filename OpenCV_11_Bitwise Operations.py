import cv2
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv2.rectangle(img1,(160,90),(320,180),(255,255,255),-1)


img2 = np.full((250,500,3),255,np.uint8)
# img2 = np.full((250,500,3),1,np.uint8)
# img2 = np.ones((250,500,3),np.uint8)
img2 = cv2.rectangle(img2,(0,125),(500,0),(0,0,0),-1)

# BitWise Ops
bitAnd = cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitXor = cv2.bitwise_xor(img1,img2)
bitNot = cv2.bitwise_not(img1)


cv2.imshow("img-1",img1)
cv2.imshow("img-2",img2)

cv2.imshow("BitWise ops",bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()