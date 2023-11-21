import os
import imageio

file_list = sorted(os.listdir("Assignment_8/images"))

IMAGES = []
for file_name in file_list:
    file_path = "Assignment_8/images/" + file_name
    image = imageio.v2.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("Assignment_8/earth.gif", IMAGES)
