import cv2 as cv
import numpy as np

# get image file
directory = "../source/paris.jpg"
img = cv.imread(directory)


def blur_with_avg(src, kernel_size):
    # Define the kernel for the average mask
    # when kernel size increases, blurring effects more
    kernel = np.ones((kernel_size, kernel_size), np.uint8) / (kernel_size ** 2)

    # return the result of blurring
    return cv.filter2D(src, -1, kernel)


# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    cv.imshow('Original Image vs Blurred Image', blur_with_avg(img, 3))

cv.destroyAllWindows()
exit(0)
