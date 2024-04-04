import cv2
import numpy as np

image_skeleton = cv2.imread(
    "Assignment_32/input/noisy_skeleton.png", cv2.IMREAD_GRAYSCALE)
image_board = cv2.imread(
    "Assignment_32/input/noisy_board.png", cv2.IMREAD_GRAYSCALE)
image_circle = cv2.imread(
    "Assignment_32/input/noisy_image.png", cv2.IMREAD_GRAYSCALE)
image_woman = cv2.imread("Assignment_32/input/woman.png", cv2.IMREAD_GRAYSCALE)
image_a = cv2.imread("Assignment_32/input/a.png", cv2.IMREAD_GRAYSCALE)
image_man_woman = cv2.imread("Assignment_32/input/man_woman.png")


def median_noise_redactor(image):
    result = cv2.medianBlur(image, 3)

    result = np.hstack((image, result))
    cv2.imshow("", result)
    cv2.waitKey(0)


median_noise_redactor(image_skeleton)
median_noise_redactor(image_board)
median_noise_redactor(image_circle)
median_noise_redactor(image_woman)
median_noise_redactor(image_man_woman)
median_noise_redactor(image_a)
