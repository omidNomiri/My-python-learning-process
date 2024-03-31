import cv2
import numpy as np

noisy_skeleton = cv2.imread("Assignment_31/input/noisy_skeleton.png",
                   cv2.IMREAD_GRAYSCALE)

noisy_board = cv2.imread("Assignment_31/input/noisy_board.png",
                   cv2.IMREAD_GRAYSCALE)

noisy_image = cv2.imread("Assignment_31/input/noisy_image.png",
                   cv2.IMREAD_GRAYSCALE)

def noise_redactor(image, divide_number):

    row, column = image.shape

    result = np.zeros((row, column), dtype=np.uint8)

    kernel = np.ones((divide_number, divide_number),
                     dtype=np.uint8) / (divide_number * divide_number)
    corner = (divide_number - 1) // 2

    for i in range(corner, row - corner):
        for j in range(corner, column - corner):
            small_selection = image[i-corner:i +
                                    (corner+1), j-corner:j+(corner+1)]
            result[i, j] = np.sum(kernel * small_selection)

    return result


result = noise_redactor(noisy_skeleton, 3)
cv2.imshow("3X3", result)
cv2.waitKey(0)
result = noise_redactor(noisy_skeleton, 5)
cv2.imshow("5X5", result)
cv2.waitKey(0)
result = noise_redactor(noisy_skeleton, 15)
cv2.imshow("15X15", result)
cv2.waitKey(0)

result = noise_redactor(noisy_board, 3)
cv2.imshow("3X3", result)
cv2.waitKey(0)
result = noise_redactor(noisy_board, 5)
cv2.imshow("5X5", result)
cv2.waitKey(0)
result = noise_redactor(noisy_board, 15)
cv2.imshow("15X15", result)
cv2.waitKey(0)

result = noise_redactor(noisy_image, 3)
cv2.imshow("3X3", result)
cv2.waitKey(0)
result = noise_redactor(noisy_image, 5)
cv2.imshow("5X5", result)
cv2.waitKey(0)
result = noise_redactor(noisy_image, 15)
cv2.imshow("15X15", result)
cv2.waitKey(0)
