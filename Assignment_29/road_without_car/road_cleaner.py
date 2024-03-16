import cv2
import numpy as np

video = cv2.VideoCapture("Assignment_29/road_without_car/input/cars.mp4")

frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

frames = []

for i in range(25):
    frame_id = np.random.randint(0, frame_count)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = video.read()
    frames.append(frame)

median_frame = np.median(frames, axis=0).astype(np.uint8)

cv2.imshow("frame", median_frame)
cv2.waitKey(0)
