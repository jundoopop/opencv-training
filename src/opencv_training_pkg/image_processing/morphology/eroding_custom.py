import cv2 as cv
import numpy as np

"""
Mask for erosion:
[[0, 1, 0],
 [1, 1, 1],
 [0, 1, 0]]

Value 1 means white.
This code is for comparing with pixels around the targeted pixel.
"""


def carve(src):
    sketchbook = np.zeros(
        src.shape, dtype=np.uint8
    )  # Sketchbook is a canvas for eroding. Newly drawn pixels.

    # Loop for thw row and column
    for i in range(0, src.shape[0]):
        for j in range(0, src.shape[1]):
            if i == 0 or j == 0 or i == src.shape[0] - 1 or j == src.shape[1] - 1:
                continue
            if (  # Check if the pixel is surrounded by white pixels.
                # Compare the pixel on centre of the kernel with the pixels toward four directions.
                src[i, j]  # Centre
                == src[i - 1, j]  # Upside
                == src[i + 1, j]  # Downside
                == src[i, j - 1]  # Leftside
                == src[i, j + 1]  # Rightside
                == 255  # White
            ):
                sketchbook[
                    i, j
                ] = 255  # If all of the surrounding pixels are white, then the pixel is white ( = 1)
            else:
                sketchbook[
                    i, j
                ] = 0  # If at least one pixel is black, the targeted pixel would be black

    return sketchbook


erosion_mask = np.array([[0, 255, 0], [255, 255, 255], [0, 255, 0]], dtype=np.uint8)

img = cv.imread(
    "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/Fingerprint-Samples-for-Each-User.png",
    cv.IMREAD_GRAYSCALE,
)

binary_img_adaptive = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2
)  # Convert to binrary image

if img is None:  # When the path of image is invalid
    raise Exception("Image not found")

while cv.waitKey(0) != ord("q"):  # Windows are displayed until q key is pressed
    cv.imshow("Original", img)  # Show the original image
    cv.imshow(
        "Binary", binary_img_adaptive
    )  # Show the binary image, constists of only black and white pixels.
    cv.imshow(
        "Carved", carve(binary_img_adaptive)
    )  # Application of the for loop erosion
    cv.imshow(
        "cv library erode", cv.erode(binary_img_adaptive, erosion_mask)
    )  # Open CV library erosion

print(
    f"Same? \n{binary_img_adaptive == carve(binary_img_adaptive)}"
)  # Compare the grayscale value of pixels of custom erosion and library erosion.
cv.destroyAllWindows()
exit(0)
