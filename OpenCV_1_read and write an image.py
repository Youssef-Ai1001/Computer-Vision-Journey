import cv2

print(cv2.__version__)

img = cv2.imread("/images/apple.jpg",0) # 0 grayscale , 1 rgb , 1- alpha channel

print(img)

cv2.imshow("GrayScale apple",img)

k = cv2.waitKey(5000)      # wait 5 sec 
cv2.destroyAllWindows()

if k == 27:
    cv2.destroyAllWindows()
    
elif k == ord('s'):          # to save the image on pc
    cv2.imwrite("Gray apple.jpg",img)
    cv2.destroyAllWindows()
