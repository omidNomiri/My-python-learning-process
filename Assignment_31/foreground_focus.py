import cv2
import numpy as np

image = cv2.imread("Assignment_31/input/flower.png", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
threshold = 255 - threshold

bitwise = cv2.bitwise_and(threshold, image)

_, threshold = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
new_image = cv2.bitwise_and(threshold, image)

blurred_image = cv2.blur(new_image, (5, 5))
mixed_image = bitwise + blurred_image

cv2.imshow("", mixed_image)
cv2.waitKey(0)
