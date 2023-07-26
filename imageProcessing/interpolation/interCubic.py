import numpy as np


def bicubic_kernel(x, y, src):
    src = src.astype(np.float32)
    kernel = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [-3, 3, -2, -1], [2, -2, 1, 1]])  # Define the kernel
    temp = 0
    x -= 3
    y -= 3
    for i in range(kernel.shape[0]):  # Loop for thw row and column
        for j in range(kernel.shape[1]):
            if x == 0 or y == 0 or x == src.shape[1] - 1 or y == src.shape[0] - 1:
                continue
            else:
                temp += kernel[i, j] * src[y + i - 1, x + j - 1].astype(np.float32)  # Calculate the result
    return temp  # Return the result
