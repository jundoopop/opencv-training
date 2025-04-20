import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
image_size = (32, 32)  # Resize images to 32x32
current_dir = os.getcwd()
folder_path = "photo_samples"  # Path to your dataset
categories = ["angular_leaf_spot", "bean_rust", "healthy"]  # List of categories

# Initialize data and labels lists
data = []
labels = []

# Load and preprocess images
for category in categories:
    path = os.path.join(current_dir, category)
    class_num = categories.index(category)

    for img in os.listdir(path):
        try:
            img_array = cv.imread(
                os.path.join(path, img), cv.IMREAD_GRAYSCALE
            )  # Convert to grayscale
            resized_array = cv.resize(img_array, image_size)  # Resize
            data.append(resized_array.flatten())  # Flatten and append to data
            labels.append(class_num)
        except Exception as e:
            pass

# Convert lists to numpy arrays
data = np.array(data, dtype="float32")
labels = np.array(labels)

# Initialize and train KNN
knn = cv.ml.KNearest_create()
knn.train(data, cv.ml.ROW_SAMPLE, labels)

# Now you can use knn.predict() to classify new images
knn.predict(np.array([data[0]]))
knn.predict(np.array([data[1]]))
