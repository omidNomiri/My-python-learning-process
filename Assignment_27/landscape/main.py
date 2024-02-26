import cv2
import numpy as np
import imageio

image = cv2.imread("Assignment_27/landscape/image.jpeg")

frame_list = []

while True:
    snow_x = np.random.randint(0, image.shape[1], size=1000)
    snow_y = np.random.randint(0, image.shape[0], size=1000)

    snow_image = image.copy()

    for i in range(100):
        snow_image[snow_y[i], snow_x[i]] = 255

    frame_list.append(snow_image)

    cv2.imshow("output", snow_image)

    if cv2.waitKey(100) and 0xFF == ord("q"):
        break

imageio.mimsave("snowy.gif", frame_list)
