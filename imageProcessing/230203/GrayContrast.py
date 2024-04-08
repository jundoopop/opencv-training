import numpy as np
import cv2 as cv
from pathlib import Path

# Load the image
source_directory = Path.cwd() / "imageProcessing" / "source"
print(f"Image resources directory: {source_directory}")

# Load the image
img = cv.imread(str(source_directory / "paris.jpg"), cv.IMREAD_GRAYSCALE)

# Generate a zero image with the same shape and type as the original image
zero_image = np.zeros(img.shape, img.dtype)

# Increase and decrease the contrast of the image
dst_contrast_down = cv.scaleAdd(img, 0.6, zero_image)
dst_contrast_up = cv.scaleAdd(img, 1.5, zero_image)

# Show the images by stacking 3 images in single window
stack_three_images = np.hstack((img, dst_contrast_down, dst_contrast_up))

cv.imshow("Grey, Contrast Reduced vs Contrast Boosted", stack_three_images)

while True:  # keep the window open until we press 'esc'
    key = cv.waitKey(0)
    if key == 27:  # 27 is the ASCII value of 'esc'
        break

cv.destroyAllWindows()
exit(0)
