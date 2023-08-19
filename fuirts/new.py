# Import necessary libraries
import numpy as np
import cv2
from sklearn.cluster import KMeans

# Read input image
img = cv2.imread('C:\\Users\\SUTHAKARAN.P\\PycharmProjects\\fuirts\\image\\pear2.jpg')

# Convert the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Otsu's thresholding to the image
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Reshape the image into a 2D array of pixels
rows, cols = thresh.shape
X = thresh.reshape(rows * cols, 1)

# Apply KMeans clustering algorithm to the pixels
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Reshape the clustered pixels back into an image
clustered = kmeans.labels_.reshape(rows, cols)

# Extract the diseased region using the largest cluster
_, counts = np.unique(clustered, return_counts=True)
disease_label = np.argmax(counts)
disease_region = np.zeros((rows, cols), dtype=np.uint8)
disease_region[clustered == disease_label] = 255

# Display the original image and the detected diseased region
cv2.imshow('Original Image', img)
cv2.imshow('Diseased Region', disease_region)
cv2.waitKey(0)
cv2.destroyAllWindows()
