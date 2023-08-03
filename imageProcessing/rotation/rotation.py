import cv2 as cv
import numpy as np


def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    middle_x, middle_y = cols // 2, rows // 2

    # Convert the angle from degrees to radians
    radian = angle * np.pi / 180

    # Create a rotated canvas to paste the rotated image
    result = np.zeros_like(image)

    # Perform the rotation
    for x in range(cols):
        for y in range(rows):
            # Set the rotated coordinate of X
            rotated_x = int(
                x * np.cos(radian)
                + y * np.sin(radian)
                - middle_x * np.cos(radian)
                - middle_y * np.sin(radian)
                + middle_x
            )
            # Set the rotated coordinate of Y
            rotated_y = int(
                (-1) * x * np.sin(radian)
                + y * np.cos(radian)
                + middle_x * np.sin(radian)
                - middle_y * np.cos(radian)
                + middle_y
            )

            # Check if the rotated coordinates are within the image boundaries
            if 0 <= rotated_x < cols and 0 <= rotated_y < rows:
                result[rotated_y, rotated_x] = image[y, x]

    return result
