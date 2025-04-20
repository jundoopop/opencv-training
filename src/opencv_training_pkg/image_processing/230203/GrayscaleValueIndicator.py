import numpy as np
import cv2 as cv

ville_gray = cv.imread('../source/paris.jpg', cv.IMREAD_GRAYSCALE)
window_title = "Ville, Greyscale"
BGR_text = "for test"


def gray_value(event, x, y, flags, param):
    greyscale_value = img[y, x, 0]
    if event == cv.EVENT_LBUTTONDOWN:
        text_to_display = f"{greyscale_value}"
        cv.putText(img, text_to_display, (x, y), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
        print(text_to_display)


cv.namedWindow(window_title)
cv.setMouseCallback(window_title, gray_value)

img = cv.cvtColor(ville_gray, cv.COLOR_GRAY2BGR)
while cv.waitKey(10) != ord('q'):
    cv.imshow(window_title, img)

cv.destroyAllWindows()
exit(0)
