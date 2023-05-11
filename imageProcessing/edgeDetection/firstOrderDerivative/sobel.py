import cv2 as cv
import numpy as np

color = cv.IMREAD_GRAYSCALE


def convolution(address):
    image = cv.imread(address, cv.IMREAD_GRAYSCALE)
    # 2 x 2 filters of x and y direction
    gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)

    x_gradient = cv.filter2D(image, -1, gx)
    y_gradient = cv.filter2D(image, -1, gy)

    # operates magnitude
    sobel_applied = np.sqrt(pow(x_gradient, 2) + pow(y_gradient, 2))
    return sobel_applied


def sobel_filter(image_file):
    """
    Performs Sobel edge detection on an image.

    Args:
      image: The input image.
      kernel_size: The size of the Sobel kernel.
      scale: The scale factor for the Sobel kernel.
      delta: The delta value for the Sobel kernel.

    Returns:
      The output image.
    """

    # Convert the image to grayscale.
    grayscale_image = cv.imread(image_file, cv.IMREAD_GRAYSCALE).astype(np.float32)

    # Create the Sobel kernel.
    sobel_x_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y_kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Apply the Sobel kernel to the image.
    sobel_x = cv.filter2D(grayscale_image, -1, sobel_x_kernel)
    sobel_y = cv.filter2D(grayscale_image, -1, sobel_y_kernel)

    # Normalize the gradient magnitude to the range [0, 255].
    gradient_magnitude = np.uint8(255 * gradient_magnitude / gradient_magnitude.max())

    # Calculate the result of the Sobel filter.
    result = cv.convertScaleAbs(
        np.sqrt(np.square(sobel_x) + np.square(sobel_y)), 1.0, 255
    )

    # Return the output image.
    return result
