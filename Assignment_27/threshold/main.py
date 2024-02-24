import cv2

image = cv2.imread("Assignment_27/threshold/bat.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rows, columns = gray_image.shape

# run time = 1.3573062419891357s

# for row in range(rows):
#     for column in range(columns):
#         if gray_image[row, column] >= 100:
#             gray_image[row, column] = 255
#         else:
#             gray_image[row, column] = 0
# threshold_image = gray_image

# run time = 0.0009999275207519531

_, threshold_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("threshold image", threshold_image)
cv2.waitKey(0)
