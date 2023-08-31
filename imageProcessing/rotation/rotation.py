import cv2 as cv
import numpy as np


def rotate(image, angle):
    rows, cols, depth = image.shape
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
                (x - middle_x) * np.cos(radian)
                - (y - middle_y) * np.sin(radian)
                + middle_x
            )
            # Set the rotated coordinate of Y
            rotated_y = int(
                (y - middle_y) * np.cos(radian)
                + (x - middle_x) * np.sin(radian)
                + middle_y
            )

            # Check if the rotated coordinates are within the image boundaries
            if 0 <= rotated_x < cols and 0 <= rotated_y < rows:
                result[rotated_y, rotated_x] = image[y, x]

    return result


def rotate2(image, angle):
    rows, cols = image.shape
    middle_x, middle_y = cols // 2, rows // 2

    # Convert the angle from degrees to radians
    radian = angle * np.pi / 180

    # Create a rotated canvas to paste the rotated image
    result = np.zeros_like(image)

    # Perform the rotation
    for x in range(cols):
        for y in range(rows):
            # x_rotated_center = (middle_x * np.cos(radian) + middle_y * np.sin(radian)).astype(np.int32)
            # y_rotated_center = (middle_x * np.sin(radian) - middle_y * np.cos(radian)).astype(np.int32)

            # # Set the rotated coordinate of X and Y
            # x_adjust = middle_x - x_rotated_center
            # y_adjust = middle_y - y_rotated_center

            # Set the rotated coordinate of X
            rotated_x, rotated_y = np.matmul(
                [[np.cos(radian), np.sin(radian)], [np.sin(radian), np.cos(radian)]],
                np.array([x, y]).T,
            ).astype(np.int32)

            # Check if the rotated coordinates are within the image boundaries
            if 0 <= rotated_x < cols and 0 <= rotated_y < rows:
                result[rotated_y, rotated_x] = image[y, x]

    return result
