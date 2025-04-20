import cv2 as cv
import numpy as np

# define the file path
source_directory = "../../../source/paris.jpg"

# kernel size : 5
# sigma value : 1
# sum of each masks are 273
gaussian_sigma_one = np.array(
    [[1, 4, 7, 4, 1],
     [4, 16, 26, 16, 4],
     [7, 26, 41, 26, 7],
     [4, 16, 26, 16, 4],
     [1, 4, 7, 4, 1]], np.float64)

# allocated same photo to different variables
# to compare functions clearly
# image1 is for manual function
# uint16 is for prevention of error caused by modulo
image = np.array(cv.imread(source_directory), dtype=np.uint16)

# compare with self-made and opencv built-in method
# windows are appeared until Q keyboard be pressed
while cv.waitKey(0) != ord("q"):
    # filter2D with ksize : 5 gaussian filter
    cv.imshow("built-in blur", cv.filter2D(image, -1, gaussian_sigma_one))

# after Q key pressed
cv.destroyAllWindows()
exit(0)
