import numpy as np
import cv2 as cv


fp = "test.png"
color = cv.IMREAD_GRAYSCALE
src = np.array(cv.imread(fp, color), dtype=np.float32)
shape = src.shape

gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

x_convoluted = cv.filter2D(src, -1, gx)
y_convoluted = cv.filter2D(src, -1, gy)


abs_x_convoluted = np.clip(np.absolute(x_convoluted), 0, 255).astype(np.uint8)
abs_y_convoluted = np.clip(np.absolute(y_convoluted), 0, 255).astype(np.uint8)

# roberts_applied = abs_x_convoluted * 0.5 + abs_y_convoluted * 0.5 오차가 있음
roberts_applied = cv.addWeighted(abs_x_convoluted, 0.5, abs_y_convoluted, 0.5, 0)

sobel_x = cv.Sobel(
    src, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
)
sobel_y = cv.Sobel(
    src, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT
)

assert (x_convoluted == sobel_x).sum() == np.prod(shape)
assert (y_convoluted == sobel_y).sum() == np.prod(shape)

# abs_x_convoluted == abs_sobel_x
abs_sobel_x = cv.convertScaleAbs(sobel_x)
abs_sobel_y = cv.convertScaleAbs(sobel_y)

assert (abs_x_convoluted == abs_sobel_x).sum() == np.prod(shape)
assert (abs_y_convoluted == abs_sobel_y).sum() == np.prod(shape)


result = cv.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

assert (result == roberts_applied).sum() == np.prod(shape)

concat_result = np.concatenate((result, roberts_applied), axis=1)

cv.imwrite("result.png", concat_result)
