import cv2
import numpy as np
# importing image
img = cv2.imread('Resources/boy.jpeg')

# defining kernel
kernel = np.ones((5, 5), np.uint8)

# Gray Scale Image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur Image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# Canny Edge Detector
imgCanny = cv2.Canny(img, 100, 100)
# in canny that 100 and 100 are the threshold value, more the threshold value less the edge lines

# Dialation Image
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# for increasing the thickness of the edge

# Eroded Image
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("Gary Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
