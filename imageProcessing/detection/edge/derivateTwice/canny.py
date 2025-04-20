import numpy as np
import cv2

Gx = np.array(
    [
        [
            -1,
            0,
            1,
        ],
        [-2, 0, 2],
        [-1, 0, 1],
    ]
)
Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

magnitude = np.sqrt(np.power(Gx, 2) + np.power(Gy, 2))
