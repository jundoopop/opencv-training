import cv2 as cv
import numpy as np
import imageProcessing.madeinbrain.blur.avgManual.allOneMask as avg

# change each default pixels to blurred ones


# get the image from the directory
# use uint16 to prevent from modulo, when average_mask method computes the number which is higher than 255
directory = "../../../source/bridge.jpg"
img = np.array(cv.imread(directory), dtype=np.uint16)

# get the length of the row and column of the image
row = len(img)
column = len(img[0])

# canvas to draw new blurred photo
new_photo = np.zeros((row, column, 3), dtype=np.uint8)

# window is showed before Q key pressed
while cv.waitKey(0) != ord("q"):
    window_name = "colored blur"
    cv.namedWindow(f"manual - {window_name}")
    cv.imshow(f"manual - {window_name}", avg.apply_mask(img, 5))

# close all windows when Q key pressed
cv.destroyAllWindows()
# exit code 0
exit(0)
