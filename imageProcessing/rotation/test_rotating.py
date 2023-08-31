import rotation as rot
import cv2 as cv
import numpy as np

img_path1 = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg"  # Path to the first image
img_path2 = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/bridge.jpg"  # Path to the second image

img_sample = cv.imread(img_path1)  # Get a first sample: Paris
img_sample2 = cv.imread(
    img_path2, cv.IMREAD_GRAYSCALE
)  # Get a second sample: Bridge in London

angle_for_comparison = 30  # Angle to rotate the image

if img_sample is None:
    print("Could not read the image")
    exit(0)

while cv.waitKey(20) != ord("q"):
    # Custom Rotation
    cv.imshow(
        f"Custom: Rotated {angle_for_comparison} degrees", rot.rotate(img_sample, 30)
    )  # Rotate the image for degrees set

    # # OpenCV Rotation
    # # Define the rotation matrix ((column_center, row_center), rotating angle, scale)
    # rotation_matrix_cv = cv.getRotationMatrix2D(
    #     (img_sample.shape[1] // 2, img_sample.shape[0] // 2), angle_for_comparison, 1.0
    # )

    # # Apply a rotation matrix to the image, and set the scale of image to show on window
    # rotated_cv = cv.warpAffine(img_sample, rotation_matrix_cv, img_sample.shape[::-1])

    # cv.imshow(f"OpenCV: Rotated {angle_for_comparison} degrees", rotated_cv)  # Rotate the image for degrees set


cv.destroyAllWindows()
exit(0)
