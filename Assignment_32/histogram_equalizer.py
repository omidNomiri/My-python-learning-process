import cv2
import numpy as np

# image = cv2.imread("Assignment_32/input/land.png", cv2.IMREAD_GRAYSCALE)
# image = cv2.imread("Assignment_32/input/landing_place.png", cv2.IMREAD_GRAYSCALE)
image = cv2.imread("Assignment_32/input/figure.png", cv2.IMREAD_GRAYSCALE)

equalize_result = cv2.equalizeHist(image)
clahe_result = cv2.createCLAHE(2, (3, 3))
clahe_result = clahe_result.apply(image)

result_list = np.hstack((image, equalize_result, clahe_result))
cv2.imshow("", result_list)
cv2.waitKey(0)
