# computes the blurred pixel value
import numpy as np


# apply the average mask
def apply_mask(image, size_of_kernel):
    # length of the row of the image
    def get_image_row(img):
        return len(img)

    # length of the column of the image
    def get_image_col(img):
        return len(img[0])

    # get a computed pixel value by each
    def average_mask(img, ksize, target_pixel_y, target_pixel_x):
        # get the lengths of row and column
        row = get_image_row(img)
        column = get_image_col(img)

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

        return result

    # number to make new canvas
    row_of_image, col_of_image = get_image_row(image), get_image_col(image)

    # new canvas to draw blurred picture declared
    sketchbook = np.zeros((row_of_image, col_of_image), dtype=np.uint8)
    # iterate for each pixel
    for i in range(row_of_image):
        for j in range(col_of_image):
            sketchbook[i][j] = average_mask(image, size_of_kernel, i, j)

    return sketchbook
