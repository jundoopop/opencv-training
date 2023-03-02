import cv2 as cv

noise = cv.imread("source/noise.jpg")

while cv.waitKey(0) != ord("q"):
    cv.imshow()


cv.destroyAllWindows()
exit(0)
