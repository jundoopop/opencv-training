import numpy as np

import imageProcessing.blur.gaussian.GaussianGenerator as gaus
import computeLoG as comlog
import laplacian
import cv2 as cv

# set values
sigma = 1
ksize = 3
depth = -1

# get image file
directory = 'C:\\Users\\1\lab\opencv-training\imageProcessing\source\\testcase1.jpg'
window_name_custom_application = "LoG Filter Applied"
window_name_custom_formula = "LoG Formula Applied"
window_name_default_application = "LoG Filter Applied by cv2.Laplacian()"
window_name_blur_only = "Gaus Blurring Applied"

sample = cv.imread(directory, cv.IMREAD_GRAYSCALE)
gausMat = gaus.gaussianMask(ksize, sigma)
newSample = np.array(sample).astype(np.float16)
sketchbook = np.zeros((450, 800))

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    # onestop -> applied LoG Formula
    # manual_result -> applied Gaussian Formula
    # default_result -> applied OpenCV library
    # pre_LoG = np.array(sample).astype(np.uint16)
    # Print the elements of the kernel
    print(comlog.apply(sigma, ksize))
    pre_LoG = cv.filter2D(sample, depth, gausMat)
    onestop = cv.filter2D(sample, depth, comlog.apply(7, 1))

    print(f"laplacian custom kernel:\n{laplacian.kernel(3,1)}")
    custom_result = cv.filter2D(pre_LoG, depth, laplacian.kernel(3, 1))
    default_result = cv.Laplacian(cv.GaussianBlur(sample, (ksize, ksize), sigma), depth, ksize)

    # show both to compare with
    cv.imshow(window_name_custom_application, custom_result)
    cv.imshow(window_name_custom_formula, onestop)
    cv.imshow(window_name_default_application, default_result)
    cv.imshow(window_name_blur_only, pre_LoG)

cv.destroyAllWindows()
exit(0)
