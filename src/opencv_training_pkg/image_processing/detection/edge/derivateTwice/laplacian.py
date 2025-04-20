import math

import numpy as np


def kernel(ksize, sigma):
    # Get the centre value
    centre = ksize // 2

    # Declare the default square mask
    # filled with zero
    kernel = np.zeros((ksize, ksize), dtype=np.float32)

    centre = ksize // 2
    for i in range(ksize):
        for j in range(ksize):
            x = i - centre
            y = j - centre
            kernel[i][j] = (x * x + y * y) / (-2.0 * ksize * ksize)
    kernel[centre][centre] -= np.sum(kernel) - kernel[centre][centre]

    # # Calculate the values of the kernel
    # # Based on Laplacian formula
    # for i in range(ksize):
    #     for j in range(ksize):
    #         x = i - centre
    #         y = j - centre
    #         # apply laplacian formula
    #         formula = (pow(x, 2) + pow(y, 2)) / (2 * pow(sigma, 2))
    #
    # kernel /= sum(kernel)

    return kernel
