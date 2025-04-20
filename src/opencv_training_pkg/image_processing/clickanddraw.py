# draw square
# make rgb changed through taskbar
import sys

import numpy as np
import cv2 as cv


# def draw_rectangle(event, x, y, img, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.rectangle(img, (x - 50, y - 50), (x + 50, y + 50), (100, 80, 0), 3)
#         print("left button pressed.")


# image_file[:] = cv.add(image_file, cv.Scalar(col, col, col))


def nothing():
    pass


window_title = 'ville'
cv.namedWindow(window_title)

img = cv.imread("source/paris.jpg")
if img is None:
    sys.exit("Could not read the image.")

cv.createTrackbar('Color Density', window_title, 0, 255, nothing)
# cv.setMouseCallback(window_title, draw_rectangle)

while True:
    color = cv.getTrackbarPos('Color Density', window_title)
    cv.imshow(window_title, cv.convertScaleAbs(img, 0.1, color))


    if cv.waitKey(50) == ord("q"):
        break

cv.destroyAllWindows()

#

# Create a black image
# Draw a diagonal blue line with thickness of 5 px
# cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
