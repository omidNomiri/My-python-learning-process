import cv2

sad_people_image = cv2.imread("Assignment_26/sad_people.jpg")

happy_people_image = cv2.rotate(sad_people_image, cv2.ROTATE_180)

cv2.imwrite("happy_people_image.jpg" ,happy_people_image)

cv2.imshow("happy people image", happy_people_image)
cv2.waitKey(0)
