import cv2 as cv
import numpy as np

color = cv.IMREAD_GRAYSCALE


def convolution(address):
    # each others are rotated by pi/4
    src = np.array(cv.imread(address, color), dtype=np.float32)

    # 2 x 2 filters of x and y direction
    gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    gy = np.array([[1, 2, 1],
                   [-2, 0, 2],
                   [-1, -2, -1]])
    # two edges
    x_convoluted = cv.filter2D(src, -1, gx)
    y_convoluted = cv.filter2D(src, -1, gy)

    # operates magnitude
    roberts_applied = np.sqrt(pow(x_convoluted, 2) + pow(y_convoluted, 2)).astype(np.uint8)

    return roberts_applied
