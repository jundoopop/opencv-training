import numpy as np
import cv2


def nonmax_suppression(sobel, direct):
    rows, cols = sobel.shape[:2]
    dst = np.zeros((rows, cols), dtype=np.float32)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            values = sobel[i - 1 : i + 2, j - 1 : j + 2].flatten()
            first = [3, 0, 1, 2]
            id = first[direct[i, j]]
