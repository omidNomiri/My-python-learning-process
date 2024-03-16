import cv2

text = cv2.imread("Assignment_29/secret_text/input/text.png")
password = cv2.imread("Assignment_29/secret_text/input/password.png")

secret_text = cv2.subtract(password, text)

result = 255 - secret_text

cv2.imwrite("Assignment_29/secret_text/output/secret_text.png", result)
