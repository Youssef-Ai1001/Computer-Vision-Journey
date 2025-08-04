import cv2

messi_img = cv2.imread("/images/messi.JPG")
ronaldo_img = cv2.imread("/images/ronaldo.jpeg")

# print(messi_img.shape)
# print(messi_img.size)
# print(messi_img.dtype)

# b,g,r = cv2.split(ronaldo_img)
# ronaldo_img = cv2.merge((b,g,r))

messi_img = cv2.resize(messi_img,(712,712))
ronaldo_img = cv2.resize(ronaldo_img,(712,712))

# dst1 = cv2.add(messi_img,ronaldo_img)
# dst2 = cv2.addWeighted(messi_img,0.2,ronaldo_img,0.8,100)

ronaldo_head = ronaldo_img[40:280,200:360]
ronaldo_img[472:712,510:670] = ronaldo_head


cv2.imshow("image",ronaldo_img)
cv2.waitKey(0)
cv2.destroyAllWindows()