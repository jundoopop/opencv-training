import shear as sh
import cv2 as cv
import numpy as np

img_path1 = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg"  # Path to the first image
img_path2 = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/bridge.jpg"  # Path to the second image

img_sample = cv.imread(img_path1, cv.IMREAD_GRAYSCALE)  # Get a first sample: Paris
img_sample2 = cv.imread(
    img_path2, cv.IMREAD_GRAYSCALE
)  # Get a second sample: Bridge in London


# Check if path is validq
if img_sample is None:
    print("Could not read img_sample.")
    exit(0)

if img_sample2 is None:
    print("Could not read img_sample2.")
    exit(0)

# Show images
while cv.waitKey(20) != ord("q"):
    cv.imshow("Default Sample Image", img_sample)  # Show the default image
    cv.imshow(
        "Sheared Image: shear_x = 0.5, shear_y = 0.5", sh.shear(img_sample, 0.5, 0.5)
    )  # shear = 0.5 and y shear = 0.5

    cv.imshow(
        "Sheared Image 2: shear_x = 0.5, shear_y = 0.5", sh.shear(img_sample, 0.0, 0.5)
    )  # shear = 0.5 and y shear = 0.5


cv.destroyAllWindows()
exit(0)
