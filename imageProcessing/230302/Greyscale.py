import cv2 as cv

img_file = "../source/paris.jpg"

# image to apply custom function
image = cv.imread(img_file)

# the default example
img_cv_grey = cv.imread(img_file, cv.IMREAD_GRAYSCALE)

# yield the length of row and column of image file
row = len(image)
col = len(image[0])

# iterate to switch colors to gray pixels
for i in range(row):
    for j in range(col):
        # opencv color values are placed in the sequence of B, G, R
        red = image[i][j][2]
        green = image[i][j][1]
        blue = image[i][j][0]

        # calculate gray value with the formula, using RGB values
        greyscale = red * 0.299 + green * 0.587 + blue * 0.114
        image[i][j] = [greyscale]

# remain windows until 'q' keyboard pressed
while cv.waitKey(0) != ord("q"):
    cv.imshow("grayscale - by loop", image)
    cv.imshow("grayscale - opencv", img_cv_grey)

# when q key pressed, all windows are closed
# and exit process with 0
cv.destroyAllWindows()
exit(0)
