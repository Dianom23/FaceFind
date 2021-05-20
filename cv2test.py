import cv2
#
img = cv2.imread("Dima.jpg")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img)
#
cv2.imshow("Image", img_grey)
cv2.waitKey()