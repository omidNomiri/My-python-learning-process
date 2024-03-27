import cv2

webcam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
lip_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml")
eye_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")


def sticker_face_filter(image):
    tiger_sticker = cv2.imread("Assignment_28/face_filter/tiger.png")
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_stick = face_detector.detectMultiScale(frame_gray, 1.3)
    for (x, y, w, h) in faces_stick:
        tiger_sticker = cv2.resize(tiger_sticker, [w, h])
        for i in range(h):
            for j in range(w):
                if tiger_sticker[i][j][0] == 0 and tiger_sticker[i][j][1] == 0 and tiger_sticker[i][j][2] == 0:
                    tiger_sticker[i][j] = image[y+i, x+j]
        frame[y:y+h, x:x+w] = tiger_sticker

    return image


def glasses_and_lips_filter(image):
    glasses_sticker = cv2.imread(
        "Assignment_28/face_filter/glasses.png", cv2.IMREAD_UNCHANGED)
    lip_sticker = cv2.imread(
        "Assignment_28/face_filter/lips.png", cv2.IMREAD_UNCHANGED)

    eyes = eye_detector.detectMultiScale(frame_gray, 1.5, maxSize=(50, 50))
    lips = lip_detector.detectMultiScale(frame, 1.3, 45)

    if image.shape[2] == 4:
        image = image[:, :, :3]

    for lips in lips:
        x, y, w, h = lips

        lips_sticker_resized = cv2.resize(lip_sticker, (w, h))

        sticker_alpha_lips = lips_sticker_resized[:, :, 3] / 255
        sticker_inv_alpha_lips = 1.0 - sticker_alpha_lips
        face_region_lips = image[y:y + h, x:x + w]

        for channel in range(3):
            face_region_lips[:, :, channel] = (sticker_alpha_lips * lips_sticker_resized[:, :, channel] +
                                        sticker_inv_alpha_lips * face_region_lips[:, :, channel])

    if len(eyes) >= 2:
        x_mid = sum((x + w // 2) for (x, y, w, h) in eyes) / len(eyes)
        y_mid = sum((y + h // 2) for (x, y, w, h) in eyes) / len(eyes)

        width, height = 150, 100

        x_sticker = x_mid - width // 2
        y_sticker = y_mid - height // 2

        glasses = cv2.resize(glasses_sticker, (width, height))

        glass_alpha = glasses[:, :, 3] / 255
        sticker_inv_alpha = 1 - glass_alpha
        face_region = image[int(y_sticker):int(
            y_sticker + height), int(x_sticker):int(x_sticker + width)]

        for channel in range(3):
            face_region[:, :, channel] = (glass_alpha * glasses[:, :, channel] +
                                    sticker_inv_alpha * face_region[:, :, channel])
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
    flipVertical = cv2.flip(image[:, :col//2], 1)
    image[:, col//2:] = flipVertical

    return image


def set_filter(filter=1):
    if filter == 1:
        filter_selection = 1
    elif filter == 2:
        filter_selection = 2
    elif filter == 3:
        filter_selection = 3
    elif filter == 4:
        filter_selection = 4
    return filter_selection


filter_selection = 3
while True:
    _, frame = webcam.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3)
    key = cv2.waitKey(25) & 0xFF

    if key == ord('1'):
        filter_selection = set_filter(1)
    elif key == ord('2'):
        filter_selection = set_filter(2)
    elif key == ord('3'):
        filter_selection = set_filter(3)
    elif key == ord('4'):
        filter_selection = set_filter(4)

    if filter_selection == 1:
        image = sticker_face_filter(frame)
    elif filter_selection == 2:
        image = glasses_and_lips_filter(frame)
    elif filter_selection == 3:
        image = chess_board_filter(frame)
    elif filter_selection == 4:
        image = mirror_filter(frame)

    cv2.imshow("result", frame)
    if key == ord('q'):
        break
