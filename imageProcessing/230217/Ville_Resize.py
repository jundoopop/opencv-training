import cv2 as cv
import numpy as np

ville = cv.imread("../source/paris.jpg")

while cv.waitKey(0) != ord("q"):
    cv.imshow('Default', ville)

cv.destroyAllWindows()
exit(0)
