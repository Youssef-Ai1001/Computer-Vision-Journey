import cv2
import numpy as np


def nothing(x):
    # print(x)
    pass

black_img = np.zeros((300,500,3),np.uint8)
cv2.namedWindow("black_img")

cv2.createTrackbar("Blue",'black_img',0,255,nothing)
cv2.createTrackbar("Green",'black_img',0,255,nothing)
cv2.createTrackbar("Red",'black_img',0,255,nothing)

switch = "0 : OFF \n 1 : ON"
cv2.createTrackbar(switch,'black_img',0,1,nothing)

while(True):
    cv2.imshow("black",black_img)
    k = cv2.waitKey(1)
    if k == 27:
        break

    b = cv2.getTrackbarPos("Blue",'black_img')
    g = cv2.getTrackbarPos("Green",'black_img')
    r = cv2.getTrackbarPos("Red",'black_img')
    s = cv2.getTrackbarPos('switch','black_img')
    
    if s == 0:
        black_img[:] = 0
    else:
        black_img[:] = [b,g,r]

cv2.destroyAllWindows()