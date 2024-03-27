import cv2
import numpy as np
from math import degrees, acos
from TFLiteFaceDetector import UltraLightFaceDetecion

def detect_and_align_face(image_path):
    """
    Detects a face in an image, extracts left and right eye coordinates,
    and performs alignment based on the eye positions.

    Args:
        image_path (str): Path to the image file.

    Returns:
        numpy.ndarray: The aligned image.
    """

    # Load the image in BGR color format (OpenCV standard)
    image = cv2.imread(image_path)

    # Load a pre-trained face detection model (e.g., Haar cascade)
    face_detector = UltraLightFaceDetecion(
    "Assignment_30/weights/RFB-320.tflite", conf_threshold=0.88)

    # Detect faces in the image
    boxes, scores = face_detector.inference(image)

    if len(boxes) == 0:
        print("No face detected in the image.")
        return None

    # Extract the first detected face (assuming single-face scenario)
    print(boxes)
    (x, y, w, h) = boxes[0]
    face_region = image[y:y+h, x:x+w]

    # Eye detection (replace with a more robust method if needed)
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  # Load eye detection model
    eyes = eye_cascade.detectMultiScale(face_region, scaleFactor=1.1, minNeighbors=2)

    # Check if both eyes are detected
    if len(eyes) != 2:
        print("Could not detect both eyes. Alignment might be inaccurate.")
        return None

    # Extract left and right eye coordinates
    left_eye = eyes[0]
    right_eye = eyes[1]
    left_eye_x, left_eye_y = left_eye[0], left_eye[1]
    right_eye_x, right_eye_y = right_eye[0], right_eye[1]

    # Calculate the rotation angle
    dx = right_eye_x - left_eye_x
    dy = right_eye_y - left_eye_y

    if dy != 0:  # Avoid division by zero
        angle = degrees(acos(dx / (np.sqrt(dx**2 + dy**2))))

    else:
        # Handle cases where eyes are on the same horizontal line (potential for improvement)
        angle = 0

    # Determine rotation direction (clockwise or counter-clockwise)
    if left_eye_y > right_eye_y:
        direction = -1  # Counter-clockwise rotation
    else:
        direction = 1  # Clockwise rotation

    # Rotate the image based on the calculated angle and direction
    center = (x + w // 2, y + h // 2)  # Center of the face region
    image_center = tuple(np.int0(center)) # type: ignore
    rotation_matrix = cv2.getRotationMatrix2D(image_center, direction * angle, 1.0)
    aligned_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))  # Maintain original dimensions

    return aligned_image

# Example usage
aligned_image = detect_and_align_face("Assignment_30/image_without_align.png")

cv2.imshow("", aligned_image) # type: ignore
cv2.waitKey(0)
