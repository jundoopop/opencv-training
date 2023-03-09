import cv2 as cv
import numpy as np

# get image file
directory = "../source/paris.jpg"
img = cv.imread(directory)

# if Q key pressed, all windows would be closed and the program exited
kernel_size = 3
while cv.waitKey(0) != ord("q"):
    cv.imshow('Original Image vs Blurred Image', cv.boxFilter(img, -1, kernel_size))

cv.destroyAllWindows()
exit(0)
