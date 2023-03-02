import cv2 as cv
import numpy as np

noise = cv.imread("source/noise.jpg")

while cv.waitKey(0) != ord("q"):
    cv.imshow('eroding morphology',
              cv.morphologyEx(noise, cv.MORPH_ERODE, np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8')))
    cv.imshow('dilating morphology',
              cv.morphologyEx(noise, cv.MORPH_DILATE, np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8')))
    cv.imshow('opening morphology',
              cv.morphologyEx(noise, cv.MORPH_OPEN, np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8')))
    cv.imshow('closing morphology',
              cv.morphologyEx(noise, cv.MORPH_CLOSE, np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]).astype('uint8')))
    cv.imshow('default', noise)

cv.destroyAllWindows()
exit(0)
