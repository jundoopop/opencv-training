import numpy as np

def bicubic_kernel(x, y, src):
    kernel = np.array([[1, ], [2, 4, 2], [1, 2, 1]])  # Define the kernel
    temp = 0
    x -= 2
    y -= 2
    for i in range(kernel.shape[0]):  # Loop for thw row and column
        for j in range(kernel.shape[1]):
            if x == 0 or y == 0 or x == src.shape[1] - 1 or y == src.shape[0] - 1:
                continue
            else:
                temp += kernel[i, j] * src[y + i - 1, x + j - 1]  # Calculate the result
    return temp / 16  # Return the result

