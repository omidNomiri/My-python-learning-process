import cv2
import numpy as np

image = cv2.imread("Assignment_32/input/spider.png", cv2.IMREAD_GRAYSCALE)

# 1. Edge detection filter
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

result = cv2.filter2D(image, 0, kernel)
result = np.hstack((image, result))

cv2.imshow("", result)
cv2.waitKey(0)

# 2. Sharpening filter
kernel = np.array([[0, -1,  0],
                   [-1,  5, -1],
                   [0, -1,  0]])

result = cv2.filter2D(image, 0, kernel)
result = np.hstack((image, result))

cv2.imshow("", result)
cv2.waitKey(0)

# 3. Emboss filter
kernel = np.array([[-2, -1,  0],
                   [-1,  1,  1],
                   [0,  1,  2]])

result = cv2.filter2D(image, 0, kernel)
result = np.hstack((image, result))

cv2.imshow("", result)
cv2.waitKey(0)

# 4. Identity filter
kernel = np.array([[0,  0,  0],
                   [0,  1,  0],
                   [0,  0,  0]])

result = cv2.filter2D(image, 0, kernel)
result = np.hstack((image, result))

cv2.imshow("", result)
cv2.waitKey(0)

# 5. Black zone filter
kernel = np.array([[0,  2,  0],
                   [2,  -4,  2],
                   [0,  2,  0]])

result = cv2.filter2D(image, 0, kernel)
result = np.hstack((image, result))
cv2.imshow("", result)
cv2.waitKey(0)
