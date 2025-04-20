"""
Implemented bilinear interpolation in openCV
using the following formula:
f(x,y) = (1-w)(1-h)f(0,0) + w(1-h)f(1,0) + (1-w)hf(0,1) + whf(1,1)

where w = x - floor(x) and h = y - floor(y)

"""

import numpy as np


# Calculating bilinear interpolation pixel value
def weighted_mean(
    point_left_up, point_right_up, point_left_down, point_right_down, scale
):  # Get the pixel values of the four coordinates on the corner
    """Interpolate (x,y) from values associated with four points.
    The four points are a list of four triplets: (x, y, value).
    The four points can be in any order. They should form a rectangle.
    """

    """
    Bilinear Interpolation:
    1. Choose four nearest pixels (2 x 2)
    2. 1.5 upscale: make (2 x 2) to (3 x 3)
    3. 2 upscale: make (2 x 2) to (4 x 4)
    """

    pixel = 0

    if scale == 0.5:  # 50% downscale
        pixel = np.mean(
            [point_left_up, point_right_up, point_left_down, point_right_down]
        )

    elif scale == 1.5:  # 150% upscale
        # Interpolate between the top two corners and the bottom two corners

        # First Interpolation
        point_center_down = np.mean([point_left_down, point_right_down])
        point_center_up = np.mean([point_left_up, point_right_up])
        point_left_center = np.mean([point_left_up, point_left_down])
        point_right_center = np.mean([point_right_up, point_right_down])

        # Second Interpolation
        point_center_center = np.mean([point_center_down, point_center_up])

        # Upscaled Result
        pixel = np.array(
            [
                [point_left_up, point_center_up, point_right_up],  # First row
                [
                    point_left_center,
                    point_center_center,
                    point_right_center,
                ],  # Second row
                [point_left_down, point_center_down, point_right_down],
            ]
        )  # Third row

    elif scale == 2:  # 200% upscale
        # First Interpolation
        # Get values of the four corners
        point_0_1 = np.average(
            [point_left_up, point_right_up], weights=[1, 2]
        )  # (0, 1)
        point_0_2 = np.average(
            [point_left_up, point_right_up], weights=[2, 1]
        )  # (0, 2)
        point_1_0 = np.average(
            [point_left_up, point_left_down], weights=[1, 2]
        )  # (1, 0)
        point_2_0 = np.average(
            [point_left_up, point_left_down], weights=[2, 1]
        )  # (2, 0)
        point_3_1 = np.average(
            [point_left_down, point_right_down], weights=[1, 2]
        )  # (3, 1)
        point_3_2 = np.average(
            [point_left_down, point_right_down], weights=[2, 1]
        )  # (3, 2)
        point_1_3 = np.average(
            [point_right_up, point_right_down], weights=[1, 2]
        )  # (1, 3)
        point_2_3 = np.average(
            [point_right_up, point_right_down], weights=[2, 1]
        )  # (2, 3)

        # Second Interpolation
        point_1_1 = np.average([point_0_1, point_3_1], weights=[1, 2])  # (1, 1)
        point_1_2 = np.average([point_0_2, point_3_2], weights=[1, 2])  # (1, 2)
        point_2_1 = np.average([point_0_1, point_3_1], weights=[2, 1])  # (2, 1)
        point_2_2 = np.average([point_0_2, point_3_2], weights=[2, 1])  # (2, 2)

        # Upscaled Result
        pixel = np.array(
            [
                [point_left_up, point_0_1, point_0_2, point_right_up],  # First row
                [point_1_0, point_1_1, point_1_2, point_1_3],  # Second row
                [point_2_0, point_2_1, point_2_2, point_2_3],  # Third row
                [point_left_down, point_3_1, point_3_2, point_right_down],  # Fourth row
            ]
        )  

    return pixel  # Return the result of the interpolation


def legacy(src, x, y):
    # Declare four points for interpolation
    left_up, right_up, left_down, right_down = (
        src[y, x],
        src[y, x + 1],
        src[y + 1, x],
        src[y + 1, x + 1],
    )  # Set the values in the four corners from the image

    # Interpolate between the top two corners and the bottom two corners
    if left_up + right_up == 0:
        upper_avg = 0
    else:
        upper_avg = np.average(
            [left_up, right_up], weights=[left_up, right_up]
        )  # Weighted average of the upper two corners

    if (
        right_down + left_down == 0
    ):  # If the value of the upper two corners or the lower two corners is 0
        lower_avg = 0
    else:
        lower_avg = np.average(
            [left_down, right_down], weights=[left_down, right_down]
        )  # Weighted average of the lower two corners

    # # Return the result of the interpolation
    # if upper_avg + lower_avg == 0:
    #     return 0
    # else:
    #     return np.clip(np.average([upper_avg, lower_avg],
    #                               weights=[upper_avg, lower_avg]), 0, 255)  # Weighted average of the two averages


def bilinear_kernel(x, y, src):
    kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])  # Define the kernel
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
