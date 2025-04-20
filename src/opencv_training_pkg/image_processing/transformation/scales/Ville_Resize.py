import cv2 as cv
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.normpath(os.path.join(script_dir, "..", "source", "paris.jpg"))
ville = cv.imread(image_path)

while cv.waitKey(0) != ord("q"):
    cv.imshow("Default", ville)

cv.destroyAllWindows()
exit(0)
