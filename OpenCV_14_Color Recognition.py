import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)

while(cap.isOpened()):
    ret, frame = cap.read()
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    height, width , channel = frame.shape
    
    cx = int(width / 2)
    cy = int(height / 2)
    
    pixel_center = hsv_frame[cy,cx]
    # print(pixel_center)
    hue_value = pixel_center[0]
    # print(hue_value)

    color = "_"

    if hue_value >= 0 and hue_value <= 5:
        color = "RED"
    elif hue_value <= 15:
        color = "ORANGE"
    elif hue_value <= 25:
        color = "YELLOW"
    elif hue_value <= 35:
        color = "LIGHT GREEN"
    elif hue_value <= 85:
        color = "GREEN"
    elif hue_value <= 100:
        color = "CYAN"
    elif hue_value <= 125:
        color = "BLUE"
    elif hue_value <= 145:
        color = "PURPLE"
    elif hue_value <= 160:
        color = "PINK"
    elif hue_value <= 179:
        color = "RED"
    else:
        color = "UNDEFINED"

    pixel_center_bgr = frame[cy,cx]
    # print(pixel_center_bgr)
    b,g,r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv.rectangle(frame,(cx-220,10),(cx+200,120),(255,255,255),-1)
    cv.putText(frame,color,(cx-200,100),0,3,(b,g,r),5)
    cv.circle(frame,(cx,cy),5,(0,0,0),3)
    cv.imshow("Frame",frame)
    
    if cv.waitKey(1) == 27:
        break
    
cap.release()
cv.destroyAllWindows()