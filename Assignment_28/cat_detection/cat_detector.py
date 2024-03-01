import cv2

cat_image = cv2.imread("Assignment_28/cat_detection/cat_image.png")
number_of_cat = 0
cat_detector = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     "haarcascade_frontalcatface.xml")

cats = cat_detector.detectMultiScale(cat_image)
for cat in cats:
    number_of_cat += 1
    x, y, w, h = cat
    cv2.rectangle(cat_image, [x, y], [x+w, y+h], (255, 255), 2)

print(f"number of cat: {number_of_cat}")
cv2.imshow("", cat_image)
cv2.waitKey(0)
