import cv2

cap = cv2.VideoCapture(0)  # open your laptop camera
fourcc = cv2.VideoWriter_fourcc(*"XVID")    # use any fourcc type to improve quality for the saved video
out = cv2.VideoWriter("/Videos/output_record.mp4",fourcc,20.0,(640,480))   # Video Setting


print(cap.isOpened())           # check if the camera is opened

while(cap.isOpened()):         # while loop to read all frames
    ret,frame = cap.read()    # read all frams if ret is TRUE it means that there is a frames to process
    if ret == True:          
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))     # get the frame height
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))      # get the frame width
        
        out.write(frame)           # save the video
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)       # convert frames from BGR2GRAY
        cv2.imshow("recording" , gray)
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
