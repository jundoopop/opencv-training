import cv2 as cv
import numpy as np
import math


# Probabilistic Hough Line Transform
def stanHough(
    img_gray,
    img_color,
    rho,
    theta,
    canny_min_threshold,
    canny_max_threshold,
):
    """
    rho = 10
    theta = np.pi / 180
    threshold = 70
    min_line_length = 50
    max_line_gap = 30
    """

    edgeDetected = cv.Canny(img_gray, canny_min_threshold, canny_max_threshold)

    lines = cv.HoughLines(edgeDetected, rho, theta, 150, None, 0, np.pi)
    copied_image = np.copy(img_color)

    if lines is not None:
        # Gathered from https://docs.opencv.org/4.8.0/d9/db0/tutorial_hough_lines.html
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]

            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a * rho
            y0 = b * rho

            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))

            cv.line(copied_image, pt1, pt2, (0, 0, 255), 1, cv.LINE_AA)

    return copied_image


path_of_img_london_bridge = (
    r"C:\Users\1\lab\opencv-training\imageProcessing\source\bridge.jpg"
)
path_of_img_square_blocks = (  # path of image with square blocks for hough lines
    r"C:\Users\1\lab\opencv-training\imageProcessing\source\Exploring-squares-FB.jpg"
)

img_color = cv.imread(path_of_img_square_blocks)  # Read the colored image
img_gray = cv.cvtColor(
    img_color, cv.COLOR_BGR2GRAY
)  # Convert the colored image to gray scale for edge detection


if img_color is None:
    print("Could not open or find the image")

else:
    """
    Standard Hough Line Transform
    Probabilistic Hough Line Transform
    -> stanHough(
        img_gray, img_color, rho,
        theta, threshold, min_line_length,
        max_line_gap, canny_min_threshold, canny_max_threshold
        )
    """

    while ord("q") != cv.waitKey(0):  # probHough needs nine parameters
        cv.imshow("Original", img_color)
        cv.imshow("Canny Edge Detection", cv.Canny(img_gray, 50, 150))
        cv.imshow(
            f"Red Lines - Standard HLT (rho : {1})",
            stanHough(img_gray, img_color, 1, np.pi / 90, 50, 150),
        )
        cv.imshow(
            f"Red Lines - Standard HLT (rho : {1.5})",
            stanHough(img_gray, img_color, 1.5, np.pi / 90, 50, 150),
        )
        cv.imshow(
            f"Red Lines - Standard HLT (rho : {2})",
            stanHough(img_gray, img_color, 2, np.pi / 90, 50, 150),
        )
    cv.destroyAllWindows()


exit(0)
