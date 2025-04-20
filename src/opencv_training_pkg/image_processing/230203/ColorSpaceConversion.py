import cv2 as cv
import numpy as np
from pathlib import Path


source_directory = Path.cwd() / "imageProcessing" / "source"
print(f"Image resources directory: {source_directory}")

img = cv.imread(str(source_directory / "paris.jpg"))
img_gray = cv.imread(str(source_directory / "paris.jpg"), cv.IMREAD_GRAYSCALE)

white = np.array([255, 255, 255], np.uint8)
img_CMY = white - img

cv.imshow("ville RGB", img)
cv.imshow("ville HSV", cv.cvtColor(img, cv.COLOR_BGR2HSV))
cv.imshow("ville CMY", img_CMY)


while True:  # keep the window open until we press 'esc'
    key = cv.waitKey(0)
    if key == 27:  # 27 is the ASCII value of 'esc'
        break

cv.destroyAllWindows()
exit(0)
