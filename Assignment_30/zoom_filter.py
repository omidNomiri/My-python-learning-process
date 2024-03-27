import time
import cv2
import numpy as np
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel


def find_body_part(part_of_face_landmarks_index):
    part_of_face_landmarks = []
    for landmark in part_of_face_landmarks_index:
        part_of_face_landmarks.append(pred[landmark])
    part_of_face_landmarks = np.array(part_of_face_landmarks, np.int16)
    part_of_face_mask = cut_face(image, part_of_face_landmarks)
    return part_of_face_mask


def cut_face(image, landmark):
    mask = np.zeros(image.shape, dtype=np.uint8)
    landmark = np.array(landmark, dtype=int)
    cv2.drawContours(mask, [landmark], -1, (255, 255, 255), -1)
    mask = mask // 255
    x, y, w, h = cv2.boundingRect(landmark)
    result = image * mask
    result = result[y:y+h, x:x+w]
    return result


def remove_background(part_of_face):
    tmp = cv2.cvtColor(part_of_face, cv2.COLOR_BGR2GRAY)

    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)

    b, g, r = cv2.split(part_of_face)

    rgba = [b, g, r, alpha]

    part_of_face = cv2.merge(rgba, 4)

    return part_of_face


def overlayPNG(imgBack, imgFront, pos=[0, 0]):
    hf, wf, cf = imgFront.shape
    hb, wb, cb = imgBack.shape

    x1, y1 = max(pos[0], 0), max(pos[1], 0)
    x2, y2 = min(pos[0] + wf, wb), min(pos[1] + hf, hb)

    x1_overlay = 0 if pos[0] >= 0 else -pos[0]
    y1_overlay = 0 if pos[1] >= 0 else -pos[1]

    wf, hf = x2 - x1, y2 - y1

    if wf <= 0 or hf <= 0:
        return imgBack

    alpha = imgFront[y1_overlay:y1_overlay + hf,
                     x1_overlay:x1_overlay + wf, 3] / 255.0
    inv_alpha = 1.0 - alpha

    imgRGB = imgFront[y1_overlay:y1_overlay +
                      hf, x1_overlay:x1_overlay + wf, 0:3]

    for c in range(0, 3):
        imgBack[y1:y2, x1:x2, c] = imgBack[y1:y2, x1:x2, c] * \
            inv_alpha + imgRGB[:, :, c] * alpha

    return imgBack


def add_filter(image, lips, right_eye, left_eye):
    lips = cv2.resize(lips, (0, 0), fx=2, fy=2)
    removed_background_lips = remove_background(lips)
    image = overlayPNG(image, removed_background_lips, pos=(720, 700))

    right_eye = cv2.resize(right_eye, (0, 0), fx=2, fy=2)
    removed_background_right_eye = remove_background(right_eye)
    image = overlayPNG(image, removed_background_right_eye, pos=(680, 480))

    left_eye = cv2.resize(left_eye, (0, 0), fx=2, fy=2)
    removed_background_left_eye = remove_background(left_eye)
    image = overlayPNG(image, removed_background_left_eye, pos=(950, 480))

    result = image
    return result


image = cv2.imread("image.png")

lips_landmarks_index = [52, 64, 63, 71, 67, 68, 61, 58, 59, 53, 56, 55]
left_eye_landmarks_index = [89, 90, 87, 91, 93, 96, 94, 95]
right_eye_landmarks_index = [39, 42, 40, 41, 35, 36, 33, 37]

fd = UltraLightFaceDetecion(
    "weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

start_time = time.perf_counter()
boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    lips = find_body_part(lips_landmarks_index)
    right_eye = find_body_part(right_eye_landmarks_index)
    left_eye = find_body_part(left_eye_landmarks_index)


result = add_filter(image, lips,
                    right_eye, left_eye)

cv2.imshow("result", result)
cv2.waitKey(0)
