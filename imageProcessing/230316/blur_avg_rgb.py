import cv2 as cv
import numpy as np


# change each default pixels to blurred ones
def apply_mask(image, sketchbook, size_of_kernel, row_of_image, col_of_image):
    for i in range(row_of_image):
        for j in range(col_of_image):
            sketchbook[i][j] = average_mask(image, size_of_kernel, i, j)

    return sketchbook.astype(dtype=np.uint8)


# computes the blurred pixel value
def average_mask(image, size_of_kernel, target_pixel_y, target_pixel_x):
    # declare variables for computing
    # count : how many elements are valid in the mask
    count = 0
    # sum_of_gray : sum of the gray pixel values inside the mask
    sum_of_colors = np.zeros(3)

    # compute with row * column for loop
    # i is a row
    for i in range(size_of_kernel):
        # j is a column
        for j in range(size_of_kernel):

            # the pixel's location, which consists the mask
            x_coordinate = target_pixel_x - (size_of_kernel // 2) + j
            y_coordinate = target_pixel_y - (size_of_kernel // 2) + i

            # check the row and column are out of the ranges
            # if targeted index is out of the range
            if x_coordinate > column - 1 or x_coordinate < 0 \
                    or y_coordinate > row - 1 or y_coordinate < 0:
                continue
            # if index is within the range
            else:
                sum_of_colors += image[y_coordinate][x_coordinate]
                count += 1

    # grayscale value
    result = sum_of_colors // count

    return result


# get the image from the directory
# use uint16 to prevent from modulo, when average_mask method computes the number which is higher than 255
img = np.array(cv.imread("../source/bridge.jpg"), dtype=np.uint16)

# get the length of the row and column of the image
row = len(img)
column = len(img[0])

# canvas to draw new blurred photo
new_photo = np.zeros((row, column), dtype=np.uint8)

# window is showed before Q key pressed
while cv.waitKey(0) != ord("q"):
    window_name = "colored blur"
    cv.namedWindow(f"manual - {window_name}")
    cv.imshow(f"manual - {window_name}", apply_mask(img, new_photo, 5, row, column))

# close all windows when Q key pressed
cv.destroyAllWindows()
# exit code 0
exit(0)
