import cv2
import numpy as np
import imageProcessing.morphology.eroding_custom as custom

img = cv2.imread(
    "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/Fingerprint-Samples-for-Each-User.png",
    cv2.IMREAD_GRAYSCALE,
)

if img is None:
    raise Exception("Image not found")

erosion_mask = np.array([[0, 255, 0], [255, 255, 255], [0, 255, 0]], dtype=np.uint8)

binary_img_simple = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
binary_img_adaptive = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
binary_img_eroded_adaptive = cv2.erode(binary_img_adaptive, erosion_mask)
binary_img_opening_operation = cv2.dilate(
    cv2.erode(binary_img_adaptive, erosion_mask), erosion_mask
)
binary_img_close_operation = cv2.erode(
    cv2.dilate(binary_img_adaptive, erosion_mask), erosion_mask
)

binary_img_eroded_simple = cv2.erode(binary_img_simple, erosion_mask)
binary_img_morph_close = cv2.morphologyEx(
    binary_img_simple, cv2.MORPH_CLOSE, erosion_mask, iterations=3
)

print(f"{binary_img_eroded_adaptive == custom.carve(binary_img_adaptive)}")
while cv2.waitKey(0) != ord("q"):
    cv2.imshow("Default Image", img)
    cv2.imshow("cv2.adaptiveThreshold() Applied", binary_img_adaptive)
    cv2.imshow("Simple Binary Image", binary_img_simple)
    cv2.imshow("Eroded Binary Image - Adaptive Threshold", binary_img_eroded_adaptive)
    cv2.imshow("Custom Erode", custom.carve(binary_img_adaptive))

cv2.destroyAllWindows()
exit(0)
