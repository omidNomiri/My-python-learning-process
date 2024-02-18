import cv2
import numpy as np

character_image = np.ones((1000, 1000))

character_image[100:200, 400:600] = 0
character_image[200:500, 300:400] = 0
character_image[200:500, 600:700] = 0
character_image[500:600, 400:600] = 0

cv2.imwrite("chess_board_image.jpg" ,character_image)

cv2.imshow("character_image", character_image)
cv2.waitKey(0)
