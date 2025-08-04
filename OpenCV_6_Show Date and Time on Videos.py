import cv2 as cv
import datetime

cap = cv.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

print(cap.get(3))
print(cap.get(4))


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + "Heigth: " + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv.putText(frame,text, (10, 50), font, 1,(0, 255, 255), 2)
        frame = cv.putText(frame,datet, (10, 100), font, 1,(0, 255, 255), 2)
        cv.imshow("Live",frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break
    
cap.release()
cv.destroyAllWindows()