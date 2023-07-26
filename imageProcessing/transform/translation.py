import numpy as np

def move(img, move_x, move_y):
    row, col = img.shape # Get the shape of the image
    img = img[move_y:, move_x:] # Just left the part of the image that will be visible after the translation
    newImg = np.zeros((row, col), np.uint8) # Create a new image with the same shape as the original
    newImg[move_y:, move_x:] = img # Put the translated image in the new image
    return newImg
