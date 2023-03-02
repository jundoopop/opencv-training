import cv2 as cv

img = cv.imread("../source/paris.jpg")

while cv.waitKey(0) != ord("q"):
    cv.imshow('default', img)
    cv.imshow('canny', cv.Canny(img, 100, 250))

cv.destroyAllWindows()
exit(0)
