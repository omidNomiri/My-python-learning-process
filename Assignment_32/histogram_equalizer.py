import cv2
import numpy as np

land_image = cv2.imread("Assignment_32/input/land.png", cv2.IMREAD_GRAYSCALE)
landing_place_image = cv2.imread("Assignment_32/input/landing_place.png",
                                 cv2.IMREAD_GRAYSCALE)
figure_image = cv2.imread(
    "Assignment_32/input/figure.png", cv2.IMREAD_GRAYSCALE)


def equalizer_histogram(image, equalizer_histogram_model):
    if equalizer_histogram_model == "normal_equalize":
        equalize_result = cv2.equalizeHist(image)

        result_list = np.hstack((image, equalize_result))
        return result_list
    elif equalizer_histogram_model == "clahe_equalize":
        clahe_result = cv2.createCLAHE(2, (3, 3))
        clahe_result = clahe_result.apply(image)

        result_list = np.hstack((image, clahe_result))
        return result_list
    else:
        return image


result = equalizer_histogram(land_image, "normal_equalize")
cv2.imshow("", result)
cv2.waitKey(0)

result = equalizer_histogram(landing_place_image, "normal_equalize")
cv2.imshow("", result)
cv2.waitKey(0)

result = equalizer_histogram(figure_image, "clahe_equalize")
cv2.imshow("", result)
cv2.waitKey(0)
