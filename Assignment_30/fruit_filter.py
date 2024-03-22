import time
import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def zoom_effect(image, landmark, fruit):
    mask = np.zeros(image.shape,dtype=np.uint8)
    cv2.drawContours(mask,[landmark],-1,(255,255,255),-1)
    mask = mask / 255
    result = cv2.multiply(image, mask)
    print(mask)
    return result


image = cv2.imread("Assignment_30/image.png")
fruit_image = cv2.imread("Assignment_30/fruit.png")

fd = UltraLightFaceDetecion(
    "Assignment_30/weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("Assignment_30/weights/coor_2d106.tflite")

color = (255, 0, 0)

start_time = time.perf_counter()
boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    lips_landmark = []
    for landmark in [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]:
        lips_landmark.append(pred[landmark])
    lips_landmark = np.array(lips_landmark, np.int16)
    result = zoom_effect(image, lips_landmark, fruit_image)

print(time.perf_counter() - start_time)
cv2.imshow("result", result)
cv2.waitKey(0)
