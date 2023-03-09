import cv2 as cv
import numpy as np

# get image file
directory = "../source/paris.jpg"
img = cv.imread(directory)

# initialise the size of the kernel, which sets the grids
kernel_size = 3

# before Q keyboard is pressed, the window cv2.boxFilter() blurring would be returned
while cv.waitKey(0) != ord("q"):
    cv.imshow('Blur : cv2.boxFilter()', cv.boxFilter(img, -1, (kernel_size, kernel_size)))

# when Q keyboard pressed, windows are destroyed
cv.destroyAllWindows()
# and exited with code 0
exit(0)
