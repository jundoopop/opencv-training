import cv2 as cv
import numpy as np


# Probabilistic Hough Line Transform
def probHough(
    img_gray,
    img_color,
    rho,
    theta,
    threshold,
    min_line_length,
    max_line_gap,
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
    lines = cv.HoughLinesP(
        edgeDetected, rho, theta, threshold, np.array([]), min_line_length, max_line_gap
    )
    copied_image = np.copy(img_color)

    # Iterate over the output "lines" and draw lines on the image copy
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(copied_image, (x1, y1), (x2, y2), (255, 0, 0), 2)

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
    -> probHough(
        img_gray, img_color, rho,
        theta, threshold, min_line_length,
        max_line_gap, canny_min_threshold, canny_max_threshold
        )
    """

    while ord("q") != cv.waitKey(0):  # probHough needs nine parameters
        cv.imshow("Original", img_color)
        cv.imshow(
            f"Blue Lines - Standard HLT (rho : {10})",
            probHough(img_gray, img_color, 10, np.pi / 60, 100, 50, 5, 50, 100),
        )
        cv.imshow(
            f"Blue Lines - Standard HLT (rho : {5})",
            probHough(img_gray, img_color, 5, np.pi / 60, 120, 50, 3, 50, 100),
        )
        cv.imshow(
            f"Blue Lines - Standard HLT (rho : {1})",
            probHough(img_gray, img_color, 1, np.pi / 60, 50, 50, 1, 50, 100),
        )
    cv.destroyAllWindows()


exit(0)
