import cv2
import numpy as np
import matplotlib.pyplot as plt

histogram_list = np.zeros(255, dtype=np.uint8)
image = cv2.imread("Assignment_31/input/spider.png", cv2.IMREAD_GRAYSCALE)
row, column = image.shape

for i in range(row):
    for j in range(column):
        histogram_list[image[i, j]] += 1

plt.plot(histogram_list)
plt.show()
plt.hist(histogram_list)
plt.show()
plt.bar(range(len(histogram_list)), histogram_list)
plt.show()
