import cv2 as cv
import numpy as np

# get image file
directory = 'imageProcessing/source/paris.jpg'
color = cv.IMREAD_GRAYSCALE
img = cv.imread(directory, color)
window_name = "Roberts Filter Applied"


def convolution(src):
    # each others are rotated by pi/4

    gx = np.array([[1, 0], [0, -1]], dtype=np.float32)
    gy = np.array([[0, 1], [-1, 0]], dtype=np.float32)

    x_convoluted = cv.filter2D(src, -1, gx)
    y_convoluted = cv.filter2D(src, -1, gy)

    roberts_applied = np.sqrt(x_convoluted ** 2 + y_convoluted ** 2)

    return roberts_applied


# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    cv.imshow(window_name, convolution(img))

cv.destroyAllWindows()
exit(0)
