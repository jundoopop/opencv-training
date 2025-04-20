import cv2 as cv
import numpy as np
import imageProcessing.blur.gaussian.GaussianGenerator as gaussian

color = cv.IMREAD_GRAYSCALE


def convolution(address):
    # each others are rotated by pi/4
    src = np.array(cv.imread(address, color), dtype=np.float32)

    # Generate two different gaussian filters
    gausOne = gaussian.gaussianMask(3, 1)
    gausTwo = gaussian.gaussianMask(9, 1)

    # two edges
    dst1 = cv.filter2D(src, -1, gausOne)
    dst2 = cv.filter2D(src, -1, gausTwo)

    # operates magnitude
    result = dst1 - dst2

    return result
