import PIL.ImageShow
import cv2
from PIL import Image, ImageShow
import numpy as np

img = Image.open("../source/paris.jpg")

# matrix is the 3d array in colored photo
# matrix_of_image[row of image][column of image][one of the r,g,b]
matrix_of_image = np.array(img)

row_of_image = len(matrix_of_image)
col_of_image = len(matrix_of_image[0])


def xy_flip(mat_img):
    output = []
    for i in range(row_of_image):
        output


print(matrix_of_image.shape)

# flipped version of matrices of images
# zero based, before the iteration
matrix_img_x_axis_flipped = np.zeros((row_of_image, col_of_image, 3))
matrix_img_y_axis_flipped = np.zeros((row_of_image, col_of_image, 3))
matrix_img_xy_flipped = Image.fromarray(matrix_of_image[-1::-1])

# iteration for x-axis flip
for i in range(row_of_image):
    matrix_img_x_axis_flipped[i] = matrix_of_image[row_of_image - 1 - i]

# iteration for y-axis flip
for i in range(col_of_image):
    matrix_img_x_axis_flipped[:, i] = matrix_of_image[:, col_of_image - 1 - i]

print(f"matrix_of_image[0][0] : {matrix_of_image[0, 0]}")
print(f"matrix_of_x_axis_flipped[0][0] : {matrix_img_x_axis_flipped[0, 0]}")

# show the flipped images
# ImageShow.show(img, "the real image")
# ImageShow.show(matrix_img_xy_flipped, "xy flipped")
ImageShow.show(Image.fromarray(matrix_img_x_axis_flipped, mode='RGB'), "x flipped")
cv2.imshow("x flipped", cv2.imread(matrix_img_x_axis_flipped, cv2.IMREAD_COLOR))
# ImageShow.show(Image.fromarray(matrix_img_y_axis_flipped), "x flipped")

# cv2.imshow("flip", np.flip(matrix_of_image))
