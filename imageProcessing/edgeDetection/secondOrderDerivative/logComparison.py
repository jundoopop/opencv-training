import imageProcessing.blur.gaussian.GaussianGenerator as gaus
import laplacian
import cv2 as cv

# set values
sigma = 1
ksize = 3
depth = -1

# get image file
directory = '/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg'
window_name_1 = "LoG Filter Applied"
window_name_2 = "LoG Filter Applied by cv2.Laplacian()"

sample = cv.imread(directory, cv.IMREAD_GRAYSCALE)
gausMat = gaus.gaussianMask(ksize, sigma)

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    # manual_result -> applied Gaussian Formula
    # default_result -> applied OpenCV library
    pre_LoG = cv.filter2D(sample, depth, gausMat)
    LoGFilter = laplacian.kernel(ksize, sigma)
    manual_result = cv.filter2D(pre_LoG, depth, LoGFilter)
    default_result = cv.Laplacian(cv.GaussianBlur(sample, (1, 1), sigma), depth, ksize)

    # show both to compare with
    cv.imshow(window_name_1, manual_result)
    cv.imshow(window_name_2, default_result)

cv.destroyAllWindows()
exit(0)
