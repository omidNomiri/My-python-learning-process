import cv2
import numpy as np

chess_board_image = np.zeros((800, 800))

for row in range(0, 800, 80):
    for col in range(0, 800, 80):
        is_dark = (row // 80 + col // 80) % 2 == 1
        if is_dark:
            chess_board_image[row:row+80, col:col+80] = 255

cv2.imwrite("chess_board_image.jpg" ,chess_board_image)

cv2.imshow("chess", chess_board_image)
cv2.waitKey(0)
