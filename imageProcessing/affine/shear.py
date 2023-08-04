import numpy as np


def shear(image, shear_x, shear_y):
    # Get the shape of the image
    rows, cols = image.shape

    # Define the affine transformation matrix
    matrix_to_shear = np.array(
        [[1.0, shear_x], [shear_y, 1.0]], dtype=np.float32
    )

    # Create a new image (all black) to store the sheared result
    result = np.zeros_like(image, dtype=np.uint8)

    # Apply the shearing transformation
    for y in range(rows):
        for x in range(cols):
            # Calculate the sheared coordinates using the affine transformation matrix
            x_result, y_result = np.matmul(
                matrix_to_shear, np.array([x, y]).T
            ).astype(np.int32)

            # Check if the sheared coordinates are within the new image bounds
            if 0 <= x_result < cols and 0 <= y_result < rows:
                # Assign the original pixel to the sheared position
                result[y_result, x_result] = image[y, x]

    return result


def shear2(image, shear_x, shear_y):
    # Get the shape of the image
    rows, cols = image.shape

    # Define the affine transformation matrix
    matrix_to_shear = np.array(
        [[1.0, shear_x, 0.0], [shear_y, 1.0, 0.0]], dtype=np.float32
    )

    # Create a new image (all black) to store the sheared result
    result = np.zeros_like(image, dtype=np.uint8)

    # Apply the shearing transformation
    for y in range(rows):
        for x in range(cols):
            # Calculate the sheared coordinates using the affine transformation matrix
            x_result = int(
                matrix_to_shear[0, 0] * x
                + matrix_to_shear[0, 1] * y
                + matrix_to_shear[0, 2]
            )
            y_result = int(
                matrix_to_shear[1, 0] * x
                + matrix_to_shear[1, 1] * y
                + matrix_to_shear[1, 2]
            )

            # Check if the sheared coordinates are within the new image bounds
            if 0 <= x_result < cols and 0 <= y_result < rows:
                # Assign the original pixel to the sheared position
                result[y_result, x_result] = image[y, x]

    return result
