import math
import numpy as np
import cv2


def apply(ksize, sigma):
    kernel = np.zeros((ksize, ksize)).astype(np.float32)
    centre = ksize // 2
    for i in range(ksize):
        for j in range(ksize):
            # x, y are values for generating mask
            x = i - centre
            y = j - centre
            formula = -1 * (pow(x, 2) + pow(y, 2)) / (2 * pow(sigma, 2))
            kernel[i, j] = (1 / (math.pi * pow(sigma, 4))) * (1 + formula) * np.exp(formula)

    return kernel
