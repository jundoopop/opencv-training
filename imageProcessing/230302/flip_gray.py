import cv2 as cv
import numpy as np

# read image with applying grayscale by opencv
img = cv.imread("../source/paris.jpg", flags=cv.IMREAD_GRAYSCALE)

# length of each axes
row_img = len(img)
col_img = len(img[0])


# flipping asymmetric
def flip_xy(image, row, column):
    result = np.zeros((row_img, col_img), dtype=np.uint8)
    # replacing each gray pixels
    for i in range(row):
        for j in range(column):
            # matrix_of_image[row of image][column of image]
            result[i][j] = image[row - i - 1][column - j - 1]

    return result


# flipping by x-axis
def flip_x(image, row, column):
    result = np.zeros((row_img, col_img), dtype=np.uint8)
    # replacing each gray pixels
    for i in range(row):
        for j in range(column):
            # matrix_of_image[row of image][column of image]
            result[i][j] = image[row - i - 1][j]

    return result


# flipping by y-axis
def flip_y(image, row, column):
    result = np.zeros((row_img, col_img), dtype=np.uint8)
    # replacing each gray pixels
    for i in range(row):
        for j in range(column):
            # matrix_of_image[row of image][column of image]
            result[i][j] = image[i][column - j - 1]

    return result


# remain windows until 'q' keyboard pressed
while cv.waitKey(0) != ord("q"):
    # show default grayscale image to compare with
    cv.imshow("default", img)
    # showing windows of each flip, function executed
    cv.imshow("xy flip function", flip_xy(img, row_img, col_img))
    cv.imshow("x flip function", flip_x(img, row_img, col_img))
    cv.imshow("y flip function", flip_y(img, row_img, col_img))

cv.destroyAllWindows()
exit(0)
