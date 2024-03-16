import cv2

room_background = cv2.imread("Assignment_29/virtual_decoration/input/room.png")
room_foreground = cv2.imread("Assignment_29/virtual_decoration/input/floor_covering_image.png")
room_mask = cv2.imread("Assignment_29/virtual_decoration/input/room_mask.png")

normalized_mask = room_mask / 255.0

result_room_foreground = room_foreground * normalized_mask

mask_inverted = 255 - room_mask

normalized_mask_inverted = mask_inverted / 255.0

result_room_background = room_background * normalized_mask_inverted

result = result_room_foreground + result_room_background

cv2.imwrite("Assignment_29/virtual_decoration/output/result.png", result)
