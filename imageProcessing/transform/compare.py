import cv2 as cv
import translation as tr
from pathlib import Path

path = "/home/treeplanter/graphics/pyOpenCv/imageProcessing/source/paris.jpg" # Path to the image
sample1 = cv.imread(path, cv.IMREAD_GRAYSCALE) # Get a first sample: Paris


while cv.waitKey(20) != ord("q"): # Wait for the user to press the "q" key
    cv.imshow("Translated - x: 0, y: 50", tr.move(sample1, 50, 100)) # x: 50, y: 100 translation
    cv.imshow("Translated - x: 0, y: 80",tr.move(sample1, 0, 80)) # x: 0, y: 80 translation
    
cv.destroyAllWindows() # Close all windows
exit(0) # Exit the program

