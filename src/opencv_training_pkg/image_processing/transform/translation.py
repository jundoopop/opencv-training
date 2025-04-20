import numpy as np


def move(img, move_x, move_y):
    row, col = img.shape  # Get the shape of the image
    newImg = np.zeros(
        (row, col), np.uint8
    )  # Create a new image with the same shape as the original
    newImg[move_y:, move_x:] = img[
        : row - move_y, : col - move_x
    ]  # Put the translated image in the new image
    return newImg


def move2(img, move_x, move_y):
    row, col = img.shape  # Get the shape of the image

    newImg = np.zeros(
        (row + move_y, col + move_x), np.uint8
    )  # Pad the image with zeros on the left and top sides
    newImg[move_y:, move_x:] = img  # Put the original image in the padded image

    # Crop the padded image to the original size
    return newImg[:row, :col]
