import sobel
import cv2 as cv

# get image file
directory = '/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg'
window_name = "Sobel Filter Applied"

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    result = sobel.convolution(directory)
    cv.imshow(window_name, sobel.convolution(directory))

cv.destroyAllWindows()
exit(0)
