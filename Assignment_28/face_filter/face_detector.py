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
    for lip in lips :
        x_lip , y_lip , w_lip , h_lip = lip
        resized_lip = cv2.resize (lip_sticker , [w_lip , h_lip])

        for i in range (w_lip) :
            for j in range (h_lip) :
                if resized_lip[i][j][0] == resized_lip[i][j][1] == resized_lip[i][j][2] == 0 :
                    resized_lip[i][j] = image [y_lip + i , x_lip + j]

        image [y_lip : y_lip + h_lip , x_lip : x_lip + w_lip] = resized_lip
    
    for face in faces :
        x_face , y_face , w_face , h_face = face

        for eye in eyes :
            x_eye , y_eye , w_eye , h_eye = eye
            resized_glasses = cv2.resize (glasses_sticker , [w_face , h_eye + 20])

            for row in range (w_eye + 20) :
                for col in range (h_face) :
                    if resized_glasses[row][col][0] == resized_glasses[row][col][1] == resized_glasses[row][col][2] == 0 :
                        resized_glasses[row][col] = image [y_eye + row , x_face + col]

            image [y_eye : y_eye + h_eye + 20 , x_face : x_face + w_face] = resized_glasses
    return image


def chess_board_filter(image):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3)
    for face in faces:
        x, y, w, h = face
        image_face = image[y:y+w, x:x+h]
        resized_image_to_small = cv2.resize(image_face, [10, 10])
        resized_image_to_big = cv2.resize(
            resized_image_to_small, [w, h], interpolation=cv2.INTER_NEAREST)
        image[y:y+w, x:x+h] = resized_image_to_big

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
