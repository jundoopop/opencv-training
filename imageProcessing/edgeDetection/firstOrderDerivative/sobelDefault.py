import cv2 as cv
import numpy as np

# copied from OpenCV document
# https://docs.opencv.org/4.x/d2/d2c/tutorial_sobel_derivatives.html

# get image file
directory = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/bridge.jpg"
window_name = "Sobel Filter Applied"
color = cv.IMREAD_GRAYSCALE

target = cv.imread(directory, color)

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    temp = cv.GaussianBlur(target, (3, 3), 0)
    sobel_x = cv.Sobel(
        temp, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
    )
    sobel_y = cv.Sobel(
        temp, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
    )

    abs_sobel_x = cv.convertScaleAbs(sobel_x)
    abs_sobel_y = cv.convertScaleAbs(sobel_y)

    # result1 : calculated by cv.addWeighted()
    # result2 : calculated by np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    result1 = cv.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
    result2 = np.sqrt(
        np.square(abs_sobel_x.astype(np.uint16))
        + np.square(abs_sobel_y).astype(np.uint16)
    ).astype(np.uint8)

    cv.imshow(f"{window_name} - Refered in cv Document", result1)
    cv.imshow(f"{window_name} - Implemented a Formula", result2)

cv.destroyAllWindows()
exit(0)
