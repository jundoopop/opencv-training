import cv2 as cv

img = cv.imread("../source/paris.jpg")


print(img[0][:5])

while cv.waitKey(0) != ord("q"):
    cv.imshow("ville default", img)
    cv.imshow("ville blurring", cv.blur(img, (9, 9)))

cv.destroyAllWindows()
exit(0)

