import cv2
import numpy as np

width = 800
height = 600
pitch = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(0, width, 100):
    if i // 100 % 2 == 0:
        pitch[:, i:i+100] = [66, 125, 17]
    else:
        pitch[:, i:i+100] = [71, 139, 16]

cv2.rectangle(pitch, (50, 50), (750, 550), (255, 255, 255), 5)

cv2.rectangle(pitch, (50, 250), (100, 350), (255, 255, 255), 5)
cv2.rectangle(pitch, (50, 200), (150, 400), (255, 255, 255), 5)

cv2.rectangle(pitch, (750, 250), (700, 350), (255, 255, 255), 5)
cv2.rectangle(pitch, (750, 200), (650, 400), (255, 255, 255), 5)

cv2.line(pitch, (400, 50), (400, 550), (255, 255, 255), 5)

cv2.circle(pitch, (400, 300), 6, (255, 255, 255), 15)
cv2.circle(pitch, (400, 300), 100, (255, 255, 255), 5)

cv2.imshow("football pitch", pitch)
cv2.waitKey(0)
