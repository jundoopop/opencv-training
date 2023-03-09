import cv2 as cv
import numpy as np


# change each default pixels to blurred ones
def apply_mask(image, sketchbook, size_of_kernel, row_of_image, col_of_image):
    for i in range(row_of_image):
        for j in range(col_of_image):
            sketchbook[i][j] = average_mask(image, size_of_kernel, i, j)

    return sketchbook


# computes the blurred pixel value
def average_mask(image, size_of_kernel, target_pixel_y, target_pixel_x):
    # declare variables for computing
    # count : how many elements are valid in the mask
    count = 0
    # sum_of_gray : sum of the gray pixel values inside the mask
    sum_of_gray = 0

    # compute with row * column for loop
    for i in range(size_of_kernel):
        for j in range(size_of_kernel):
            x_coordinate = target_pixel_x - size_of_kernel // 2 + j - 1
            y_coordinate = target_pixel_y - size_of_kernel // 2 + i - 1

            # check the row and column are out of the ranges
            # if targeted index is out of the range
            if x_coordinate > column - 1 or x_coordinate < 0 \
                    or y_coordinate > row - 1 or y_coordinate < 0:
                continue
            # if index is within the range
            else:
                image[y_coordinate][x_coordinate] += sum_of_gray
                count += 1

    result = sum_of_gray // count

    return result


# get the image from the directory
img = np.array(cv.imread("../source/bridge.jpg", cv.IMREAD_GRAYSCALE), dtype=np.uint16)

# get the length of the row and column of the image
row = len(img)
column = len(img[0])
new_photo = np.zeros((row, column), dtype=np.uint8)

# window is showed before Q key pressed
while cv.waitKey(0) != ord("q"):
    window_name = "grayscale blur"
    cv.namedWindow(f"manual - {window_name}")
    cv.imshow(f"manual - {window_name}", apply_mask(img, new_photo, 3, row, column))

# close all windows when Q key pressed
cv.destroyAllWindows()
# exit code 0
exit(0)
