import cv2

actor_image = cv2.imread("Assignment_26/actor.jpg")

dead_person_image = cv2.cvtColor(actor_image, cv2.COLOR_BGR2GRAY)

for i in range(20, 100):
    dead_person_image[i-20, 80-i:100-i] = 0

for i in range(80, 100):
    dead_person_image[i-20, 0:100-i] = 0

cv2.imwrite("dead_person_image.jpg" ,dead_person_image)

cv2.imshow("Gray image", dead_person_image)
cv2.waitKey(0)
