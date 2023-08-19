import cv2
import numpy as np
print("balaji")

# Load image and convert to grayscale
img = cv2.imread('C:\\Users\\SUTHAKARAN.P\\PycharmProjects\\fuirts\\image\\pear1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Otsu's thresholding to binarize the image
ret, thresh = cv2.threshold(blur, 0, 150, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop over contours and classify each contour as healthy or diseased
for cnt in contours:
    # Calculate the contour area and bounding rectangle
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)

    # Calculate the aspect ratio of the bounding rectangle
    aspect_ratio = float(w) / h

    # If the aspect ratio is less than 1, rotate the rectangle
    if aspect_ratio < 1:
        angle = 90 - np.degrees(np.arctan2(h, w))
        M = cv2.getRotationMatrix2D((x + w / 2, y + h / 2), angle, 1)
        rotated_img = cv2.warpAffine(img, M, img.shape[:2][::-1], flags=cv2.INTER_CUBIC)
        rotated_gray = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2GRAY)
        rotated_thresh = cv2.threshold(rotated_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        cnts, hierarchy = cv2.findContours(rotated_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h

    # Classify the contour as healthy or diseased based on its aspect ratio
    if aspect_ratio > 1.2:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, 'Diseased', (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 0.9, (0, 0, 255), 2)
        #cv2.count('Diseased')
    else:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'HEALTHY', (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 0.9, (0, 255, 0), 2)
       # cv2.count("Healthy")

# Display the result
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
