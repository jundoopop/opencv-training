import differGaussian
import cv2 as cv

# set values
firstKsize = (3, 3)
secondKsize = (9, 9)

# get image file
directory = '/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg'
window_name_1 = "DoG Filter Applied"
window_name_2 = "DoG Filter Applied by openCV library"

sample = cv.imread(directory, cv.IMREAD_GRAYSCALE)

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    # manual_result -> applied Gaussian Formula
    # default_result -> applied OpenCV library
    manual_result = differGaussian.convolution(directory)
    default_result = cv.GaussianBlur(sample, firstKsize, 0) - cv.GaussianBlur(sample, secondKsize, 0)

    # show both to compare with
    cv.imshow(window_name_1, manual_result)
    cv.imshow(window_name_2, default_result)

cv.destroyAllWindows()
exit(0)
