import cv2
print('Package Imported')

'''
Playing with Images
'''
# # reading image
# img = cv2.imread('Resources/boy.jpeg')

# # showing image
# cv2.imshow("Output", img)
# cv2.waitKey(0)

'''
Playing With Video
'''
# cap = cv2.VideoCapture('Resources/test_video.mp4')

# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


'''
Playing with webcam
'''

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
