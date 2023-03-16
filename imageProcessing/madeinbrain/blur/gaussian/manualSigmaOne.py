import numpy as np


def gaussianManual(img, ):
    row = len(img)
    column = len(img[0])
    gaussian_sigma_one = np.array(
        [[1, 4, 7, 4, 1],
         [4, 16, 26, 16, 4],
         [7, 26, 41, 26, 7],
         [4, 16, 26, 16, 4],
         [1, 4, 7, 4, 1]], np.float64)

    # get a computed pixel value by each
    def average_mask(target_pixel_y, target_pixel_x):

        ksize = 5

        # declare variables for computing
        # valid_masks : how many elements are valid in the mask
        valid_masks = 0
        # sum_of_pixel : sum of pixel values inside the mask
        sum_of_pixel = 0

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
                    sum_of_pixel += img[y_coordinate][x_coordinate] * gaussian_sigma_one[i][j]
                    valid_masks += gaussian_sigma_one[i][j]

        # result value
        result = sum_of_pixel // valid_masks

        return result.astype(np.uint8)

    # new canvas to draw blurred picture declared
    # if pixels are consisted of b,g,r values by each
    if np.shape(img) == (row, column, 3):
        sketchbook = np.zeros((row, column, 3), dtype=np.uint8)
    # or gray value by each
    else:
        sketchbook = np.zeros((row, column), dtype=np.uint8)

    # iterate to draw new blurred picture
    for i in range(row):
        for j in range(column):
            sketchbook[i][j] = average_mask(i, j)

    return sketchbook
