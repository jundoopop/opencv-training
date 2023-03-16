import imageProcessing.madeinbrain.blur.gaussian.manualSigmaOne as gaus
import cv2 as cv
import numpy as np

# define the file path
source_directory = "../../../source/paris.jpg"

# allocated same photo to different variables
# to compare functions clearly
# image1 is for manual function
image1 = np.array(cv.imread(source_directory), dtype=np.uint16)
# image2 is for built-in function
image2 = cv.imread(source_directory)

# compare with self-made and opencv built-in method
# windows are appeared until Q keyboard be pressed
while cv.waitKey(0) != ord("q"):
    # avg mask applied
    cv.imshow("blurred manually", gaus.gaussianManual(image1))
    # opencv cv2.GaussianBlur() applied
    cv.imshow("built-in blur", cv.GaussianBlur(image2, (5, 5), sigmaX=1))

# after Q key pressed
cv.destroyAllWindows()
exit(0)
