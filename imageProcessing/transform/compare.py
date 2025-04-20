import cv2 as cv
import translation as tr
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.normpath(os.path.join(script_dir, "..", "source", "paris.jpg"))

sample1 = cv.imread(image_path, cv.IMREAD_GRAYSCALE)  # Get a first sample: Paris

filter = np.array(
    [[1, 0], [0, 1]], np.uint8
)  # Filter to apply to the image (2x2 matrix)

while cv.waitKey(20) != ord("q"):  # Wait for the user to press the "q" key
    cv.imshow("Default Sample Image", sample1)
    cv.imshow(
        "Move1 Translated - x: 0, y: 80", tr.move(sample1, 0, 80)
    )  # x: 0, y: 80 translation
    cv.imshow(
        "Move2 Translated - x: 50, y: 100", tr.move(sample1, 50, 100)
    )  # x: 0, y: 80 translation

cv.destroyAllWindows()  # Close all windows
exit(0)  # Exit the program
