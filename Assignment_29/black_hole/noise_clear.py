import cv2
import numpy as np

images = []
image_without_noise = []

for folder in range(1, 5):
    sum_of_image = None
    for image_in_folder in range(1, 6):
        path = f"Assignment_29/black_hole/input/{folder}/{image_in_folder}.jpg"
        image = cv2.imread(path)
        images.append(image.astype(np.float32))

        if sum_of_image is None:
            sum_of_image = np.zeros(image.shape)

        sum_of_image += image

    average_image = (sum_of_image / len(images))
    average_image = average_image.astype(np.uint8)
    image_without_noise.append(average_image)


counter = 1
for image in image_without_noise:
    output_path = f"Assignment_29/black_hole/output/image_without_noise{counter}.jpg"
    cv2.imwrite(output_path, image)
    counter += 1

outputs = [cv2.imread(
    f"Assignment_29/black_hole/output/image_without_noise{i}.jpg") for i in range(1, 5)]

output_concatenate_1 = np.concatenate((outputs[0], outputs[1]), axis=1)
output_concatenate_2 = np.concatenate((outputs[2], outputs[3]), axis=1)

result = np.concatenate((output_concatenate_1, output_concatenate_2), axis=0)
cv2.imshow("", result)
cv2.waitKey(0)
