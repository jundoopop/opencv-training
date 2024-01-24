import numpy as np
import cv2 as cv
from pathlib import Path


def place_icons(image, size):
    image_path = Path.cwd() / "gui_painter" / "icons"
    icon_name = [
        "eraser",
        "line",
        "rectangle",
        "circle",
        "plus",
        "ellipse",
        "color-wheel",
        "save",
        "load",
        "clear",
        "paint-brush",
        "minus-sign",
    ]
    icons = [(i % 2, i // 2, 1, 1) for i in range(len(icon_name))]
    icons = np.multiply(icons, size * 2)  # type: ignore

    for roi, name in zip(icons, icon_name):
        x, y, w, h = roi
        icon = cv.imread(str(image_path / f"{name}.png"), cv.IMREAD_COLOR)
        if icon is None:
            raise FileNotFoundError(str(image_path / f"{name}.png"))
        image[y : y + h, x : x + w] = cv.resize(icon, size)

    return list(icons)


def create_hueIndex(image, roi):
    x, y, w, h = roi
    index = [[(j, 1, 1) for j in range(w)] for i in range(h)]
    ratios = (180 / w, 255, 255)
    hueIndex = np.multiply(index, ratios).astype(np.uint8)  # type: ignore
    image[y : y + h, x : x + w] = cv.cvtColor(hueIndex, cv.COLOR_HSV2BGR)


image = np.full((500, 800, 3), 255, np.uint8)
icons = place_icons(image, (50, 50))
cv.imshow("image", image)
cv.waitKey(0)
