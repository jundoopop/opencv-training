import numpy as np
import cv2 as cv

# Read image
IMG_PATH = "/home/treeplanter/graphics/pyOpenCv/\
imageProcessing/source/concreteblock.jpg"

# Load an image to draw lines on
target = cv.imread(IMG_PATH)

# Get the edges of the image
target_edge = cv.Canny(cv.cvtColor(target, cv.COLOR_BGR2GRAY), 50, 200)

# Declare parameter space.
# formula: rho = x * cos(theta) + y * sin(theta)
theta_range = np.deg2rad(np.arange(0, 180, 20))
max_rho = np.hypot(len(target), len(target[0]))
rho_range = np.arange(-max_rho, max_rho, 1)

# Delcare accumulator array to contain the votes
accumulate_array = [[[] for j in range(len(rho_range))] 
                    for i in range(len(theta_range))]
accumulator_theshold = 100

# Loop through the parameter space
for rho_idx, rho in enumerate(rho_range):
    for theta_idx, theta in enumerate(theta_range):
        # Loop through the image
        for x in range(len(target_edge[0])):
            for y in range(len(target_edge)):
                # If the pixel is an edge
                if target_edge[y, x] == 255:
                    # Get the rho value
                    rho_value = x * np.cos(theta) + y * np.sin(theta)
                    # If rho_value is within the tolerance
                    if rho - 0.5 <= rho_value <= rho + 0.5:
                        # Increment the accumulator array
                        accumulate_array[theta_idx][rho_idx].append([x, y])


for rho_idx in range(len(rho_range)):
    for theta_idx in range(len(theta_range)):
        # If the accumulator array has enough votes
        if len(accumulate_array[theta_idx][rho_idx]) >= accumulator_theshold:
            # Draw the line
            cv.line(
                target,
                accumulate_array[theta_idx][rho_idx][0],  # first point
                accumulate_array[theta_idx][rho_idx][-1],  # last point
                (0, 0, 255),
                2,
            )


while cv.waitKey(20) != ord("q"):
    cv.imshow("Hough Applied", target)

cv.destroyAllWindows()
exit(0)
