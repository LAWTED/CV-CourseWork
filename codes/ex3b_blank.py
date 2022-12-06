# Image stitching using affine transform
import numpy as np
import cv2
import sys
import math
from matplotlib import pyplot as plt

im1 = cv2.imread('../inputs/building.jpg')
im2 = cv2.imread('../inputs/YOUR_OWN.jpg')
#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#

# Hough Transform using cv

def hough_transform(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Detect edges
    edges = cv2.Canny(gray_blur, 50, 150, apertureSize=3)
    # Detect lines using Hough
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    # Draw lines
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return img

im_result1 = hough_transform(im1)
im_result2 = hough_transform(im2)


##########################################################################################

cv2.imwrite('../results/ex3b_building_hough.jpg', im_result1)
cv2.imwrite('../results/ex3b_YOUR_OWN_hough.jpg', im_result2)
