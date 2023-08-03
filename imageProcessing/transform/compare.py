import cv2 as cv
import translation as tr
import numpy as np
from pathlib import Path

path = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg"  # Path to the image
sample1 = cv.imread(path, cv.IMREAD_GRAYSCALE)  # Get a first sample: Paris

filter = np.array(
    [[1, 0], [0, 1]], np.uint8
)  # Filter to apply to the image (2x2 matrix)

while cv.waitKey(20) != ord("q"):  # Wait for the user to press the "q" key
    cv.imshow("Default Sample Image", sample1)  # x: 50, y: 100 translation
    cv.imshow(
        "Move1 Translated - x: 0, y: 80", tr.move(sample1, 0, 80)
    )  # x: 0, y: 80 translation
    cv.imshow(
        "Move2 Translated - x: 0, y: 80", tr.move2(sample1, 0, 80)
    )  # x: 0, y: 80 translation

cv.destroyAllWindows()  # Close all windows
exit(0)  # Exit the program
