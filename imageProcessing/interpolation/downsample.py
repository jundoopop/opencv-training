"""
Downsizing: Set the ratio to 0.5
"""

import cv2 as cv
import numpy as np
import interLinear as il

img = cv.imread("../source/resize1.jpg", cv.IMREAD_GRAYSCALE)

if img is None:
    print("Can't read the image")
    exit(0)

ratio = 0.5  # Resize ratio

img = cv.imread("../source/resize1.jpg", cv.IMREAD_GRAYSCALE)
if img is None:
    print("Can't read the image")
    exit(0)

dsize = (int(len(img[0]) * ratio), int(len(img) * ratio))  # dsize[0] = width, dsize[1] = height

sketchbook_weighted = np.array(
    [[il.weighted_mean(int(i // ratio), int(j // ratio), img) for i in range(dsize[0])] for j in range(dsize[1])])

while cv.waitKey(0) != ord("q"):
    cv.imshow("Original", img)
    # CV library bilinear interpolation
    cv.imshow("CV library bilinear interpolation",
              cv.resize(img, dsize, fx=0, fy=0, interpolation=cv.INTER_LINEAR))

    # Custom bilinear interpolation formula -> Weighted mean
    cv.imshow("Custom bilinear interpolation - weighted mean",
              sketchbook_weighted.astype(np.uint8))

cv.destroyAllWindows()
exit(0)
