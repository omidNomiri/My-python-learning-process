import cv2
import numpy as np

image = cv2.imread("Assignment_31/input/lion.png", cv2.IMREAD_GRAYSCALE)

row, column = image.shape
result = np.zeros((row, column), dtype=np.uint8)

kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

for i in range(1, row - 1):
    for j in range(1, column - 1):
        small_selection = image[i-1:i+2, j-1:j+2]
        result[i, j] = np.abs(np.sum(kernel * small_selection))


cv2.imshow("", result)
cv2.waitKey(0)
