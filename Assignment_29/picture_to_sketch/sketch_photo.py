import cv2

image = cv2.imread(
    "Assignment_29/picture_to_sketch/input/image.png", cv2.IMREAD_GRAYSCALE)

inverted = 255 - image
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blurred = 255 - blurred

sketch = image / inverted
sketch = sketch * 255

cv2.imwrite("Assignment_29/picture_to_sketch/output/sketch.jpg", sketch)
