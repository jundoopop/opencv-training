import numpy as np
import cv2 as cv

ville_gray = cv.imread('../source/paris.jpg', cv.IMREAD_COLOR)
zero_image = np.zeros(ville_gray.shape, ville_gray.dtype)

dst_contrast = cv.scaleAdd(ville_gray, 0.6, zero_image)
dst_contrast_up = cv.scaleAdd(ville_gray, 1.5, zero_image)

while cv.waitKey(0) != ord("q"):
    cv.imshow("Ville Grey, Default", ville_gray)
    cv.imshow("Ville Grey, Contrast Reduced", dst_contrast)
    cv.imshow("Ville Grey, Contrast Boosted", dst_contrast_up)

cv.destroyAllWindows()
exit(0)
