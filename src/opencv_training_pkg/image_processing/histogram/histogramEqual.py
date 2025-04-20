import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_original = cv.imread("karina_zzang.png")
img_gray = cv.cvtColor(img_original, cv.COLOR_BGR2GRAY)

# histogram equalization

gray_hist = cv.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(gray_hist)
plt.show()
