import cv2 as cv
from matplotlib.pyplot import gray
import numpy as np
from pathlib import Path


# Preprocess the images
def preprocessImg(no):
    relative_path = (
        Path.cwd() / "imageProcessing" / "detection" / "images" / "face" / f"{no}.jpg"
    )
    print(f"Current directory: {str(relative_path)}")
    img = cv.imread(str(relative_path), cv.IMREAD_COLOR)
    if img is None:
        return None, None
    # grayscale and equalize the histogram
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    return img, gray  # Return the original and the grayscale image


face_cascade = cv.CascadeClassifier(
    "C:\\Users\\jundo\\lab\\opencv-training\\imageProcessing\\detection\\haarcascade_frontalface_default.xml"
)
eye_cascade = cv.CascadeClassifier(
    "C:\\Users\\jundo\\lab\\opencv-training\\imageProcessing\\detection\\haarcascade_eye.xml"
)

colourImage, grayImage = preprocessImg(2)
if colourImage is None:
    print("Image not found : color")
    exit(0)

if grayImage is None:
    print("Image not found : gray")
    exit(0)

# Detect the faces
faces = face_cascade.detectMultiScale(grayImage, 1.1, 3, 0, (0, 80))

if faces.any():
    x, y, w, h = faces[0]
    face_image = colourImage[y : y + h, x : x + w]

    eyes = eye_cascade.detectMultiScale(face_image, 1.2, 3, 0, (0, 25))
    if len(eyes) == 2:
        for ex, ey, ew, eh in eyes:
            center = (x + ex + ew // 2, y + ey + eh // 2)
            cv.circle(colourImage, center, 5, (0, 255, 255), 2)
    else:
        print("Eyes are not detected")

    cv.rectangle(colourImage, faces[0], (0, 0, 255), 2)
    cv.imshow("Face", colourImage)

else:
    print("Face not detected")
cv.waitKey(0)
