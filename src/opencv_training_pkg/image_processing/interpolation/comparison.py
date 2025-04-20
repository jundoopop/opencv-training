import cv2 as cv
import numpy as np
import interLinear as il
import interCubic as ic

img = cv.imread(
    "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/resize1.jpg",
    cv.IMREAD_GRAYSCALE,
)
if img is None:
    print("Can't read the image")
    exit(0)

ratio = 0.5  # Resize ratio
dsize = (
    int(len(img) * ratio),
    int(len(img[0]) * ratio),
) 

sketchbook_weighted = np.zeros(
    shape=dsize, dtype=np.float32
)  # Create a new array for custom interpolation

for i in range(0, len(img), 2):
    for j in range(0, len(img[0]), 2):
        # print(f"Curent coordinate: ({i}, {j})")
        # print(
        #     f"Shape of the imaging bound: {np.shape(sketchbook_weighted[2 * i : 2 * i + int(ratio * 2), 2 * j : 2 * j + int(ratio * 2)])}"
        # )
        # print(
        #     f"Shape of the interpolated range:\n{il.weighted_mean(img[i, j], img[i, j + 1], img[i + 1, j], img[i + 1, j + 1], ratio)}"
        # )
        sketchbook_weighted[
            int(ratio * i) : int(ratio * i) + int(ratio * 2), int(ratio * j) : int(ratio * j) + int(ratio * 2)
        ] = il.weighted_mean(
            img[i, j], img[i, j + 1], img[i + 1, j], img[i + 1, j + 1], ratio
        )
# Get the result of custom interpolation

while cv.waitKey(0) != ord("q"):
    cv.imshow("Original", img)
    # CV library bilinear interpolation

    cv.imshow(
        "Custom bilinear interpolation - Downsample 0.5x",
        sketchbook_weighted.astype(np.uint8),
    )


cv.destroyAllWindows()
exit(0)
