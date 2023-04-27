import cv2 as cv

# get image file
directory = '/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg'
window_name = "Sobel Filter Applied (Default Method)"
color = cv.IMREAD_GRAYSCALE

target = cv.imread(directory, color)

# if Q key pressed, all windows would be closed and the program exited
while cv.waitKey(0) != ord("q"):
    result = cv.Sobel(target, cv.CV_8U, 1, 1)
    cv.imshow(window_name, result)

cv.destroyAllWindows()
exit(0)
