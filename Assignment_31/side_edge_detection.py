import cv2
import numpy as np

image = cv2.imread("Assignment_31/input/house.png", cv2.IMREAD_GRAYSCALE)

def edge_detector(image, filter):
    row, column = image.shape
    result = np.zeros((row, column), dtype=np.uint8)

    for i in range(1, row - 1):
        for j in range(1, column - 1):
            small_selection = image[i-1:i+2, j-1:j+2]
            result[i, j] = np.abs(np.sum(filter * small_selection))
    
    return result

horizontal_filter = np.array ([[-1 , -1 , -1] ,
                               [0 , 0 , 0] ,
                               [1 , 1 , 1]])

vertical_filter = np .array ([[1 , 0 , -1] , 
                              [1 , 0 , -1] , 
                              [1 , 0 , -1]])

result = edge_detector(image, horizontal_filter)
cv2.imshow("", result)
cv2.waitKey(0)

result = edge_detector(image, vertical_filter)
cv2.imshow("", result)
cv2.waitKey(0)
