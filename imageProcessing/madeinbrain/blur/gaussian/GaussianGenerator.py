import numpy as np

def gaussianMask(ksize, sigma):
    # Get the centre value
    centre = ksize // 2

    # Declare the default square mask
    # filled with zero
    kernel = np.zeros((ksize, ksize))

    # Calculate the values of the kernel
    # Based on Gaussian Distribution
    for i in range(ksize):
        for j in range(ksize):
            x = i - centre
            y = j - centre
            kernel[x, y] = (2.71 ** (-(x ** 2 + y ** 2) / (2 * sigma ** 2))) \
                           / (2 * 3.14 * (sigma ** 2))

    # Normalize the kernel so that its values sum to 1
    kernel /= np.sum(kernel)

    return kernel
