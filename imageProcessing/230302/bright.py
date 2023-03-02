import cv2 as cv


def bright(img, val, row, column):
    # iterate all of pixels
    for i in range(row):
        for j in range(column):
            img[i][j] += val

    return img


image = cv.imread("../source/paris.jpg", cv.IMREAD_GRAYSCALE)

row_of_image = len(image)
col_of_image = len(image[0])

# open both of manual and opencv implements
while cv.waitKey(0) != ord("q"):
    cv.imshow("brighten 50, manual", bright(image, 50, row_of_image, col_of_image))
    cv.imshow("brighten 50, opencv", cv.add(image, 50))

cv.destroyAllWindows()
