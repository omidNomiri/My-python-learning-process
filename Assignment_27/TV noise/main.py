import cv2
import numpy as np
from imageio import mimsave

image = np.ones((800, 1200), dtype=np.uint8) * 255
cv2.line(image, (800, 700), (900, 800), 0, 15)
cv2.line(image, (400, 700), (300, 800), 0, 15)
cv2.rectangle(image, (100, 100), (1100, 700), 150, 15)

rows, columns = image.shape
frame_list = []

while True:
    TV_noise = np.random.random((600, 1000)) * 255
    TV_noise = np.array(TV_noise, dtype=np.uint8)

    image[100:700, 100:1100] = TV_noise
    frame_list.append(image.copy())

    cv2.imshow("TV noise", image)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

mimsave('gif.gif', frame_list, fps=30)
