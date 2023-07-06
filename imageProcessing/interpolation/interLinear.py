"""
Implemented bilinear interpolation in openCV
using the following formula:
f(x,y) = (1-w)(1-h)f(0,0) + w(1-h)f(1,0) + (1-w)hf(0,1) + whf(1,1)

where w = x - floor(x) and h = y - floor(y)

"""

import cv2 as cv
import numpy as np


# Calculating bilinear interpolation pixel value
def bi_inter(x, y, src):
    '''Interpolate (x,y) from values associated with four points.
    The four points are a list of four triplets: (x, y, value).
    The four points can be in any order. They should form a rectangle.
    '''

    # Prevent the index error
    if x >= src.shape[1] - 1:
        x = x - 1
    if y >= src.shape[0] - 1:
        y = y - 1

    # Declare four points for interpolation
    left_up, right_up, left_down, right_down = \
        src[y, x], src[y, x + 1], src[y + 1, x], src[y + 1, x + 1]  # Set the values in the four corners from the image

    # Interpolate between the top two corners and the bottom two corners
    if left_up + right_up == 0:
        upper_avg = 0
    else:
        upper_avg = np.average([left_up, right_up],
                               weights=[left_up, right_up])  # Weighted average of the upper two corners

    if right_down + left_down == 0:  # If the value of the upper two corners or the lower two corners is 0
        lower_avg = 0
    else:
        lower_avg = np.average([left_down, right_down],
                               weights=[left_down, right_down])  # Weighted average of the lower two corners

    # Return the result of the interpolation
    if upper_avg + lower_avg == 0:
        return 0
    else:
        return np.clip(np.average([upper_avg, lower_avg],
                                  weights=[upper_avg, lower_avg]), 0, 255)  # Weighted average of the two averages


def wavg(p1, p2):  # Weighted average of the two points
    return p1 * p1 / (p1 + p2) + p2 * p2 / (p1 + p2)
