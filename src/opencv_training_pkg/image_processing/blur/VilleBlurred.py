import cv2 as cv
import numpy as np
from pathlib import Path

# Load the image
source_directory = Path.cwd() / "imageProcessing" / "source"
# Show the directory if it is correct
print(f"Image resources directory: {source_directory}")

# Load the image
img = cv.imread(str(source_directory / "paris.jpg"))

if img is None:  # Check if the image is loaded
    raise Exception("Image not found")

# Declare an np array to show images in single window
stack_two_images = np.hstack((img, cv.blur(img, (9, 9))))

# Show two cases of blurring
cv.imshow("ville default vs blurring", stack_two_images)

while True:  # keep the window open until we press 'esc'
    key = cv.waitKey(0)
    if key == 27:  # 27 is the ASCII value of 'esc'
        break

cv.destroyAllWindows()
exit(0)
