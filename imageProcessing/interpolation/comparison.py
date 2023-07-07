import cv2 as cv
import numpy as np
import interLinear as il

img = cv.imread("../source/resize1.jpg", cv.IMREAD_GRAYSCALE)
if img is None:
    print("Can't read the image")
    exit(0)

ratio = 2  # Resize ratio
dsize = (int(len(img[0]) * ratio), int(len(img) * ratio))  # dsize[0] = width, dsize[1] = height

# sketchbook = np.ndarray(shape=dsize, dtype=np.float32)  # Create a new array for custom interpolation

# row: len(img), col: len(img[0])
# for i in range(len(img)):
#     for j in range(len(img[0])):
#         sketchbook[i, j] = il.bi_inter(i // 2, j // 2, img)  # Apply custom interpolation to the image
sketchbook_weighted = np.array(
    [[il.weighted_mean(i // ratio, j // ratio, img) for i in range(dsize[0])] for j in range(dsize[1])])
sketchbook_convoluted = np.array(
    [[il.bilinear_kernel(i // ratio, j // ratio, img) for i in range(dsize[0])] for j in range(dsize[1])])
while cv.waitKey(0) != ord("q"):
    cv.imshow("Original", img)
    # CV library bilinear interpolation
    cv.imshow("CV library bilinear interpolation",
              cv.resize(img, dsize, fx=0, fy=0, interpolation=cv.INTER_LINEAR))

    # cv.imshow("CV library nearest neighbor interpolation",
    #           cv.resize(img, dsize, fx=0, fy=0, interpolation=cv.INTER_NEAREST))

    # Custom bilinear interpolation formula -> Weighted mean
    cv.imshow("Custom bilinear interpolation - weighted mean",
              sketchbook_weighted.astype(np.uint8))
    # Custom bilinear interpolation formula -> 3 x 3 kernel
    cv.imshow("Custom bilinear interpolation - convolution",
              sketchbook_convoluted.astype(np.uint8))

cv.destroyAllWindows()
exit(0)
