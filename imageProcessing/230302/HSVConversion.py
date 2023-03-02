import cv2

img_file = "../source/paris.jpg"

image = cv2.imread(img_file)

row = len(image)
col = len(image[0])

for i in range(row):
    for j in range(col):
        red = image[i][j][2]
        green = image[i][j][1]
        blue = image[i][j][0]

        greyscale = red * 0.299 + green * 0.587 + blue * 0.114
        image[i][j] = [greyscale]

while cv2.waitKey(0) != ord("q"):
    cv2.imshow("grayscale - by loop", image)

cv2.destroyAllWindows()
