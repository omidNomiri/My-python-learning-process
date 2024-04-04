import cv2
import numpy as np

image = cv2.imread("Assignment_32/input/hidden_item.tif", cv2.IMREAD_GRAYSCALE)


def noise_redactor(image, divide_number, kernel_size):

    kernel = np.ones((divide_number, divide_number),
                     dtype=np.uint8) // kernel_size

    result = cv2.filter2D(image, -1, kernel)

    return result


avg_kernel_3x3_1 = noise_redactor(image, 3, 1)
avg_kernel_3x3_2 = noise_redactor(image, 3, 0.2)
avg_kernel_3x3_3 = noise_redactor(image, 3, 0.04)

avg_kernel_5x5_1 = noise_redactor(image, 5, 1)
avg_kernel_5x5_2 = noise_redactor(image, 5, 0.2)
avg_kernel_5x5_3 = noise_redactor(image, 5, 0.04)

result_list_3x3 = np.hstack(
    (image, avg_kernel_3x3_1, avg_kernel_3x3_2, avg_kernel_3x3_3))

cv2.imshow("", result_list_3x3)
cv2.waitKey(0)

result_list_5x5 = np.hstack(
    (image, avg_kernel_5x5_1, avg_kernel_5x5_2, avg_kernel_5x5_3))

cv2.imshow("", result_list_5x5)
cv2.waitKey(0)
