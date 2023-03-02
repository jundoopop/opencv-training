import numpy as np
import cv2 as cv

ville_gray = cv.imread('../source/paris.jpg', cv.IMREAD_GRAYSCALE)

dst_saturation = cv.add(ville_gray, 100)
dst_modulo = ville_gray + 100

while cv.waitKey(0) != ord("q"):
    cv.imshow("Ville Grey, Saturation", dst_saturation)
    cv.imshow("Ville Grey, Modulo", dst_modulo)
    cv.imshow("Ville Grey, Default", ville_gray)

cv.destroyAllWindows()
exit(0)
