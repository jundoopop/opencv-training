import cv2 as cv
import numpy as np

# copied from OpenCV document
# https://docs.opencv.org/4.x/d2/d2c/tutorial_sobel_derivatives.html

# get image file
directory = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/bridge.jpg"
directory_quebecFlag = (
    "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/Flag_of_Quebec.png"
)
directory_bingLogo = (
    "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/binglogo.jpg"
)
window_name = "Sobel Filter Applied"
color = cv.IMREAD_GRAYSCALE


def sobel_addWeighted(target):
    temp = cv.GaussianBlur(target, (3, 3), 0)
    sobel_x = cv.Sobel(
        temp, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
    )
    sobel_y = cv.Sobel(
        temp, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
    )

    abs_sobel_x = cv.convertScaleAbs(sobel_x)
    abs_sobel_y = cv.convertScaleAbs(sobel_y)

    result = cv.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
    result2 = (abs_sobel_x * 0.5+ abs_sobel_y * 0.5).astype(np.uint8)

    return result


def sobel_sqrt(target):
    temp = cv.GaussianBlur(target, (3, 3), 0)
    sobel_x = cv.Sobel(
        temp, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
    )
    sobel_y = cv.Sobel(
        temp, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
    )

    abs_sobel_x = cv.convertScaleAbs(sobel_x)
    abs_sobel_y = cv.convertScaleAbs(sobel_y)
    result = cv.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
    # result2 : calculated by np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    result2 = np.sqrt(
        np.square(abs_sobel_x.astype(np.uint16))
        + np.square(abs_sobel_y).astype(np.uint16)
    ).astype(np.uint8)

    return result2


target = cv.imread(directory, color)
target2 = cv.imread(directory_quebecFlag, color)
target3 = cv.imread(directory_bingLogo, color)

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    # modify the target when needed
    cv.imshow("original", target)
    cv.imshow("sobel_addWeighted", sobel_addWeighted(target))
    cv.imshow("sobel_sqrt", sobel_sqrt(target))
cv.destroyAllWindows()
exit(0)
