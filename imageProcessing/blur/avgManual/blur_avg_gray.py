import cv2 as cv
import numpy as np
import imageProcessing.blur.avgManual.allOneMask as avg

# get the image from the directory
# use uint16 to prevent from modulo, when average_mask method computes the number which is higher than 255
directory = "../../../source/bridge.jpg"
img = np.array(cv.imread(directory, cv.IMREAD_GRAYSCALE), dtype=np.uint16)

# size of the kernel, ksize * ksize mask would be applied
ksize = 5

# window is showed before Q key pressed
while cv.waitKey(0) != ord("q"):
    window_name = "grayscale blur"
    cv.namedWindow(f"manual - {window_name}")
    cv.imshow(f"manual - {window_name}", avg.apply_mask(img, ksize))

# close all windows when Q key pressed
cv.destroyAllWindows()
# exit code 0
exit(0)
