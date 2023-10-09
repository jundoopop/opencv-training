"""
Hough Transform Implementation

Reference: https://dl.acm.org/doi/10.1145/361237.361242

Packages:
- numpy: for matrix operations
- cv2: for image processing. 
    Used for reading, writing and showing images and drawing lines.
"""
import numpy as np
import cv2 as cv

# Read image

# Declare parameter space.


def parameter_space(x, y, rho, theta):
    # Calculate rho and theta values for each point in the image.
    rho = x * np.cos(theta) + y * np.sin(theta)
    theta = np.deg2rad(np.arange(-90, 90, 1))

    return [rho, theta]


def hough_transform(image, rho_res=1):
    """
    Perform the Hough Line Transform.
    It returns the accumulator array, thetas, and rhos.
    """
    # Step 1: Edge detection
    # Use Canny edge detection to get the edge points in the image.
    edges = cv.Canny(image, 50, 200)

    # Calculate the diagonal length of the image,
    # which will be the maximum possible rho value.
    # row = len(image), column = len(image[0])
    max_rho = np.hypot(len(image), len(image[0]))

    # Create an array of possible rho values.
    rhos = np.arange(-max_rho, max_rho, rho_res)

    # Create an array of possible theta values in radians.
    thetas = np.linspace(0, np.pi, 180)

    # Step 2: Initialize the accumulator
    # The accumulator is a 2D array.
    # The rows represent rho values and columns represent theta values.
    accumulator = np.zeros((len(rhos), len(thetas)), dtype=np.uint16)

    # Step 3: Populate the accumulator
    # For each edge point, calculate the possible (rho, theta) pair
    # and increment their value in the accumulator.
    # Returns the indices of the detected pixels as edges.
    edge_points = np.argwhere(edges)
    for coordinate in edge_points:
        y, x = coordinate
        for theta_index, theta in enumerate(thetas):
            rho = x * np.cos(theta) + y * np.sin(theta)  # Hough Space
            rho_index = np.argmin(np.abs(rhos - rho))
            accumulator[rho_index, theta_index] += 1

    return accumulator, thetas, rhos


path = "/home/treeplanter/graphics/pyOpenCv/\
imageProcessing/source/blocks.png"  # Path to the image.
target = cv.imread(path)  # Load a grayscale of the image.
if target is None:  # Check if the image was loaded.
    print("Could not read the image")
    exit(0)
target_gray = cv.cvtColor(target, cv.COLOR_BGR2GRAY)  # Convert to grayscale.

# Get the accumulator and possible theta and rho values.
accumulator, thetas, rhos = hough_transform(target_gray)

# Step 4: Find peaks in the accumulator
# A peak in the accumulator represents a potential line in the image.
# For simplicity, we're thresholding the accumulator to detect these peaks.
hough_threshold = 120
accumulator_peaks = np.where(accumulator > hough_threshold)

cnt = 0
# For each detected peak, draw the corresponding line on the image.
for rho_index, theta_index in zip(*accumulator_peaks):  # type: ignore
    rho = rhos[rho_index]
    theta = thetas[theta_index]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 300 * (-b))
    y1 = int(y0 + 300 * (a))
    x2 = int(x0 - 300 * (-b))
    y2 = int(y0 - 300 * (a))
    if cnt < 50:
        print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")
        cnt += 1
    cv.line(target, (x1, y1), (x2, y2), (128, 128, 128), 2)

# Display the resulting image with detected lines.
while cv.waitKey(10) != ord("q"):
    cv.imshow("Hough Transform", target)
cv.destroyAllWindows()
exit(0)
