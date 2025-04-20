"""
numpy for computing each pixels of the images
cv2 for reading and showing images
"""
import numpy as np
import cv2 as cv


def rotate_image(source_image, angle):
    """
    Rotate an image by a input angle value using inverse warping.

    :param source_image: Source image, a NumPy array of shape (H, W, C)
    :param angle: Angle of rotation in degrees
    :return: Rotated image
    """

    (
        rows,
        columns,
        demensions,
    ) = source_image.shape  # Get height and width of the matrix of the source image

    destination_image = np.zeros_like(
        source_image
    )  # Create an empty canvas for mapping

    # Center of rotation
    x_center = columns // 2
    y_center = rows // 2

    radian = np.deg2rad(angle)  # Get radian value of the angle
    matrix_for_rotation = np.array(
        [
            [
                np.cos(radian),
                -np.sin(radian),
                x_center - x_center * np.cos(radian) + y_center * np.sin(radian),
            ],
            [
                np.sin(radian),
                np.cos(radian),
                y_center - x_center * np.sin(radian) - y_center * np.cos(radian),
            ],
            [0, 0, 1],
        ]
    )  # Define the rotation matrix.
    # When mutliple the matrix with the coordinate of the destination image, the result is the coordinate of the source image.

    # Compute the inverse rotation matrix for inversed mapping
    matrix_for_inversion = np.linalg.inv(matrix_for_rotation)

    # Iterate each pixel in the destination image for mapping
    for y in range(rows):  # Count height
        for x in range(columns):  # Count width
            # Compute the corresponding location in the source image
            x_source, y_source, dot_result = np.dot(matrix_for_inversion, [x, y, 1])
            # Convert to integer to find the exact coordinates
            x_source = int(x_source / dot_result)
            y_source = int(y_source / dot_result)

            # Check if the computed location is within the bound indices of the source image
            if 0 <= x_source < columns and 0 <= y_source < rows:
                # Map the value from the source image to the destination image
                destination_image[y, x, :] = source_image[y_source, x_source, :]

    return destination_image  # Return the result


if __name__ == "__main__":  # Main function for Execution
    path = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg"  # Path of the source image

    targeted_image = cv.imread(path)  # Read the source image

    theta = 30  # Define the angle for rotation

    result_image = rotate_image(targeted_image, theta)  # Apply the function

    while cv.waitKey(1) != ord("q"):  # Wait for the key 'q' to be pressed
        cv.imshow(f"Rotated Image: degree {theta}", result_image)  # Show the result

    cv.destroyAllWindows()  # Close all windows when key 'q' is pressed
    exit(0)  # Exit the program
