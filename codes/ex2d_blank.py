# SIFT matching using OpenCV
import numpy as np
import cv2
import sys
import math
from matplotlib import pyplot as plt


im_gray1 = cv2.imread('../inputs/sift_input1.jpg', 0)
im_gray2 = cv2.imread('../inputs/sift_input2.jpg', 0)

#--------------------------------- WRITE YOUR CODE HERE ---------------------------------#




 











##########################################################################################

# Keypoint maps
cv2.imwrite('../results/ex2d_sift_input1.jpg', np.uint8(img_sift_kp_1))
cv2.imwrite('../results/ex2d_sift_input2.jpg', np.uint8(img_sift_kp_2))


# Feature Matching outputs
cv2.imwrite('../results/ex2d_matches_least50.jpg', np.uint8(img_least50))
cv2.imwrite('../results/ex2d_matches_most50.jpg', np.uint8(img_most50))