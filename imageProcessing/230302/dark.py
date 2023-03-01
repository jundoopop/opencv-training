import cv2 as cv


def dark(img, val, row, column):
    for i in range(row):
        for j in range(column):
            img[i][j] -= val

    return img


image = cv.imread("../source/paris.jpg", cv.IMREAD_GRAYSCALE)

row_of_image = len(image)
col_of_image = len(image[0])

while cv.waitKey(0) != ord("q"):
    cv.imshow("darken 30, manual", dark(image, 30, row_of_image, col_of_image))
    cv.imshow("darken 30, opencv", cv.subtract(image, 30))

cv.destroyAllWindows()
