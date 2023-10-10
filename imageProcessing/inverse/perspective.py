import numpy as np
import cv2 as cv


def warp_perspective(source_image, src_points, dst_points):
    """
    Apply a perspective transformation to an image using inverse warping.

    :param source_image: Source image, a NumPy array of shape (rows, columns, depth)
    :param source_points: Coordinates of 4 points in the source image
    :param destination_points: Coordinates of 4 points in the destination image
    :return: Transformed image
    """
    # Get the dimensions of the source image
    rows, columns, depth = source_image.shape

    # Create an empty array for the destination image
    destination_image = np.zeros_like(source_image)

    # Compute the perspective transformation matrix
    matrix_for_transformation = cv.getPerspectiveTransform(np.float32(dst_points), np.float32(src_points))

    # Compute the inverse perspective transformation matrix
    matrix_for_inversion = np.linalg.inv(matrix_for_transformation)

    # Iterate over each pixel in the destination image
    for y in range(rows):
        for x in range(columns):
            # Compute the corresponding location in the source image
            x_source, y_source, dot_result = np.dot(matrix_for_inversion, [x, y, 1])
            x_source = int(x_source / dot_result)
            y_source = int(y_source / dot_result)

            # Check if the computed location is within the bounds of the source image
            if 0 <= x_source < columns and 0 <= y_source < rows:
                # Assign the value from the source image to the destination image
                destination_image[y, x, :] = source_image[y_source, x_source, :]

    return destination_image


# Example usage
if __name__ == "__main__":
    # Read the source image
    path = "C:\\Users\\1\lab\opencv-training\imageProcessing\source\clock.png"
    source_image = cv.imread(path)
    rows, columns, depth = source_image.shape

    # Define the source and destination points
    source_points = [(0, 0), (columns - 1, 0), (columns - 1, rows - 1), (0, rows - 1)]
    destination_points = [(75, 118), (columns - 127, 30), (columns - 20, rows - 50), (29, rows - 80)]

    # Apply the perspective transformation
    destination_image = warp_perspective(source_image, source_points, destination_points)

    while cv.waitKey(1) != ord('q'):
        cv.imshow('Source Image', source_image)
        cv.imshow('Transformed Image', destination_image)  # Show the result

    cv.waitKey(0)
    cv.destroyAllWindows()
    exit(0)
