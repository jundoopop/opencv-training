# computes the blurred pixel value
import numpy as np


# apply the average mask
def apply_mask(image, size_of_kernel):
    # length of the row of the image
    row = len(image)
    # length of the column of the image
    column = len(image[0])

    # get a computed pixel value by each
    def average_mask(img, ksize, target_pixel_y, target_pixel_x):

        # declare variables for computing
        # valid_masks : how many elements are valid in the mask
        valid_masks = 0
        # sum_of_gray : sum of the gray pixel values inside the mask
        sum_of_gray = 0

        # compute with row * column for loop
        # iterator i is a row of image
        for i in range(ksize):
            # iterator j is a column of image
            for j in range(ksize):

                # the pixel's location, which consists the mask
                x_coordinate = target_pixel_x - (ksize // 2) + j
                y_coordinate = target_pixel_y - (ksize // 2) + i

                # check the row and column are out of the ranges
                # if targeted index is out of the range
                if x_coordinate > column - 1 or x_coordinate < 0 \
                        or y_coordinate > row - 1 or y_coordinate < 0:
                    continue
                # if index is within the range
                else:
                    sum_of_gray += image[y_coordinate][x_coordinate]
                    valid_masks += 1

        # result value
        result = sum_of_gray // valid_masks

        return result.astype(np.uint8)

    # new canvas to draw blurred picture declared
    if np.shape(image) == (row, column, 3):
        sketchbook = np.zeros((row, column, 3), dtype=np.uint8)
    else:
        sketchbook = np.zeros((row, column), dtype=np.uint8)

    # iterate for each pixel
    for i in range(row):
        for j in range(column):
            sketchbook[i, j] = average_mask(image, size_of_kernel, i, j)

    return sketchbook
