import numpy as np
import cv2 as cv

img = cv.imread(cv.samples.findFile('paris.jpg'))
# Create a black image
# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

cv.imshow('beautiful.jpeg');
k = cv.waitKey(0)
