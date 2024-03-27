import time
import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

image = cv2.imread("Assignment_30/image.png")

fd = UltraLightFaceDetecion(
    "Assignment_30/weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("Assignment_30/weights/coor_2d106.tflite")

color = (255, 0, 0)

start_time = time.perf_counter()
boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    for index, p in enumerate(np.round(pred).astype(np.int16)):
        cv2.circle(image, tuple(p), 4, color, -1)
        cv2.putText(image, str(index), tuple(p), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

    lips_landmark = []
    for landmark in [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]:
        lips_landmark.append(pred[landmark])
    lips_landmark = np.array(lips_landmark, np.int16)

print(time.perf_counter() - start_time)
cv2.imshow("result", image)
cv2.waitKey(0)
# cv2.imwrite("Assignment_30/result.png", image)
