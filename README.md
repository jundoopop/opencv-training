# OpenCV Training Repository

This repository contains Python code examples and explorations related to learning computer vision concepts using the OpenCV library.

**Note:** This repository is currently undergoing refactoring to improve organization and clarity.

## Overview

The primary focus of this project is to practice and understand various image processing techniques. Code is organized into different directories based on the specific skill or concept being demonstrated.

## Directory Structure Highlights

* **/imageProcessing**: Contains implementations of core image processing algorithms.
  * `affine/`: Affine transformations
  * `blur/`: Image blurring techniques (e.g., Gaussian, Median)
  * `classification/`: Basic image classification examples
  * `detection/`: Object detection examples
  * `edgeDetection/`: Edge detection algorithms (e.g., Canny, Sobel)
  * `histogram/`: Histogram computation and manipulation (e.g., Equalization)
  * `hough/`: Hough transforms for line and circle detection
  * `interpolation/`: Image interpolation methods
  * `inverse/`: Image inversion
  * `morphology/`: Morphological operations (Erosion, Dilation, etc.)
  * `rotation/`: Image rotation
  * `simpleLines/`: Drawing lines on images
  * `transform/`: Geometric image transformations
* **/videoProcessing**: Examples related to video analysis (currently contains `tracking.py`).
* **/gui_painter**: Simple GUI application for drawing.
* **/etc**: Miscellaneous supporting files or older examples.

## Covered Topics

This repository explores the following computer vision and image processing topics:

* **Basic Image Operations:** Loading, displaying, saving images.
* **Geometric Transformations:** Affine transformations, rotation, scaling, perspective transform.
* **Image Filtering:** Blurring (Gaussian, Median, Bilateral), sharpening.
* **Edge Detection:** Canny, Sobel, Laplacian operators.
* **Histograms:** Calculation, equalization, analysis.
* **Morphological Operations:** Erosion, Dilation, Opening, Closing.
* **Feature Detection:** Hough transforms for lines and circles.
* **Object Detection/Classification:** Basic examples.
* **Image Segmentation:** (Implied through techniques like edge detection/morphology)
* **Video Processing:** Basic tracking.
* **GUI Interaction:** Mouse event handling for drawing.

## Dependencies

* Python 3.x
* OpenCV (`opencv-python`)
* NumPy

## How to Run

Navigate into the specific directory for the topic you are interested in and run the Python script. For example:

```bash
cd imageProcessing/edgeDetection
python canny.py
```

---
