import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()

    resized_frame = cv2.resize(frame, (640, 480))
    cv2.rectangle(resized_frame, (290, 210), (350, 270), (0, 255, 0), 2)
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    square_target = gray_frame[210:270, 290:350]
    detector = np.median(square_target)

    label = ""
    if detector >= 130:
        label = "White"
    elif 100 <= detector <= 129:
        label = "Gray"
    else:
        label = "Black"

    text_x, text_y = 280, 190

    cv2.putText(resized_frame, f"{label}", (text_x, text_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("", resized_frame)

    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

camera.release()
