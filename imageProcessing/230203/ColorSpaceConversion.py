import cv2 as cv
import numpy as np

img = cv.imread("../source/paris.jpg")
img_gray = cv.imread("../source/paris.jpg", cv.IMREAD_GRAYSCALE)

white = np.array([255, 255, 255], np.uint8)
img_CMY = white - img

while cv.waitKey(0) != ord("q"):
    cv.imshow("ville RGB", img)
    cv.imshow("ville HSV", cv.cvtColor(img, cv.COLOR_BGR2HSV))
    cv.imshow("ville CMY", img_CMY)

cv.destroyAllWindows()
exit(0)
