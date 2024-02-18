import cv2
import numpy as np

none_gradient_image = np.zeros((255, 255))

for i in range(255):
    none_gradient_image[i, 0:255] = i

cv2.imwrite("gradient_image.jpg" ,none_gradient_image)
