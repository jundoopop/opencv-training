import PIL.ImageShow
import cv2 as cv
from PIL import Image, ImageShow
import numpy as np

img = cv.imread("../source/paris.jpg", flags=cv.IMREAD_GRAYSCALE)

row_img = len(img)
col_img = len(img[0])


def flip_xy(image, row, column):
    result = np.zeros((row_img, col_img), dtype=np.uint8)
    for i in range(row):
        for j in range(column):
            result[i][j] = image[row - i - 1][column - j - 1]

    return result


def flip_x(image, row, column):
    result = np.zeros((row_img, col_img), dtype=np.uint8)
    for i in range(row):
        for j in range(column):
            result[i][j] = image[row - i - 1][j]

    return result


def flip_y(image, row, column):
    result = np.zeros((row_img, col_img), dtype=np.uint8)
    for i in range(row):
        for j in range(column):
            result[i][j] = image[i][column - j - 1]

    return result


print(flip_xy(img, row_img, col_img)[0][0])
while cv.waitKey(0) != ord("q"):
    # matrix_of_image[row of image][column of image][one of the r,g,b]
    cv.imshow("default", img)
    cv.imshow("xy flip function", flip_xy(img, row_img, col_img))
    cv.imshow("x flip function", flip_x(img, row_img, col_img))
    cv.imshow("y flip function", flip_y(img, row_img, col_img))

cv.destroyAllWindows()
# matrix is the 3d array in colored photo
# matrix_of_image[row of image][column of image][one of the r,g,b]

# cv.imshow("flip", img[-1::-1][-1::-1][-1::-1])
