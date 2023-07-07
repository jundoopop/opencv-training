import numpy as np
import cv2 as cv
import interCubic as ic

path = "../source/resize1.jpg"
color = cv.IMREAD_GRAYSCALE  # Read the image as grayscale
img = cv.imread(cv.samples.findFile(path), color)  # Read the image

if img is None:  # If the path of source is wrong
    print("Can't read the image")
    exit(0)

ratio = 2  # Resize ratio
dsize = size = (int(len(img[0]) * ratio), int(len(img) * ratio))  # dsize[0] = width, dsize[1] = height

sketchbook_cubic_convolution = np.array(
    [[ic.bicubic_kernel(i // ratio, j // ratio, img) for i in range(dsize[0])] for j in range(dsize[1])])

while cv.waitKey(0) != ord("q"):
    cv.imshow("Cubic Convolution Test - Custom", sketchbook_cubic_convolution.astype(np.uint8))

cv.destroyAllWindows()
exit(0)
