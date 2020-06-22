import cv2

# # Gray Scale Image
# img = cv2.imread('Resources/boy.jpeg')

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("Gray Image", imgGray)
# cv2.waitKey(0)


# Blur Image
img = cv2.imread('Resources/boy.jpeg')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)
