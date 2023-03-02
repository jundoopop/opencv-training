import cv2 as cv
import numpy as np

# cv.VideoCapture.open('source/yosemite.mp4')
sample_video = cv.VideoCapture('source/piano.mp4')

while sample_video.isOpened():
    window_title = 'nature'
    cv.namedWindow(window_title)

    ret, frame = sample_video.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # if cv.waitKey(30) >= 0: break
    #
    # exposure = sample_video.get(cv.CAP_PROP_EXPOSURE)

    cv.imshow(window_title, sample_video)
    if cv.waitKey(100) == ord('q'):
        break

sample_video.release()
