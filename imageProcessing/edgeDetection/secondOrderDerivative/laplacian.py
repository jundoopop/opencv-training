import math

import numpy as np


def kernel(ksize, sigma):
    # Get the centre value
    centre = ksize // 2

    # Declare the default square mask
    # filled with zero
    kernel = np.zeros((ksize, ksize))

    # Calculate the values of the kernel
    # Based on Laplacian formula
    for i in range(ksize):
        for j in range(ksize):
            x = i - centre
            y = j - centre
            # apply laplacian formula
            formula = (pow(x, 2) + pow(y, 2)) / (2 * pow(sigma, 2))

            kernel[x, y] = (-1 * (1 / (math.pi * pow(sigma, 4)))) * (1 - formula) * np.exp(formula)

    kernel /= sum(kernel)

    return kernel
