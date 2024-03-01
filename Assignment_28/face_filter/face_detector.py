import cv2
import numpy as np

# image = cv2.imread("Assignment_28/face_filter/face.jpeg")
webcam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
lip_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml")
eye_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml")


def sticker_face_filter(image, sticker):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_stick = face_detector.detectMultiScale(frame_gray, 1.3)
    for (x, y, w, h) in faces_stick:
        sticker = cv2.resize(sticker, [w, h])
        for i in range(h):
            for j in range(w):
                if sticker[i][j][0] == 0 and sticker[i][j][1] == 0 and sticker[i][j][2] == 0:
                    sticker[i][j] = image[y+i, x+j]
        frame[y:y+h, x:x+w] = sticker

    return image


def glasses_and_lips_filter(image, faces, eyes, lips):
    ...


def chess_board_filter(image):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3)
    for face in faces:
        x, y, w, h = face
        image_face = image[y:y+w, x:x+h]
        image_face_small = cv2.resize(image_face, [20, 20])
        image_face_big = cv2.resize(
            image_face_small, [w, h], interpolation=cv2.INTER_NEAREST)
        image[y:y+w, x:x+h] = image_face_big

    return image


def mirror_filter(image):
    col = image.shape[1]
    flipVertical = cv2.flip(image[:,:col//2], 1)
    image[:,col//2:] = flipVertical

    return image


tiger_sticker = cv2.imread("Assignment_28/face_filter/tiger.png")
glasses_sticker = cv2.imread(
    "Assignment_28/face_filter/glasses.png", cv2.IMREAD_UNCHANGED)
lip_sticker = cv2.imread(
    "Assignment_28/face_filter/lips.png", cv2.IMREAD_UNCHANGED)

while True:
    _, frame = webcam.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3)
    eyes = eye_detector.detectMultiScale(frame_gray, 1.3, 20)
    lips = lip_detector.detectMultiScale(frame_gray, 1.3)
    key = cv2.waitKey(100) & 0xFF
    if key == ord('1'):
        image = sticker_face_filter(frame, tiger_sticker)
    if key == ord('2'):
        image = glasses_and_lips_filter(frame, faces, eyes, lips)
    if key == ord('3'):
        image = chess_board_filter(frame)
    if key == ord('4'):
        image = mirror_filter(frame)

    cv2.imshow("result", frame)
    if key == ord('q'):
        break
