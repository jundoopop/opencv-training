import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("../source/paris.jpg")
img_gray = cv.imread("../source/paris.jpg", cv.IMREAD_GRAYSCALE)
img_equalize = cv.equalizeHist(cv.imread("../source/paris.jpg", cv.IMREAD_GRAYSCALE))

while cv.waitKey(0) != ord("q"):
    cv.imshow("ville, gray", img_gray)
    cv.imshow("ville, equalized", img_equalize)

    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

cv.destroyAllWindows()
exit(0)
