import cv2 as cv

img = cv.imread("/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/citations.jpeg")

while cv.waitKey(0) != ord("q"):
    cv.imshow('default', img)
    cv.imshow('canny', cv.Canny(img, 200, 250))

cv.destroyAllWindows()
exit(0)
