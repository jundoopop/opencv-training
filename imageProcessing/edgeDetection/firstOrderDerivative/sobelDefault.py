import cv2 as cv

# copied from OpenCV document
# https://docs.opencv.org/4.x/d2/d2c/tutorial_sobel_derivatives.html

# get image file
directory = '/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg'
window_name = "Sobel Filter Applied (Default Method)"
color = cv.IMREAD_GRAYSCALE

target = cv.imread(directory, color)

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    sobel_x = cv.Sobel(target, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    sobel_y = cv.Sobel(target, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

    abs_sobel_x = cv.convertScaleAbs(sobel_x)
    abs_sobel_y = cv.convertScaleAbs(sobel_y)

    result = cv.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

    cv.imshow(window_name, result)

cv.destroyAllWindows()
exit(0)
