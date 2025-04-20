from math import sqrt
import cv2 as cv
import numpy as np


def distance(a, b):
    return np.sum(np.square(a - b))


def point_line_distance(point, start, end):
    if start == end:
        return distance(point, start)
    else:
        n = abs(
            (end[0] - start[0]) * (start[1] - point[1])
            - (start[0] - point[0]) * (end[1] - start[1])
        )
        d = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        return n / d


def rdp(pointList, epsilon):
    dmax = 0.0
    index = 0
    for i in range(1, len(pointList) - 1):
        d = point_line_distance(pointList[i], pointList[0], pointList[-1])
        if d > dmax:
            index = i
            dmax = d

    if dmax >= epsilon:
        resultList = rdp(pointList[: index + 1], epsilon)[:-1] + rdp(
            pointList[index:], epsilon
        )
    else:
        resultList = [pointList[0], pointList[-1]]

    return resultList
