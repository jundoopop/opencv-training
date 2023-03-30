import cv2 as cv
import numpy as np
import GaussianGenerator as gg

# define the file path
source_directory = "../../../source/paris.jpg"

# allocated same photo to different variables
# to compare functions clearly
# image1 is for manual function
image1 = np.array(cv.imread(source_directory))
# image2 is for built-in function
image2 = cv.imread(source_directory)

# compare with self-made and opencv built-in method
# windows are appeared until Q keyboard be pressed
ksize = 5
sd = 1
while cv.waitKey(0) != ord("q"):
    # avg mask applied
    cv.imshow("blurred manually", cv.filter2D(image1, -1, gg.gaussianMask(ksize, sd)))
    # opencv cv2.GaussianBlur() applied
    cv.imshow("built-in blur", cv.GaussianBlur(image2, (5, 5), sigmaX=1))

# after Q key pressed
cv.destroyAllWindows()
exit(0)
